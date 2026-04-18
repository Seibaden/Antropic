"""
Google Finance → Notion 주가 자동 업데이트

설정:
  1. .env 파일에 NOTION_TOKEN, NOTION_DATABASE_ID 입력
  2. STOCKS 리스트에 종목 추가
  3. python stock_notion_updater.py 실행

Notion 데이터베이스 필요 컬럼 (Properties):
  - Ticker   : Title
  - Name     : Text
  - Price    : Number
  - Change   : Number
  - Change % : Number
  - Currency : Text
  - Updated  : Date
"""

import os
import re
import time
import logging
import requests
import schedule
import yfinance as yf
from bs4 import BeautifulSoup
from datetime import datetime, timezone
from notion_client import Client
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)

# ── 종목 설정 ──────────────────────────────────────────────────────────────────
# Google Finance 형식: "티커:거래소"
# yfinance 형식: 미국 "AAPL", 한국 "005930.KS"
STOCKS = [
    {"google": "AAPL:NASDAQ",   "yf": "AAPL",      "name": "Apple"},
    {"google": "GOOGL:NASDAQ",  "yf": "GOOGL",     "name": "Google"},
    {"google": "MSFT:NASDAQ",   "yf": "MSFT",      "name": "Microsoft"},
    {"google": "TSLA:NASDAQ",   "yf": "TSLA",      "name": "Tesla"},
    {"google": "005930:KRX",    "yf": "005930.KS", "name": "삼성전자"},
    {"google": "000660:KRX",    "yf": "000660.KS", "name": "SK하이닉스"},
]

# 매일 업데이트 실행 시각 (24시간 형식, 서버 로컬 시간 기준)
SCHEDULE_TIME = os.getenv("SCHEDULE_TIME", "09:00")
# ──────────────────────────────────────────────────────────────────────────────


_GF_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8",
}


def _fetch_google_finance(google_ticker: str) -> dict | None:
    """Google Finance HTML 스크래핑으로 주가 조회."""
    url = f"https://www.google.com/finance/quote/{google_ticker}"
    try:
        resp = requests.get(url, headers=_GF_HEADERS, timeout=10)
        resp.raise_for_status()
    except requests.RequestException as e:
        logger.warning(f"[Google Finance] {google_ticker} 요청 실패: {e}")
        return None

    soup = BeautifulSoup(resp.text, "html.parser")

    # 현재가
    price_tag = soup.find("div", class_=re.compile(r"YMlKec fxKbKc"))
    if not price_tag:
        logger.warning(f"[Google Finance] {google_ticker} 가격 파싱 실패")
        return None

    def _clean(text: str) -> float:
        return float(re.sub(r"[^\d.-]", "", text.replace(",", "")))

    try:
        price = _clean(price_tag.text)
    except ValueError:
        return None

    # 등락(절대값, %)
    change, change_pct = 0.0, 0.0
    change_tags = soup.find_all("div", class_=re.compile(r"JwB6zf"))
    if len(change_tags) >= 2:
        try:
            change = _clean(change_tags[0].text)
            change_pct = _clean(change_tags[1].text)
            # 하락이면 음수 처리
            pct_text = change_tags[1].text
            if "▼" in pct_text or "-" in pct_text:
                change = -abs(change)
                change_pct = -abs(change_pct)
        except ValueError:
            pass

    # 통화
    currency = "USD"
    cur_tag = soup.find("div", class_=re.compile(r"bLLb2d"))
    if cur_tag:
        currency = cur_tag.text.strip()

    return {"price": price, "change": change, "change_pct": change_pct, "currency": currency}


def _fetch_yfinance(yf_ticker: str) -> dict | None:
    """yfinance(Yahoo Finance)로 주가 조회 (Google Finance 실패 시 fallback)."""
    try:
        stock = yf.Ticker(yf_ticker)
        info = stock.fast_info
        price = round(float(info.last_price), 4)
        prev = round(float(info.previous_close), 4)
        change = round(price - prev, 4)
        change_pct = round((change / prev) * 100, 2) if prev else 0.0
        currency = getattr(info, "currency", "USD")
        return {"price": price, "change": change, "change_pct": change_pct, "currency": currency}
    except Exception as e:
        logger.error(f"[yfinance] {yf_ticker} 조회 실패: {e}")
        return None


def fetch_stock(stock: dict) -> dict | None:
    """Google Finance 우선, 실패 시 yfinance로 주가 조회."""
    data = _fetch_google_finance(stock["google"])
    if data:
        logger.info(f"[Google Finance] {stock['name']} ({stock['google']}) → {data['price']} {data['currency']}")
        return data

    logger.info(f"[Fallback → yfinance] {stock['name']} ({stock['yf']})")
    data = _fetch_yfinance(stock["yf"])
    if data:
        logger.info(f"[yfinance] {stock['name']} ({stock['yf']}) → {data['price']} {data['currency']}")
    return data


# ── Notion ────────────────────────────────────────────────────────────────────

def _build_properties(stock: dict, data: dict) -> dict:
    ticker = stock["google"].split(":")[0]
    now_iso = datetime.now(timezone.utc).isoformat()
    return {
        "Ticker":   {"title": [{"text": {"content": ticker}}]},
        "Name":     {"rich_text": [{"text": {"content": stock["name"]}}]},
        "Price":    {"number": data["price"]},
        "Change":   {"number": data["change"]},
        "Change %": {"number": data["change_pct"]},
        "Currency": {"rich_text": [{"text": {"content": data["currency"]}}]},
        "Updated":  {"date": {"start": now_iso}},
    }


def upsert_notion_row(notion: Client, database_id: str, stock: dict, data: dict):
    ticker = stock["google"].split(":")[0]
    props = _build_properties(stock, data)

    existing = notion.databases.query(
        database_id=database_id,
        filter={"property": "Ticker", "title": {"equals": ticker}},
    )

    if existing["results"]:
        page_id = existing["results"][0]["id"]
        notion.pages.update(page_id=page_id, properties=props)
        logger.info(f"[Notion] 업데이트: {stock['name']} ({ticker})")
    else:
        notion.pages.create(
            parent={"database_id": database_id},
            properties=props,
        )
        logger.info(f"[Notion] 새 행 생성: {stock['name']} ({ticker})")


# ── 메인 작업 ─────────────────────────────────────────────────────────────────

def run_update():
    token = os.getenv("NOTION_TOKEN")
    db_id = os.getenv("NOTION_DATABASE_ID")

    if not token or not db_id:
        logger.error("NOTION_TOKEN 또는 NOTION_DATABASE_ID가 설정되지 않았습니다. .env 파일을 확인하세요.")
        return

    notion = Client(auth=token)
    logger.info(f"=== 주가 업데이트 시작 ({datetime.now().strftime('%Y-%m-%d %H:%M:%S')}) ===")

    for stock in STOCKS:
        data = fetch_stock(stock)
        if data:
            upsert_notion_row(notion, db_id, stock, data)
        time.sleep(1)  # 요청 간 간격

    logger.info("=== 주가 업데이트 완료 ===")


def main():
    logger.info(f"스케줄러 시작 — 매일 {SCHEDULE_TIME}에 업데이트합니다.")
    schedule.every().day.at(SCHEDULE_TIME).do(run_update)

    # 시작 시 즉시 1회 실행
    run_update()

    while True:
        schedule.run_pending()
        time.sleep(30)


if __name__ == "__main__":
    main()
