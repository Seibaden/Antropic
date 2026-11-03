# Claude 셋업 공유용 Confluence 페이지 작성 가이드

> **목적:** Claude로 셋업한 내용을 동료에게 설명하는 Confluence 페이지를 만들 때 쓰는 가이드입니다.
> 페이지 하나에 **① 작업 흐름(Workflow) ② 핵심 포인트(Key Point) ③ 새로 추가된 개념 설명**을 담습니다.
> 작성일: 2026-11-03

---

## 0. 한눈에 보기

| 항목 | 핵심 |
|---|---|
| **독자** | Claude를 처음 쓰는 동료 (개념을 모르는 사람 기준으로 작성) |
| **페이지가 답해야 할 질문** | 무엇을 셋업했나? 왜 했나? 어떻게 동작하나? 나는 뭘 하면 되나? |
| **구성 순서** | 요약 → 배경 → 작업 흐름 → 핵심 포인트 → 새 개념 → 사용법 → FAQ |
| **분량** | 페이지 1개 + 필요하면 하위 페이지 (개념 상세, 트러블슈팅) |
| **시각 요소** | 흐름도 1개, 비교 표(Before/After) 1개, 패널은 화면당 2개 이하 |
| **첫 화면에서 끝내기** | 스크롤하지 않아도 "무엇을, 왜, 나에게 무슨 영향"이 보이게 |

---

## 1. 참고 자료 링크

### 1-1. Confluence 공식 템플릿 / 가이드
- [Confluence 템플릿 갤러리 (Software & IT)](https://atlassian.com/software/confluence/templates/categories/software-development-and-it) — How-to, 요구사항, 회고, 의사결정 템플릿 등을 미리 볼 수 있음
- [Confluence 템플릿 갤러리 75+ 개편 소개 (Atlassian Blog)](https://www.atlassian.com/blog/confluence/new-templates-for-confluence)
- [How-To Article Blueprint (Atlassian 공식)](https://confluence.atlassian.com/display/DOC/How-To+Article+Blueprint) — "사용법" 섹션 뼈대로 활용
- [Creating your Technical Documentation Space (Atlassian 공식, 구버전)](https://confluence.atlassian.com/spaces/CONF54/pages/428803611/Creating+your+Technical+Documentation+Space) — 기술 문서용 스페이스 구성, 권한 설정
- [There's a Confluence template for that (Atlassian Community)](https://community.atlassian.com/t5/Confluence-articles/There-s-a-Confluence-template-for-that/ba-p/2735283) — `/decision` 매크로 등 의사결정 기록 방법

### 1-2. 작업 흐름(프로세스) 문서 작성법
- [Confluence 프로세스 문서 템플릿 만들기 (ONES)](https://ones.com/blog/?p=1146386) — "목적·대상 → 흐름도 요약 → 트리거/사전조건 → 단계별 절차(담당 역할 포함)" 구조
- [팀 워크플로 인덱스 페이지 구성 (ONES)](https://ones.com/blog/?p=1135983) — 관련 프로세스를 한 곳에 모으는 인덱스 페이지
- [Example Confluence pages for engineering teams (DocuWriter)](https://www.docuwriter.ai/posts/example-confluence-pages) — API 문서, 런북 등 예제 페이지 모음 (제품 홍보 성격 있음)

### 1-3. 개념 설명 문서 작성법
- [Diátaxis — Explanation(설명) 문서](https://diataxis.fr/explanation/) — "왜 이렇게 되어 있는가"를 설명하는 문서 작성 원칙
- [Diátaxis — How-to 가이드](https://diataxis.fr/how-to-guides/) — "어떻게 하는가" 문서와 개념 설명을 분리하는 이유
- [Google Developer Documentation Style Guide](https://developers.google.com/style)

### 1-4. 페이지를 보기 좋게 만들기
- [How to Make Beautiful Pages in Confluence (Atlassian Community)](https://community.atlassian.com/t5/Confluence-articles/How-to-Make-Beautiful-Pages-in-Confluence/bc-p/2169206)
- [Five native ways to make a Confluence page look modern](https://community.atlassian.com/forums/discussion/3283354/five-native-ways-to-make-a-confluence-page-look-modern-and-where-macros-fit) — 추가 앱 없이 기본 기능만 사용

### 1-5. Claude 셋업 설명에 인용할 자료 (개념 설명용)
- [Claude Code 공식 문서 — `.claude` 디렉터리 구조](https://code.claude.com/docs/en/claude-directory) — CLAUDE.md, settings, skills 파일이 어디에 있는지
- [Claude Code 공식 문서 — 설정 문제 진단(Debug your config)](https://code.claude.com/docs/en/debug-your-config) — `/memory`, `/skills`, `/hooks`, `/mcp` 로 로드 상태 확인
- [Claude Code 공식 문서 — Memory (CLAUDE.md)](https://code.claude.com/docs/en/memory)
- [Claude Code 공식 문서 — Skills](https://code.claude.com/docs/en/skills)
- [Claude Code 공식 문서 — Hooks](https://code.claude.com/docs/en/hooks)
- [Claude Code 공식 문서 — MCP](https://code.claude.com/docs/en/mcp)
- [Claude Code 공식 문서 — Settings](https://code.claude.com/docs/en/settings)
- [How to give Claude Code context: CLAUDE.md, skills, MCP (Falconer)](https://falconer.com/guides/claude-code-context/) — 팀 공유 관점 정리 (비공식)
- [Claude Code Setup 2026: MCP Servers, Hooks, Skills (okhlopkov)](https://www.okhlopkov.com/claude-code-setup-mcp-hooks-skills-2026/) — 개인 셋업 사례 (비공식)

> 참고: 1-2, 1-5의 비공식 블로그는 개인/벤더 의견입니다. 개념 정의나 파일 위치처럼 정확해야 하는 내용은 **공식 문서(code.claude.com) 링크를 근거로** 적으세요.

---

## 2. 페이지 구조 설계

### 2-1. 권장 페이지 트리

```
📂 [팀명] AI 활용 / Claude
├── 📄 Claude 셋업 소개 — 작업 흐름과 핵심 개념   ← 이번에 만들 메인 페이지
│   ├── 📄 새 개념 상세: CLAUDE.md / Skills / MCP / Hooks
│   ├── 📄 따라 하기: 내 PC에서 사용 시작하기
│   └── 📄 FAQ & 트러블슈팅
└── 📄 변경 이력 (셋업이 바뀔 때마다 기록)
```

- 메인 페이지 하나만 읽어도 전체 그림이 이해되어야 합니다.
- 개념 설명이 길어지면 하위 페이지로 빼고 메인에는 **3줄 요약 + 링크**만 남깁니다.

### 2-2. 메인 페이지 섹션 순서 (이유 포함)

| # | 섹션 | 담을 내용 | 이유 |
|---|---|---|---|
| 1 | **페이지 정보** | 작성자, 대상, 최종 수정일, 상태 | 문서를 믿어도 되는지 판단 |
| 2 | **TL;DR (요약)** | 3~5줄: 무엇을, 왜, 효과 | 바쁜 동료는 여기까지만 읽음 |
| 3 | **배경 / 문제** | 기존 방식의 불편함 | "왜 바꿨는지" 공감대 형성 |
| 4 | **전체 작업 흐름** | 흐름도 1개 + 단계 설명 | 동작 방식을 한눈에 |
| 5 | **핵심 포인트** | 꼭 알아야 할 3~5가지 | 실수 방지, 기억할 것 |
| 6 | **새로 추가된 개념** | 개념별 카드 (정의·역할·예시) | 처음 보는 용어 해소 |
| 7 | **Before / After** | 기존 vs 변경 비교 표 | 변화가 무엇인지 확실히 |
| 8 | **사용 방법** | 단계별 따라 하기 | 바로 써볼 수 있게 |
| 9 | **FAQ / 주의사항** | Expand로 접어 두기 | 페이지가 길어지지 않게 |
| 10 | **참고 링크 / 문의처** | 공식 문서, 담당자, 채널 | 더 알고 싶을 때 |

---

## 3. 섹션별 작성법

### 3-1. TL;DR — 첫 화면에서 끝내기
- **Info 패널** 1개 안에 3~5줄로 씁니다.
- 공식: `무엇을` + `왜` + `결과(숫자가 있으면 숫자)` + `내가 할 일`

> 예) "Claude Code에 팀 공통 규칙(CLAUDE.md)과 반복 작업용 Skill 3개, Notion·Gmail 연동(MCP)을 셋업했습니다. 반복 문서 작업이 수동 30분에서 5분으로 줄었습니다. 저장소를 받으면 셋업이 자동으로 적용되며, 8장의 '시작하기'만 따라 하면 됩니다."

### 3-2. 작업 흐름 (Workflow)
**그리는 도구** (Confluence 안에서)
- `/whiteboard` 또는 `/draw.io` (앱 설치 시) — 편집 가능한 흐름도
- Mermaid는 기본 Confluence에서 렌더링되지 않으므로 앱(Mermaid for Confluence 등)이 있을 때만 사용
- 도구가 없으면 **번호 단계 + 화살표 표**로도 충분

**흐름도 작성 규칙**
- 단계는 **5~8개**. 넘으면 하위 흐름으로 분리
- 각 상자는 **"누가 + 무엇을"** (예: "개발자: 요청 입력", "Claude: Skill 실행")
- 사람 / Claude / 외부 시스템을 **색으로 구분** (예: 사람 = 파랑, Claude = 보라, 외부 시스템 = 회색)
- 흐름도 바로 아래에 **같은 번호의 단계 설명 표**를 붙이기

**단계 설명 표 형식**

| 단계 | 누가 | 무엇을 | 결과물 / 다음 단계 |
|---|---|---|---|
| ① | 사용자 | Claude에게 작업 요청 | 요청 프롬프트 |
| ② | Claude | CLAUDE.md 규칙을 읽고 작업 계획 | 실행 계획 |
| ③ | Claude | 필요한 Skill / MCP 도구 실행 | 중간 결과 |
| ④ | Hook | 정해진 검사 자동 실행 (포맷, 테스트 등) | 통과 / 실패 |
| ⑤ | 사용자 | 결과 검토 후 승인 | 커밋 / 공유 |

**흐름도 예시 (텍스트로 그린 초안)**

```
 [사용자] 요청 입력
      │
      ▼
 [Claude] CLAUDE.md(팀 규칙) 로드 ──► 작업 계획
      │
      ├──► [Skill] 반복 작업 절차 실행
      │
      ├──► [MCP] 외부 서비스 연동 (Notion, Gmail, GitHub …)
      │
      ▼
 [Hook] 자동 검사 (포맷 / 테스트 / 금지 명령 차단)
      │
      ▼
 [사용자] 결과 검토 ──► 승인 / 수정 요청
```

### 3-3. 핵심 포인트 (Key Point)
- **3~5개만.** 7개를 넘으면 아무것도 기억에 남지 않습니다.
- 형식: **굵은 한 줄 제목 + 1~2줄 설명**
- 반드시 지켜야 하는 것(보안, 금지 사항)은 **Warning 패널**로 분리
- 3열 레이아웃에 "카드" 형태로 배치하면 눈에 잘 들어옵니다.

```
┌──────────────────┬──────────────────┬──────────────────┐
│ 🎯 규칙은 한 곳에  │ 🔁 반복은 Skill로  │ 🔒 비밀값은 금지   │
│ 팀 규칙은 저장소의 │ 3번 이상 반복하는  │ API 키·토큰은      │
│ CLAUDE.md에서만    │ 작업은 Skill로     │ 문서·코드·프롬프트 │
│ 관리합니다.        │ 만들어 공유합니다. │ 에 넣지 않습니다.  │
└──────────────────┴──────────────────┴──────────────────┘
```

### 3-4. 새로 추가된 개념 설명 — "개념 카드" 패턴
새 개념은 **항상 같은 순서**로 설명하면 독자가 쉽게 비교합니다.

| 순서 | 항목 | 작성 요령 |
|---|---|---|
| 1 | **한 줄 정의** | 전문용어 없이 20자 내외 |
| 2 | **비유** | 이미 아는 것에 빗대기 (예: "신입에게 주는 업무 매뉴얼") |
| 3 | **왜 필요한가** | 없을 때 생기는 문제 |
| 4 | **어디에 있나** | 파일 경로 / 설정 위치 |
| 5 | **우리 팀 예시** | 실제로 셋업한 내용 1~2개 |
| 6 | **확인 방법** | 명령어 / 화면 (예: `/memory`, `/mcp`) |
| 7 | **더 보기** | 공식 문서 링크 |

**개념 간 관계를 표로 정리** — 개념이 여러 개면 개별 설명 앞에 비교 표를 먼저 둡니다.

| 개념 | 한 줄 정의 | 언제 동작? | 강제력 | 위치 |
|---|---|---|---|---|
| **CLAUDE.md** | Claude가 항상 읽는 팀 규칙 메모 | 세션 시작 시 항상 | 권고 (지침) | 저장소 루트 `CLAUDE.md` |
| **Skill** | 필요할 때 꺼내 쓰는 작업 매뉴얼 | 관련 작업일 때만 | 권고 (절차) | `.claude/skills/<이름>/SKILL.md` |
| **MCP** | 외부 서비스와 연결하는 플러그 | 도구 호출 시 | — (연결 통로) | `.mcp.json` |
| **Hook** | 특정 시점에 자동 실행되는 스크립트 | 이벤트 발생 시 (예: 파일 수정 후) | **강제** (항상 실행) | `.claude/settings.json` 의 `hooks` |
| **Settings / 권한** | 허용·차단할 명령 목록 | 도구 실행 전 | **강제** | `.claude/settings.json` |

> 💡 공식 문서의 구분: **CLAUDE.md는 "우리는 이렇게 한다"는 지침**, **권한(permissions)과 Hook은 "절대 일어나면 안 되는 일"을 보장하는 장치**입니다. 이 구분을 페이지에 꼭 적어 두면 오해가 줄어듭니다.

### 3-5. Before / After 비교 표
변화를 가장 빠르게 전달하는 방법입니다.

| 항목 | 기존 (Before) | 변경 후 (After) |
|---|---|---|
| 팀 코딩 규칙 전달 | 매번 프롬프트에 설명 | CLAUDE.md에 한 번 작성, 자동 적용 |
| 반복 작업 | 사람마다 다른 방식 | Skill로 표준화 |
| 외부 도구 연동 | 복사·붙여넣기 | MCP로 직접 조회·작성 |
| 품질 검사 | 잊으면 누락 | Hook이 자동 실행 |

### 3-6. 사용 방법 (따라 하기)
- How-To Article 형식: **사전 준비 → 번호 단계 → 완료 확인**
- 명령어는 반드시 **Code Block 매크로** (복사 버튼 제공)
- 단계마다 "이렇게 보이면 성공" 문장 또는 스크린샷 추가
- 개인 설정과 팀 공유 설정을 구분해 적기
  - 팀 공유(저장소에 커밋): `CLAUDE.md`, `.claude/settings.json`, `.claude/skills/`, `.mcp.json`
  - 개인 전용(커밋 안 함): `~/.claude/` 아래 파일, `.claude/settings.local.json`

---

## 4. 예제 페이지 (그대로 복사해서 수정)

> 아래는 메인 페이지 예시입니다. `[ ]` 부분만 실제 내용으로 바꾸세요.
> 이 저장소에 있는 **주가 → Notion 자동 업데이트 스크립트**를 예시 소재로 썼습니다.

---

**[페이지 제목] Claude 셋업 소개 — 작업 흐름과 핵심 개념**

| 작성자 | 대상 | 최종 수정일 | 상태 |
|---|---|---|---|
| @[작성자] | [팀명] 전체 | 2026-11-03 | 🟢 최신 (Status 매크로) |

ℹ️ **[Info 패널] 요약 (TL;DR)**
- Claude Code에 **팀 규칙(CLAUDE.md)**, **반복 작업 Skill**, **Notion·Gmail 연동(MCP)** 을 셋업했습니다.
- 예: 매일 주요 종목 주가를 Notion 데이터베이스에 자동 기록하고, 정리한 문서를 메일로 바로 보냅니다.
- 저장소를 받으면 팀 설정이 자동 적용됩니다. → **[8. 시작하기]** 만 따라 하세요.

**목차** (Table of Contents 매크로)

## 1. 배경
- 기존: 주가 확인 → 엑셀 정리 → Notion 붙여넣기를 매일 수동으로 반복 ([약 20분/일])
- 문제: 담당자마다 형식이 다르고, 누락이 생겨도 알 수 없음
- 목표: 반복 작업은 자동화하고, 사람은 검토만 하기

## 2. 전체 작업 흐름
(Whiteboard / draw.io 흐름도 삽입)

| 단계 | 누가 | 무엇을 | 결과 |
|---|---|---|---|
| ① | 사용자 | Claude에게 "오늘 주가 업데이트해줘" 요청 | 요청 |
| ② | Claude | CLAUDE.md에서 팀 규칙(형식, 종목 목록 위치) 확인 | 작업 계획 |
| ③ | Claude | `stock_notion_updater.py` 실행 → 가격 수집 | 종목별 가격 |
| ④ | MCP (Notion) | Notion DB에 행 추가/갱신 | 업데이트된 DB |
| ⑤ | MCP (Gmail) | 요약을 담당자에게 메일 발송 | 알림 메일 |
| ⑥ | 사용자 | Notion·메일 결과 확인 | 완료 |

## 3. 핵심 포인트
(3열 레이아웃)
- 🎯 **종목 추가는 코드 한 곳에서** — `STOCKS` 목록만 수정합니다.
- 🔁 **실행 시각은 환경 변수로** — `SCHEDULE_TIME` (기본 09:00)
- 🔒 **토큰은 `.env` 에만** — Notion 토큰을 코드·문서·채팅에 붙여넣지 마세요.

⚠️ **[Warning 패널]** `.env` 파일은 절대 커밋하지 않습니다. 토큰이 유출되면 즉시 Notion에서 재발급하세요.

## 4. 새로 추가된 개념
(개념 비교 표 — 3-4절의 표를 그대로 사용)

▶ **(Expand) CLAUDE.md — Claude가 항상 읽는 팀 규칙 메모**
- 비유: 신입에게 주는 "우리 팀 일하는 방식" 한 장 요약
- 왜: 매번 같은 설명을 반복하지 않으려고
- 위치: 저장소 루트 `CLAUDE.md` (200줄 이하 권장)
- 우리 예시: "날짜는 YYYY-MM-DD", "종목 목록은 `STOCKS`에서만 관리"
- 확인: Claude Code에서 `/memory`
- 더 보기: [공식 문서](https://code.claude.com/docs/en/memory)

▶ **(Expand) Skill — 필요할 때만 꺼내 쓰는 작업 매뉴얼**
- 비유: 서랍 속 업무 체크리스트. 관련 작업을 할 때만 꺼냄
- 위치: `.claude/skills/<이름>/SKILL.md` (폴더 안에 SKILL.md가 있어야 인식됨)
- 우리 예시: [주간 리포트 작성 Skill]
- 확인: `/skills`
- 더 보기: [공식 문서](https://code.claude.com/docs/en/skills)

▶ **(Expand) MCP — 외부 서비스와 연결하는 플러그**
- 비유: Claude에 꽂는 USB 어댑터 (Notion, Gmail, GitHub …)
- 위치: 저장소의 `.mcp.json` (팀 공유) / 개인 연결은 개인 설정
- 우리 예시: Notion(DB 갱신), Gmail(결과 메일 발송)
- 확인: `/mcp` — 연결 실패 시 "failed"로 표시
- 더 보기: [공식 문서](https://code.claude.com/docs/en/mcp)

▶ **(Expand) Hook — 정해진 시점에 무조건 실행되는 자동 검사**
- 비유: 문을 닫으면 자동으로 잠기는 도어락. 잊어버릴 수 없음
- 위치: `.claude/settings.json` 의 `"hooks"` 항목
- 우리 예시: [파일 수정 후 자동 포맷 / `.env` 수정 차단]
- 확인: `/hooks`
- 더 보기: [공식 문서](https://code.claude.com/docs/en/hooks)

## 5. Before / After
(3-5절 형식의 표)

## 6. 시작하기
1. 저장소를 받습니다.
   ```
   git clone [저장소 주소]
   ```
2. 필요한 패키지를 설치합니다.
   ```
   pip install -r requirements.txt
   ```
3. `.env` 파일을 만들고 `NOTION_TOKEN`, `NOTION_DATABASE_ID` 를 입력합니다.
4. 실행합니다.
   ```
   python stock_notion_updater.py
   ```

✅ **[Success 패널]** Notion 데이터베이스에 오늘 날짜의 가격이 보이면 성공입니다.

## 7. FAQ
▶ (Expand) Q. Claude가 팀 규칙을 무시하는 것 같아요 → `/memory` 로 CLAUDE.md가 로드됐는지 확인
▶ (Expand) Q. Notion 연결이 안 돼요 → `/mcp` 에서 상태 확인, 토큰과 DB 공유 설정 확인
▶ (Expand) Q. 내 개인 설정을 팀에 영향 없이 바꾸려면? → `.claude/settings.local.json` 사용

## 8. 참고 링크 & 문의
- 공식 문서: [Claude Code `.claude` 디렉터리](https://code.claude.com/docs/en/claude-directory), [설정 문제 진단](https://code.claude.com/docs/en/debug-your-config)
- 문의: @[담당자] / #[채널명]
- 변경 이력: [변경 이력 페이지 링크]

---

## 5. 작성 팁

1. **독자는 "Claude를 처음 쓰는 동료"** — 셋업한 사람에게 당연한 것(경로, 명령어, 용어)도 다 적습니다.
2. **개념 설명 → 사용법 순서를 지키기** — 개념을 모른 채 따라 하면 문제가 생겼을 때 대응하지 못합니다.
3. **"왜"를 빼먹지 않기** — 셋업 내용은 바뀌어도 이유는 오래 유효합니다.
4. **실제 예시를 쓰기** — 일반론보다 "우리 팀의 ○○ Skill"이 훨씬 이해가 빠릅니다.
5. **강제 vs 권고 구분** — Hook·권한(강제)과 CLAUDE.md·Skill(권고)을 섞어 설명하지 않습니다.
6. **비밀값 노출 금지** — 스크린샷·코드 예시에 토큰, 사내 주소, 개인정보가 없는지 확인합니다.
7. **흐름도는 하나만** — 여러 개가 필요하면 전체 흐름 1개 + 하위 페이지로 나눕니다.
8. **발표용으로도 쓸 수 있게** — 섹션 하나가 슬라이드 하나가 되도록 짧게 끊습니다.

---

## 6. 사용 매크로 요약

| 매크로 | 쓰는 곳 |
|---|---|
| `Page Properties` | 상단 페이지 정보 표 |
| `Status` | 최신 / 검토 중 / 폐기 예정 표시 |
| `Info` / `Success` / `Warning` 패널 | 요약, 성공 확인, 보안 주의 |
| `Table of Contents` | 상단 목차 |
| `Whiteboard` / `draw.io` | 작업 흐름도 |
| `Layout` 3열 | 핵심 포인트 카드 |
| `Expand` | 개념 상세, FAQ |
| `Code Block` | 명령어, 설정 예시 |
| `Children Display` | 하위 페이지 목록 |
| `/decision` | "왜 이 방식을 선택했는가" 결정 기록 |

---

## 7. 게시 전 체크리스트

- [ ] 첫 화면(스크롤 없이)에서 **무엇을 / 왜 / 내가 할 일**이 보이는가?
- [ ] 흐름도의 단계 번호와 설명 표 번호가 일치하는가?
- [ ] 핵심 포인트가 5개 이하인가?
- [ ] 새 개념마다 **정의·비유·위치·우리 예시·확인 방법·공식 링크**가 있는가?
- [ ] 강제 장치(Hook, 권한)와 권고(CLAUDE.md, Skill)를 구분해 설명했는가?
- [ ] 토큰·비밀번호·사내 주소가 노출되지 않았는가?
- [ ] 명령어는 Code Block으로 넣어 복사 가능한가?
- [ ] 담당자·최종 수정일·문의 채널이 적혀 있는가?
- [ ] Claude를 처음 쓰는 동료 1명이 이 페이지만 보고 따라 해 봤는가?
