# Confluence 유저 매뉴얼 작성 가이드

> 가시성 좋고, 깔끔하고, 찾기 쉬운 Confluence 유저 매뉴얼을 만들기 위한 실전 가이드
> 작성일: 2026-11-03

---

## 0. 한눈에 보기 (TL;DR)

| 원칙 | 한 줄 요약 |
|---|---|
| **구조 먼저** | 글을 쓰기 전에 페이지 트리(목차)부터 설계한다 |
| **한 페이지 = 한 목적** | 길어지면 하위 페이지로 쪼갠다 |
| **훑어 읽기 가능하게** | 제목·번호 목록·표·스크린샷으로 텍스트 벽을 없앤다 |
| **강조는 아껴서** | 패널(Info/Note/Warning)은 화면당 최대 2개 |
| **템플릿으로 일관성** | 모든 매뉴얼 페이지는 같은 뼈대를 쓴다 |
| **유지보수 설계** | 담당자·최종 검토일·버전을 페이지 상단에 명시 |

---

## 1. 참고 웹페이지 링크

### 1-1. Atlassian 공식 문서
- [How-To Article Blueprint (Confluence 공식)](https://confluence.atlassian.com/display/DOC/How-To+Article+Blueprint) — 단계별 사용법 문서용 기본 템플릿. 저장 시 인덱스 페이지가 자동 생성됨
- [Working with Page Layouts, Columns and Sections](https://confluence.atlassian.com/spaces/CONF43/pages/297675578/Working+with+Page+Layouts+and+Columns+and+Sections) — 레이아웃/컬럼/섹션 활용법 (구버전 문서지만 개념은 동일)

### 1-2. Confluence 문서화 베스트 프랙티스
- [Effective Documentation with Confluence: Templates, Macros, and Structure (Univ. of Waterloo)](https://uwaterloo.ca/atlassian/blog/effective-documentation-confluence-templates-macros-and) — 템플릿·매크로·구조 잡기
- [Best Practices for Documentation in Confluence (Mad Devs)](https://maddevs.io/blog/best-practices-for-documentation-in-confluence) — 목차, 계층 구조, 간결한 작성
- [Confluence documentation best practices (Refined)](https://www.refined.com/blog/confluence-documentation-best-practices)
- [10 Confluence Best Practices Your Users Should Know (Stiltsoft)](https://stiltsoft.com/blog/10-confluence-best-practices-your-users-should-know/)
- [Documentation best practices (Gliffy)](https://www.gliffy.com/blog/documentation-best-practices) — 다이어그램 활용 관점

### 1-3. 페이지 디자인 / 보기 좋게 만들기
- [How to Make Beautiful Pages in Confluence (Atlassian Community)](https://community.atlassian.com/t5/Confluence-articles/How-to-Make-Beautiful-Pages-in-Confluence/bc-p/2169206)
- [Five native ways to make a Confluence page look modern (Atlassian Community)](https://community.atlassian.com/forums/discussion/3283354/five-native-ways-to-make-a-confluence-page-look-modern-and-where-macros-fit) — 앱 없이 기본 기능만으로
- [How to use Confluence macros to organize your documentation (Refined)](https://www.refined.com/blog/how-to-use-confluence-macros-to-organize-your-documentation)
- [5 Confluence macros to transform your documentation (Refined)](https://www.refined.com/blog/5-confluence-macros-to-transform-your-documentation)
- [Tips to Contextualize Confluence Content with Panels, Footnotes… (Atlassian Community)](https://community.atlassian.com/t5/App-Central/Tips-to-Contextualize-Confluence-Content-with-Panels-Footnotes/ba-p/2782471)
- [How to Make Your Confluence Pages More Attractive (Stiltsoft)](https://stiltsoft.com/?p=2963)

### 1-4. 유저 매뉴얼 / 지식베이스 구조
- [How to create an End-user document for a software (Atlassian Community Q&A)](https://community.atlassian.com/t5/Confluence-questions/Hi-Everyone-How-to-create-an-End-user-document-for-a-software/qaq-p/1305802)
- [7 Confluence templates to level up your self-service knowledge base](https://community.atlassian.com/forums/App-Central-articles/7-Confluence-templates-to-level-up-your-self-service-knowledge/ba-p/3142911)
- [Setting up a knowledge base in Confluence (Appfire)](https://appfire.atlassian.net/wiki/spaces/USECASES/pages/478511457/Setting+up+a+knowledge+base+in+Confluence)
- [User Manuals with Confluence (K15t)](https://www.k15t.com/solutions/user-manuals) — PDF/Word 내보내기·버전 관리가 필요할 때 (유료 앱)

### 1-5. 글쓰기 스타일 가이드 (문장 품질)
- [Google Developer Documentation Style Guide](https://developers.google.com/style)
- [Microsoft Writing Style Guide](https://learn.microsoft.com/style-guide/welcome/)
- [Diátaxis 프레임워크](https://diataxis.fr/) — 문서를 튜토리얼 / How-to / 레퍼런스 / 설명 4종으로 나누는 방법론

> 참고: Refined, Stiltsoft, Appfire, K15t 등은 유료 앱 벤더 블로그라 자사 앱을 추천하는 경우가 많습니다. 핵심 원칙(레이아웃·패널·Expand·절제)은 **기본 기능만으로도** 충분히 적용 가능합니다.

---

## 2. 스페이스 & 페이지 트리 설계

글을 쓰기 전에 **목차부터** 확정합니다. 정리 안 된 평평한 스페이스는 몇 달 안에 검색 불가능한 상태가 됩니다.

### 권장 페이지 트리 예시

```
📘 [제품명] 유저 매뉴얼 (스페이스 홈)
├── 🚀 시작하기
│   ├── 제품 소개
│   ├── 계정 생성 및 로그인
│   └── 5분 빠른 시작 (Quick Start)
├── 🧭 기능별 사용법 (How-to)
│   ├── 기능 A 사용하기
│   ├── 기능 B 사용하기
│   └── ...
├── ⚙️ 설정 및 관리
│   ├── 사용자 권한 설정
│   └── 알림 설정
├── 📖 레퍼런스
│   ├── 화면/메뉴 설명
│   ├── 용어집 (Glossary)
│   └── 단축키
├── ❓ FAQ & 문제 해결 (Troubleshooting)
└── 📝 릴리스 노트 / 변경 이력
```

### 설계 원칙
- **깊이는 3단계 이내** — 그 이상이면 사용자가 길을 잃음
- **페이지 제목은 동사형/목적형** — "결재 기능" ❌ → "결재 요청하기" ✅
- **Diátaxis 4분류**를 섹션 기준으로 쓰면 자연스럽게 정리됨
  - 튜토리얼(배우기) → *시작하기*
  - How-to(작업 수행) → *기능별 사용법*
  - 레퍼런스(정보 조회) → *레퍼런스*
  - 설명(이해) → *제품 소개, 개념 설명*
- 자주 묻는 질문은 FAQ로 분리하고, 본문에서 링크로 연결

---

## 3. 스페이스 홈(랜딩 페이지) 구성

스페이스 홈은 "매뉴얼의 표지 + 내비게이션"입니다.

**레이아웃 추천:** 상단 1컬럼 → 하단 3컬럼

```
┌──────────────────────────────────────────────┐
│  [배너 이미지 / 제품 로고]                      │
│  📘 [제품명] 유저 매뉴얼                        │
│  한 줄 소개 · 🔍 검색창(Livesearch 매크로)       │
├──────────────┬──────────────┬────────────────┤
│ 🚀 시작하기   │ 🧭 사용법     │ ❓ 도움이 필요?  │
│ - 빠른 시작   │ - 기능 A      │ - FAQ          │
│ - 로그인      │ - 기능 B      │ - 문제 해결     │
│              │              │ - 문의 채널     │
├──────────────┴──────────────┴────────────────┤
│ 📝 최근 업데이트 (Recently Updated 매크로)       │
└──────────────────────────────────────────────┘
```

**사용 매크로**
- `Livesearch` — 스페이스 내 검색창
- `Children Display` / `Page Tree` — 하위 페이지 자동 목록
- `Recently Updated` — 최근 변경 문서
- `Info Panel` — 공지/안내 1개

---

## 4. 개별 매뉴얼 페이지 표준 템플릿

모든 How-to 페이지가 같은 뼈대를 쓰면 사용자는 "어디에 무엇이 있는지" 학습하게 됩니다.

```
[페이지 제목: ○○ 하기]

┌ Page Properties (페이지 속성 표) ─────────────┐
│ 대상 사용자 │ 일반 사용자 / 관리자              │
│ 소요 시간   │ 약 3분                          │
│ 담당자      │ @담당자                         │
│ 최종 검토일 │ 2026-11-03                      │
│ 상태        │ [최신] (Status 매크로, 초록)      │
└─────────────────────────────────────────────┘

## 개요
이 문서에서는 ○○하는 방법을 설명합니다. (1~2문장)

ℹ️ [Info 패널] 시작 전 필요 사항
- 권한: ○○ 권한 필요
- 사전 작업: ○○ 완료

## 목차
(Table of Contents 매크로 — 페이지가 길 때만)

## 단계별 진행
1. **[메뉴명]** 을 클릭합니다.
   (스크린샷 — 클릭 위치에 빨간 박스/번호 표시)
2. ○○ 항목에 값을 입력합니다.
3. **[저장]** 을 클릭합니다.

✅ [Success/Tip 패널] 완료되면 ○○ 화면이 표시됩니다.

## 주의 사항
⚠️ [Warning 패널] 삭제한 데이터는 복구할 수 없습니다.

## 자주 묻는 질문
▶ (Expand 매크로) Q. ○○가 안 보여요
▶ (Expand 매크로) Q. ○○를 취소하려면?

## 관련 문서
- [다음 단계: △△ 하기]
- [□□ 설정 방법]
```

> 💡 Confluence의 **How-To Article Blueprint**를 기반으로 위 구조를 스페이스 템플릿으로 저장해 두면, 새 페이지 생성 시 자동으로 적용됩니다. (관리자 권한이 없다면 "template" 라벨을 단 페이지를 만들어 복사해서 사용)

---

## 5. 가시성을 높이는 시각 요소 활용법

### 5-1. 패널(Panel) — 의미별로 색을 고정
| 패널 | 용도 | 예 |
|---|---|---|
| ℹ️ **Info (파랑)** | 참고 정보, 사전 조건 | "이 기능은 관리자만 사용 가능합니다" |
| ✅ **Success / Tip (초록)** | 팁, 완료 결과 | "단축키 Ctrl+S로 빠르게 저장" |
| 📝 **Note (보라/노랑)** | 알아두면 좋은 내용 | "변경 사항은 5분 후 반영됩니다" |
| ⚠️ **Warning (주황/빨강)** | 데이터 손실·되돌릴 수 없는 작업 | "삭제 후 복구 불가" |

- **화면당 최대 2개**까지만. 남발하면 아무것도 눈에 안 띔
- 패널 안 내용은 **3줄 이내**. 길면 본문이나 Expand로
- 패널 안에 표·이미지 넣지 않기

### 5-2. 레이아웃(Layout)
- 긴 텍스트는 1컬럼(가독성 최고)
- 비교·나란히 보기만 2컬럼 (예: "설정 전 / 설정 후")
- 3컬럼은 랜딩 페이지 내비게이션 용도로만

### 5-3. 스크린샷
- **잘라서(crop)** 필요한 영역만 보여주기
- 클릭할 위치에 **빨간 박스 + 번호(①②③)** 를 표시하고, 본문 단계 번호와 일치시키기
- 가로 폭 통일 (예: 본문 폭 기준 600~800px), 테두리(border) 적용
- 개인정보·실제 고객 데이터는 반드시 마스킹

### 5-4. 기타 유용한 매크로
| 매크로 | 용도 |
|---|---|
| `Table of Contents` | 긴 페이지 상단 목차 |
| `Expand` | FAQ, 상세 설명, 고급 옵션 접기 |
| `Status` | 최신 / 검토 중 / 폐기 예정 라벨 |
| `Page Properties` + `Page Properties Report` | 문서 메타데이터 + 전체 문서 현황표 |
| `Excerpt` / `Excerpt Include` | 공통 문구(주의사항 등) 한 곳에서 관리 후 재사용 |
| `Include Page` | 공통 섹션 재사용 |
| `Children Display` | 하위 페이지 자동 목록 |
| `Code Block` | 명령어·설정값 (복사하기 쉬움) |
| `Jira Issue` | 관련 이슈/개선 요청 연결 |
| 다이어그램(draw.io / Gliffy / Whiteboard) | 업무 흐름, 화면 흐름도 |

---

## 6. 글쓰기 원칙

1. **사용자 관점 & 능동태** — "버튼이 클릭되면…" ❌ → "**[저장]** 을 클릭합니다." ✅
2. **한 단계 = 한 동작** — 번호 목록 한 줄에 동작 하나만
3. **UI 요소 표기 통일** — 버튼/메뉴명은 **굵게** 또는 `[대괄호]`, 화면 표시 그대로
4. **경로 표기** — **설정 > 사용자 관리 > 권한** 처럼 `>`로 통일
5. **결과를 알려주기** — 각 주요 단계 뒤 "○○ 화면이 나타납니다"
6. **문장은 짧게** — 한 문장 한 개념, 문단은 3~4줄 이내
7. **용어 통일** — 용어집 페이지를 만들고 같은 대상은 항상 같은 단어로
8. **조건은 앞에** — "관리자 권한이 있는 경우, **[삭제]** 를 클릭합니다."

---

## 7. 일관성 체크리스트 (스타일 규칙)

- [ ] 제목 계층: H1(페이지 제목) → H2(섹션) → H3(하위) — H4 이하 사용 자제
- [ ] 이모지는 섹션 아이콘 용도로만, 페이지 트리 최상위에 통일된 세트 사용
- [ ] 날짜 형식 통일 (YYYY-MM-DD)
- [ ] 표 헤더 행은 항상 강조(헤더 행 설정)
- [ ] 페이지 폭: 긴 표/다이어그램 페이지만 "전체 폭(Full width)", 나머지는 기본 폭
- [ ] 스크린샷 스타일(테두리, 강조 색상) 통일
- [ ] 모든 페이지에 라벨(label) 부여 → 검색·필터 용이 (예: `manual`, `how-to`, `기능A`)

---

## 8. 유지보수 & 거버넌스

- **페이지 오너 지정**: Page Properties에 담당자 명시
- **정기 검토**: 분기 1회 "최종 검토일" 기준으로 오래된 문서 점검 (Page Properties Report로 한눈에 확인)
- **상태 라벨 운영**: `최신(초록)` / `검토 중(노랑)` / `폐기 예정(빨강)`
- **변경 이력**: 큰 변경은 릴리스 노트 페이지에 기록, 페이지 버전 기록(History) 활용
- **권한**: 편집 권한은 필요한 사람에게만, 읽기는 넓게
- **피드백 채널**: 각 페이지 하단에 "이 문서가 도움이 되었나요? 문의: #채널/담당자" 문구
- **내보내기 필요 시**: PDF/Word 배포가 필요하면 스페이스 내보내기 또는 Scroll PDF Exporter 등 앱 검토

---

## 9. 작업 순서 (실행 계획)

1. **대상 독자 정의** — 일반 사용자 / 관리자 / 신규 입사자 등
2. **페이지 트리 설계** — 2장 구조를 기반으로 목차 확정
3. **템플릿 제작** — 4장 표준 템플릿을 스페이스 템플릿으로 등록
4. **스페이스 홈 구성** — 3장 레이아웃으로 랜딩 페이지 제작
5. **핵심 페이지 3~5개 먼저 작성** — 빠른 시작 + 가장 많이 쓰는 기능
6. **실제 사용자 1~2명에게 리뷰** — "이 문서만 보고 따라 할 수 있는가?"
7. **피드백 반영 후 나머지 페이지 확장**
8. **정기 검토 일정 등록**

---

## 10. 최종 품질 체크리스트

- [ ] 처음 보는 사람이 **3클릭 이내**에 원하는 문서에 도달하는가?
- [ ] 페이지 상단만 보고 "이 문서가 무엇이고 누구를 위한 것인지" 알 수 있는가?
- [ ] 단계 번호와 스크린샷 번호가 일치하는가?
- [ ] 패널이 화면당 2개 이하인가?
- [ ] 모든 페이지에 담당자·최종 검토일·라벨이 있는가?
- [ ] 모바일(Confluence 앱)에서도 깨지지 않는가? (3컬럼·큰 표 주의)
- [ ] 깨진 링크나 오래된 스크린샷이 없는가?
