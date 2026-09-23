# 🚀 LG Electronics · Gemini Enterprise & Antigravity 2.0 실무 핸즈온 가이드

> **화면만 보고 바로 따라하는 직관적 실습 매뉴얼 (`Step-by-Step Visual Guide`)**  
> 복잡한 이론 설명 대신 **① 화면 어디를 클릭하는지(실제 UI 캡처)** ➔ **② 무엇을 복사해서 붙여넣는지(프롬프트·코드)** ➔ **③ 어떤 화면이 나오면 성공인지(결과 UI)** 순서로만 구성했습니다.
>
> * 🌐 **라이브 웹페이지 버전 (좌측 목차 · 원클릭 복사 · 이미지 확대)**: **[https://gorock-afk.github.io/LG_workshop_ge_agy_a/](https://gorock-afk.github.io/LG_workshop_ge_agy_a/)**
> * 📂 **실습 파일 폴더 (Google Drive)**: [실습 파일 전체 다운로드](https://drive.google.com/drive/folders/1dxqldyrsQ7oSRi-d1ieRdDVJmTmQ0r2V)
> * 📊 **발표 슬라이드 원본 (Google Slides)**: [교안 슬라이드 열기](https://docs.google.com/presentation/d/1IYXVTVUEw_TKte4I1Ff31scmNEY7ueXCZ2i8AKiZWog/edit)

![워크샵 대표 아키텍처](assets/screenshots/slide_01_ui_1.png)

---

## 🗺️ 한눈에 보는 오늘 실습 로드맵 (3시간 · 하나의 마스터 대시보드 완성)

오늘 실습은 따로 노는 예제를 여러 개 만드는 것이 아닙니다.  
**1부(크롬 브라우저)**에서 만든 **LG 가전 주간 트렌드 보고서**를 **2부(Antigravity 데스크톱 앱)**로 가져와 **5장 발표용 웹 슬라이드**로 만들고, 여기에 **실시간 주가·환율·뉴스 탭**과 **LG 5대 가전 920행 실적 분석 탭**을 차례대로 붙여 **총 4개 탭으로 구성된 사내 인텔리전스 포털**을 완성합니다.

![5단계 누적 빌드업 로드맵 다이어그램](assets/screenshots/slide_02_ui_1.png)

| 순서 | 실습 환경 | 내가 직접 만드는 결과물 | 핵심 포인트 |
| :--- | :---: | :--- | :--- |
| **Part 1 (30분)** | 🌐 크롬 GE Web | **LG AI 가전·OLED 주간 트렌드 보고서 초안** | `Project` 팀 공유 + 사내 양식(`01_template.md`) 고정 |
| **Part 2 (30분)** | 🌐 크롬 GE Web | **내 Gmail 임시보관함(Drafts)에 자동 생성된 보고 메일** | `Workflow` 3단계 노드 연결 + **`HITL` 사람 승인 버튼** |
| **Part 3 (30분)** | 💻 Antigravity 2.0 | **LG 시그니처 레드(`#A50034`) 5장 발표용 웹 슬라이드** | 세팅 점검 + 4대 커맨드(`/grill-me`·`/plan`·`/btw`·`/learn`) |
| **Part 4 (30분)** | 💻 Antigravity 2.0 | **3개 탭 포털 (탭1: 슬라이드 / 탭2·3: 실시간 주가·환율·뉴스)** | **15줄 무인증 파이썬 코드** ➔ `/lg-live-market` 스킬 등록 & `/schedule` |
| **Part 5 (1시간)** | 💻 Antigravity 2.0 | **4번째 `[LG 5대 가전 실적·구독]` 탭 통합 & 95점 품질 검증** | `@04_lg_appliance_data.csv`(920행) 정제 + `/browser` + **새 세션 95점 게이트** |

---

## 📦 실습 파일 8종 바로 받기 (`./files/`)

아래 파일 이름을 클릭하면 바로 내용을 보거나 다운로드할 수 있습니다. 실습 전 내 PC의 `LG_Workshop` 폴더에 넣어두세요.

| 번호 | 파일명 (클릭 시 열기) | 언제 쓰나요? | 파일 설명 |
| :---: | :--- | :---: | :--- |
| **01** | [`01_GE_Workflow_lg_weekly_report_template.md`](./files/01_GE_Workflow_lg_weekly_report_template.md) | **Part 1** | 크롬 GE `Project Knowledge`에 업로드할 **LG 주간 보고서 표준 양식** |
| **02** | [`02_AG_Webpage_hello_world_slides.html`](./files/02_AG_Webpage_hello_world_slides.html) | **Part 3** | 키보드 좌우 화살표(`←`/`→`)로 넘기는 **5장 웹 슬라이드 기본 뼈대** |
| **03** | [`02_AG_Webpage_lg_brand_slides_SKILL.md`](./files/02_AG_Webpage_lg_brand_slides_SKILL.md) | **Part 3** | LG 시그니처 레드(`#A50034`) 디자인 규칙을 고정하는 **`SKILL.md`** |
| **04** | [`03_AG_Dashboard_fetch_lg_live_market.py`](./files/03_AG_Dashboard_fetch_lg_live_market.py) | **Part 4** | **API 키·설치 불필요!** 15줄 무인증 LG전자(`066570`) 시세·환율·뉴스 수집 코드 |
| **05** | [`03_AG_Dashboard_lg_live_market_SKILL.md`](./files/03_AG_Dashboard_lg_live_market_SKILL.md) | **Part 4** | 15줄 파이썬 코드를 `/lg-live-market` 스킬로 등록하는 정의서 |
| **06** | [`04_AG_Analytics_lg_appliance_data.csv`](./files/04_AG_Analytics_lg_appliance_data.csv) | **Part 5** | LG 5대 가전(`OLED evo`·`워시타워`·`디오스`·`HVAC`·`스탠바이미`) **920행 실무 데이터** |
| **07** | [`04_AG_Analytics_design_guidelines.md`](./files/04_AG_Analytics_design_guidelines.md) | **Part 5** | 대시보드 디자인 및 가전 데이터 정제 상시 규칙 (`.agents/rules/`) |
| **08** | [`05_Instructor_Solution_app.py`](./files/05_Instructor_Solution_app.py) | **완성본** | Part 3~5 전체 4개 탭이 하나로 합쳐진 최종 완성본 코드 |

---

# 🌐 [1부 · 크롬 브라우저] Part 1. GE Project & 사내 양식(Knowledge) 세팅 (30분)

### 🔹 Step 1-1. 팀 공유용 Project 생성 및 동료 초대하기

> **💡 핵심 포인트**: 개인 채팅창에서 프롬프트를 치면 나만 쓸 수 있지만, **`Project`**를 만들어 양식을 넣어두면 **`Invite+`로 초대한 팀원 모두가 똑같은 사내 보고서 양식으로 AI를 사용**할 수 있습니다.

![Step 1-1 프로젝트 생성 및 팀원 초대 화면](assets/screenshots/slide_04_ui_1.png)

#### 👆 화면 보고 그대로 따라하기
1. **좌측 사이드바 `Projects` 클릭**: 크롬에서 Gemini Enterprise 웹 화면 좌측 메뉴의 **`Projects` ➔ `+ New Project`** 버튼을 클릭합니다.
2. **프로젝트 이름 입력**: **`LG 가전/TV 글로벌 주간 인텔리전스`** 라고 입력하고 생성합니다.
3. **우측 상단 `Invite+` 클릭 (팀 공유)**: 우측 상단 **`Invite+`** 버튼을 눌러 옆자리 동료(또는 팀원 이메일)를 **`Editor`** 권한으로 초대합니다.

---

### 🔹 Step 1-2. 사내 보고서 양식(`01_template.md`) 업로드 & 맞춤 지침 고정하기

> **💡 핵심 포인트**: 매번 "표로 정리해줘, 출처 적어줘"라고 말할 필요 없이, **사내 표준 보고서 양식 파일(`Knowledge`)**과 **3줄 고정 규칙(`Instructions`)**을 프로젝트에 박아둡니다.

![Step 1-2 Knowledge 파일 업로드 및 Instructions 입력 화면](assets/screenshots/slide_05_ui_1.png)

#### 👆 화면 보고 그대로 따라하기
1. **우측 `Project Knowledge`에 파일 업로드**:
   - 우측 패널 **`Project Knowledge` (`+ Add file`)** 영역에 실습 파일 **[`01_GE_Workflow_lg_weekly_report_template.md`](./files/01_GE_Workflow_lg_weekly_report_template.md)** 를 마우스로 끌어다 놓습니다.
2. **그 아래 `Custom Instructions` 입력창에 아래 3줄 복사·붙여넣기 후 `Save` 클릭**:

```text
1. 모든 답변과 보고서는 반드시 첨부된 '01_GE_Workflow_lg_weekly_report_template.md' 양식 목차와 표 구조를 100% 준수해 작성한다.
2. LG전자 제품군 표기는 사내 표준 명칭(LG 올레드 evo, LG 트롬 오브제컬렉션 워시타워, 디오스 오브제컬렉션 냉장고, LG 휘센 AI 시스템에어컨)으로 통일한다.
3. 모든 수치 변화율(YoY, MoM) 뒤에는 괄호로 근거 출처와 기준 일자를 반드시 병기하고, 마지막에 실무 액션 아이템 3가지를 제시한다.
```

3. **채팅창 테스트 (아래 한 줄만 입력해 보고서 양식대로 나오는지 확인)**:

```text
북미 AI 가전 및 글로벌 프리미엄 OLED TV 최근 1주일 시장 동향과 경쟁사 프로모션 변화를 요약해줘.
```

---

# ⚡ [1부 · 크롬 브라우저] Part 2. GE Workflow & Gmail 초안 자동화 (30분)

### 🔹 Step 2-1. 3단계 워크플로우 노드 연결하기 (`Schedule` ➔ `Research` ➔ `Gmail Draft`)

> **💡 핵심 포인트**: 매주 월요일 아침마다 직접 검색할 필요 없이, **스케줄러가 리서치를 돌리고 내 Gmail 임시보관함(`Drafts`)에 보고 메일 초안까지 만들어 두도록** 파이프라인을 연결합니다.

![Step 2-1 워크플로우 3단계 노드 연결 화면](assets/screenshots/slide_07_ui_1.png)

#### 👆 화면 보고 그대로 따라하기
1. 좌측 메뉴 **`Workflows` ➔ `+ Create Workflow`** 버튼을 클릭합니다.
2. 캔버스에 아래 순서대로 **3개의 노드를 추가(`+`)**하여 화살표로 연결합니다:
   - **노드 1 (`Trigger`)**: `Schedule` 선택 ➔ 매주 월요일 오전 08:30 (`Every Monday 08:30 AM`)
   - **노드 2 (`Action 1`)**: `Gemini Research` 선택 ➔ 연결할 프로젝트로 방금 만든 **`LG 가전/TV 글로벌 주간 인텔리전스`** 지정
   - **노드 3 (`Action 2`)**: `Gmail - Create Draft` 선택 (발송이 아닌 안전한 **임시보관함 초안 생성**)

---

### 🔹 Step 2-2. 앞 단계 리서치 결과(`{Step2.output}`)를 Gmail 본문에 자동 꽂아넣기

> **💡 핵심 포인트**: 2번 노드가 작성한 보고서 전문을 **변수 태그(`{Step2.output}`)** 하나로 3번 Gmail 노드의 메일 본문(`Body`)에 그대로 넘겨줍니다.

![Step 2-2 노드 프롬프트 및 변수 바인딩 화면](assets/screenshots/slide_08_ui_1.png)

#### 👆 화면 보고 그대로 따라하기
1. **2번 노드(`Gemini Research`) 클릭 후 `Prompt` 칸에 아래 내용 복사·붙여넣기**:

```text
최근 7일간의 글로벌 AI 스마트홈 가전(워시타워·냉장고·에어컨) 및 프리미엄 OLED TV 주요 뉴스, 북미 가전 유통사(BestBuy·HomeDepot) 가격 프로모션 동향, 에너지 효율 규제 이슈를 조사하여 프로젝트 표준 양식(01_GE_Workflow_lg_weekly_report_template.md)에 맞춰 주간 보고서를 작성해줘.
```

2. **3번 노드(`Gmail - Create Draft`) 클릭 후 각 칸에 아래 내용 입력**:
   - **To (수신자)**: `본인 이메일 주소 입력`
   - **Subject (제목)**: `[주간 트렌드 보고] LG AI 가전 & OLED 글로벌 마켓 인텔리전스 ({CurrentDate})`
   - **Body (본문)**: 우측 파란색 **`+ Insert Variable`** 버튼을 눌러 **`{Step2.output}`** 선택

---

### 🔹 Step 2-3. 사람 승인 게이트(`HITL`) 켜고 내 Gmail 임시보관함에서 초안 확인하기

> **💡 핵심 포인트**: AI가 임의로 메일을 보내는 사고를 막기 위해 **`Require approval` (Human-in-the-Loop)** 스위치를 켜두면, **사람이 `[Approve]` 버튼을 눌렀을 때만** Gmail 임시보관함에 저장됩니다.

![Step 2-3 HITL 승인 팝업 및 Gmail 임시보관함 확인 화면](assets/screenshots/slide_09_ui_1.png)

#### 👆 화면 보고 그대로 따라하기
1. **3번 노드(`Gmail Draft`) 하단의 `Require approval before creating draft` 스위치 ON**: 승인 토글을 켭니다.
2. **우측 상단 `Run Test` 클릭**: 워크플로우가 돌아가다가 3번 노드 앞에서 멈추며 화면에 **`[Approve]` / `[Edit]`** 미리보기 창이 뜹니다.
3. **`[Approve]` 클릭 후 Gmail 확인**: 새 탭에서 **Gmail ➔ `임시보관함(Drafts)`**을 열어 주간 트렌드 보고서 메일이 깔끔하게 들어와 있는지 확인합니다. *(이 메일 본문을 잠시 후 Part 3에서 복사해 사용합니다!)*

---

# 💻 [2부 · 데스크톱 앱] Part 3. Antigravity 세팅 점검 & LG 브랜드 5장 웹 슬라이드 제작 (30분)

### 🔹 Step 3-0. [필수] 실습 시작 전 Antigravity 세팅 & 권한 점검하기

> **⚠️ 실습 전 가장 먼저 확인하세요!**  
> 에이전트가 파일을 만들고 브라우저 프리뷰를 띄우려면 **실행 권한 세팅이 `Disabled`(꺼짐)로 되어 있지 않은지** 꼭 점검해야 합니다.

| ① Settings(⚙️) 권한 세팅 점검 (`Disabled` 해제 확인) | ② 상단 모델(`Gemini 3.8 Flash`) & 워크스페이스 폴더 점검 |
| :---: | :---: |
| ![세팅 점검 1 - 권한 설정 확인](assets/screenshots/slide_11_ui_1.png) | ![세팅 점검 2 - 모델 및 폴더 확인](assets/screenshots/slide_11_ui_2.png) |

#### 👆 위 두 화면을 보고 그대로 체크하기
1. **왼쪽 화면(`① 권한 점검`)**: 좌측 하단 **톱니바퀴(`Settings` ⚙️)** 아이콘 클릭 ➔ `Agent` / `Tools` 실행 권한 항목들이 **`Disabled`로 막혀 있지 않고 활성화(`Auto` 또는 `Ask`)** 되어 있는지 확인합니다.
2. **오른쪽 화면(`② 모델·폴더 점검`)**:
   - 좌측 탐색기(`Explorer`)에 오늘 실습 폴더(**`LG_Workshop`**)가 열려 있고 `02~04`번 실습 파일들이 보이는지 확인합니다.
   - 우측 채팅창 상단 모델이 **`Gemini 3.8 Flash`**로 선택되어 있는지 확인합니다.

---

### 🔹 Step 3-1. Antigravity 4대 핵심 슬래시 커맨드(`/grill-me` · `/plan` · `/btw` · `/learn`) 익히기

> **💡 핵심 포인트**: 프롬프트를 길게 고민할 필요 없이, **4가지 슬래시 커맨드**로 **① 기획 인터뷰(`/grill-me`) ➔ ② 설계도 승인(`/plan`) ➔ ③ 중간 간섭(`/btw`) ➔ ④ 스킬 저장(`/learn`)** 루프를 돌립니다.

| ① `/grill-me` (역질문으로 기획 구체화) | ② `/plan` & `/btw` (설계 승인 및 중간 지시) | ③ `/learn` (작업 규칙을 스킬로 저장) |
| :---: | :---: | :---: |
| ![4대 커맨드 1 - grill-me](assets/screenshots/slide_12_ui_1.png) | ![4대 커맨드 2 - plan 및 btw](assets/screenshots/slide_12_ui_2.png) | ![4대 커맨드 3 - learn](assets/screenshots/slide_12_ui_3.png) |

#### 👆 채팅창에 순서대로 입력해 보기
1. **`/grill-me` (왼쪽 화면)**: 애매한 요청을 던지면 에이전트가 알아서 3가지 핵심 질문(보고 대상, 강조 지표, 슬라이드 장수)을 먼저 물어봅니다.
   ```text
   /grill-me Part 2에서 만든 LG 가전 주간 보고서를 본부장님 보고용 5장짜리 인터랙티브 웹 슬라이드로 만들고 싶어. 먼저 나한테 핵심 질문 3가지만 해줘.
   ```
2. **`/plan` & `/btw` (가운데 화면)**: 질문에 답한 뒤 `/plan`으로 5장 구성안을 승인하고, 코딩 도중 `/btw`로 디자인 요청을 끼워 넣습니다.
   ```text
   /btw 우측 상단에 'LG AI Appliance Weekly' 뱃지를 고정하고, 키보드 좌우 방향키(←, →)로 슬라이드가 넘어가게 해줘.
   ```

---

### 🔹 Step 3-2. `/learn`으로 LG 시그니처 디자인(`#A50034`)을 재사용 스킬(`SKILL.md`)로 박제하기

> **💡 핵심 포인트**: 방금 맞춘 LG 브랜드 컬러(`#A50034`)와 5장 카드 레이아웃을 **`/learn`** 명령어로 저장해 두면, `.agents/skills/lg-brand-slides/SKILL.md` 파일이 생성되어 다음주부터는 **`/lg-brand-slides` 한 마디로 똑같은 퀄리티의 장표**가 나옵니다.

| ① `.agents/skills/lg-brand-slides/SKILL.md` 생성 확인 | ② 생성된 `SKILL.md` 내부 디자인 규칙 확인 |
| :---: | :---: |
| ![SKILL.md 폴더 생성 확인](assets/screenshots/slide_13_ui_1.png) | ![SKILL.md 내부 코드 상세](assets/screenshots/slide_13_ui_2.png) |

#### 👆 채팅창에 아래 명령어 복사·붙여넣기
```text
/learn 방금 합의한 LG전자 시그니처 레드(#A50034) 배너, #F3F4F6 라이트그레이 KPI 카드 그리드, 키보드 좌우 화살표(←/→) 슬라이드 전환 규칙을 'lg-brand-slides'라는 이름의 스킬(.agents/skills/lg-brand-slides/SKILL.md)로 저장해줘.
```
> 💡 직접 타이핑하기 번거로우신 분은 실습 폴더의 **[`02_AG_Webpage_lg_brand_slides_SKILL.md`](./files/02_AG_Webpage_lg_brand_slides_SKILL.md)** 파일을 `.agents/skills/lg-brand-slides/SKILL.md` 위치에 복사해 넣으셔도 동일하게 작동합니다.

---

### 🔹 Step 3-3. 기본 뼈대(`02_AG_Webpage_hello_world_slides.html`) 띄워 슬라이드 넘김 확인하기

![Step 3-3 Hello World 5장 웹 슬라이드 구동 화면](assets/screenshots/slide_14_ui_1.png)

#### 👆 화면 보고 그대로 따라하기
1. 좌측 파일 탐색기에서 **[`02_AG_Webpage_hello_world_slides.html`](./files/02_AG_Webpage_hello_world_slides.html)** 파일을 클릭합니다.
2. 우측 아티팩트 프리뷰 창에서 키보드 **좌우 화살표(`←` / `→`)**를 눌러 1페이지부터 5페이지까지 부드럽게 넘어가는지 확인합니다.

---

### 🔹 Step 3-4. `/lg-brand-slides` 스킬 + Gmail 보고서 본문 ➔ LG 브랜드 5장 웹 슬라이드 완성!

| ① 채팅창에 `/lg-brand-slides` + Gmail 본문 붙여넣기 | ② 완성된 LG 시그니처 레드(`#A50034`) 5장 웹 슬라이드 |
| :---: | :---: |
| ![Step 3-4 프롬프트 입력 화면](assets/screenshots/slide_15_ui_1.png) | ![Step 3-4 완성된 LG 5장 웹 슬라이드](assets/screenshots/slide_15_ui_2.png) |

#### 👆 채팅창에 아래 프롬프트 복사·붙여넣기
```text
/lg-brand-slides 스킬을 적용해서 @02_AG_Webpage_hello_world_slides.html 파일을 업데이트해줘.
아래에 붙여넣는 Part 2 Gmail 임시보관함 주간 보고서 내용을 바탕으로:
- Slide 1: LG AI 가전 & OLED 주간 핵심 요약 (KPI 카드 3개)
- Slide 2: 제품군별(올레드 evo / 워시타워 / 디오스 / 휘센) 시장 동향 비교표
- Slide 3: 북미·유럽 주요 유통 채널 프로모션 및 경쟁사 동향
- Slide 4: 리스크 요인 및 에너지 효율 규제 대응 포인트
- Slide 5: 본부별 추천 액션 아이템 Top 3
로 채운 뒤 우측 프리뷰 화면에 바로 띄워줘.

[여기에 Part 2 Gmail 임시보관함 보고서 본문 붙여넣기]
```

---

# 📊 [2부 · 데스크톱 앱] Part 4. 15줄 무인증 파이썬 스킬(`/lg-live-market`) & 실시간 대시보드 확장 (30분)

### 🔹 Step 4-1. Part 3 웹 슬라이드를 `1번 탭`으로 보존하고 좌측 사이드바 3개 탭 대시보드 만들기

> **💡 핵심 포인트**: 방금 만든 5장 웹 슬라이드를 버리지 않고 **좌측 사이드바 `1번 탭`에 그대로 보존**한 뒤, **`2번 탭(LG전자 실시간 주가·환율)`**과 **`3번 탭(실시간 뉴스 피드)`**을 옆에 추가합니다.

![Step 4-1 좌측 사이드바 3탭 대시보드 통합 화면](assets/screenshots/slide_17_ui_1.png)

#### 👆 채팅창에 아래 프롬프트 복사·붙여넣기
```text
방금 완성한 5장짜리 LG 주간 트렌드 웹 슬라이드를 버리지 말고 그대로 보존해서, 좌측 사이드바 네비게이션이 있는 통합 대시보드(app.py)로 확장해줘.
- [탭 1. 주간 트렌드 웹 슬라이드]: 방금 만든 5장 HTML 슬라이드를 페이지네이션 그대로 임베딩
- [탭 2. LG전자(066570) 실시간 시세 & 글로벌 환율]: 실시간 주가·등락률 KPI 카드 및 USD/KRW, EUR 환율 패널
- [탭 3. 글로벌 가전 실시간 뉴스 피드]: 최신 뉴스 5건 헤드라인·발행일·원문 링크 테이블
로 3개 탭 레이아웃을 먼저 구성해줘.
```

---

### 🔹 Step 4-2. 15줄 무인증 파이썬 코드(`03_fetch_lg_live_market.py`)를 `/lg-live-market` 스킬로 등록해 연동하기

> **💡 핵심 포인트**: 복잡한 DART API 키 발급이나 `pip install` 없이도, **파이썬 기본 내장 `urllib` 15줄 코드([`03_AG_Dashboard_fetch_lg_live_market.py`](./files/03_AG_Dashboard_fetch_lg_live_market.py))**를 **Antigravity 스킬(`/lg-live-market`)**로 등록해 **LG전자(`066570`) 실시간 주가 + `USD/KRW` 환율 + 구글 뉴스 RSS 5건**을 2·3번 탭에 즉시 꽂아 넣습니다.

![Step 4-2 15줄 무인증 파이썬 코드 스킬 등록 및 실시간 연동 화면](assets/screenshots/slide_18_ui_1.png)

#### 🐍 우리가 스킬로 등록할 15줄 무인증 파이썬 코드 (`03_AG_Dashboard_fetch_lg_live_market.py`)
```python
import urllib.request, urllib.parse, json, xml.etree.ElementTree as ET

def fetch_lg_live_dashboard_data(stock_code="066570", keyword="LG전자 AI 가전"):
    headers = {"User-Agent": "Mozilla/5.0"}
    # 1. [No-Key] 네이버 금융 LG전자(066570) 실시간 주가·등락률 JSON
    req = urllib.request.Request(f"https://m.stock.naver.com/api/stock/{stock_code}/basic", headers=headers)
    stock = json.loads(urllib.request.urlopen(req, timeout=5).read().decode("utf-8"))
    # 2. [No-Key] Frankfurter(ECB) 실시간 USD/KRW · EUR 글로벌 환율 JSON
    fx = json.loads(urllib.request.urlopen("https://api.frankfurter.dev/v1/latest?base=USD&symbols=KRW,EUR,JPY", timeout=5).read().decode("utf-8"))
    # 3. [No-Key] Google News RSS 실시간 'LG전자 AI 가전' 최신 뉴스 5건
    rss_url = f"https://news.google.com/rss/search?q={urllib.parse.quote(keyword)}&hl=ko&gl=KR&ceid=KR:ko"
    root = ET.fromstring(urllib.request.urlopen(rss_url, timeout=5).read())
    news = [{"title": item.findtext("title"), "pubDate": item.findtext("pubDate"), "link": item.findtext("link")} for item in root.findall(".//item")[:5]]
    return {"stock_name": stock.get("stockName", "LG전자"), "close_price": stock.get("closePrice"), "fluctuation_rate": stock.get("fluctuationsRatio"), "usd_krw": fx["rates"]["KRW"], "latest_news": news}
```

#### 👆 채팅창에 아래 프롬프트 복사·붙여넣기 (스킬 등록 + 2·3번 탭 실시간 연동)
```text
[1단계: 스킬 등록] @03_AG_Dashboard_fetch_lg_live_market.py (15줄 무인증 코드)를 '.agents/skills/lg-live-market/' 폴더 아래에 SKILL.md와 스크립트로 등록해줘.
[2단계: 스킬 실행 및 대시보드 연동] 방금 등록한 /lg-live-market 스킬을 실행해서 가져온 LG전자(066570) 실시간 주가·등락률과 USD/KRW 환율을 대시보드 [탭 2] KPI 카드에 바인딩하고, 실시간 구글 뉴스 5건을 [탭 3] 뉴스 리스트에 연결해줘.
```

---

### 🔹 Step 4-3. 실시간 `[뉴스/시세 Pull]` 수동 갱신 버튼 & `/schedule` 매일 아침 9시 자동화

| ① 우측 상단 `[오늘의 LG 트렌드 & 뉴스 Pull]` 버튼 클릭 | ② `/schedule` 매일 오전 9시 자동 갱신 스케줄러 등록 |
| :---: | :---: |
| ![Step 4-3 실시간 Pull 버튼 동작 화면](assets/screenshots/slide_19_ui_1.png) | ![Step 4-3 schedule 자동화 설정 화면](assets/screenshots/slide_19_ui_2.png) |

#### 👆 채팅창에 아래 프롬프트 복사·붙여넣기
```text
1. 대시보드 우측 상단에 '[🔄 오늘의 LG 시세 & 뉴스 실시간 Pull]' 버튼을 추가하고, 버튼을 누르면 /lg-live-market 스킬 함수가 즉시 재실행되어 현재 시각 타임스탬프와 함께 최신 주가·환율·뉴스로 새로고침되게 해줘.
2. /schedule 매일 오전 9시 정각에 /lg-live-market 스킬을 자동 실행해 대시보드 캐시 데이터를 최신 상태로 업데이트하도록 예약해줘.
```

---

# 📈 [2부 · 데스크톱 앱] Part 5. LG 5대 가전 920행 데이터 Analytics & 95점 검증 게이트 (1시간)

### 🔹 Step 5-0. Part 5 전체 흐름 한눈에 보기 (`Rules` ➔ `@CSV 정제` ➔ `4번째 탭 통합` ➔ `/browser` & `95점 게이트`)

![Step 5-0 가전 데이터 분석 및 95점 검증 게이트 전체 아키텍처](assets/screenshots/slide_21_ui_1.png)

1. **상시 규칙 자동 적용 (`.agents/rules/design_guidelines.md`)**: 실습 파일 [`04_AG_Analytics_design_guidelines.md`](./files/04_AG_Analytics_design_guidelines.md)를 `.agents/rules/` 폴더에 넣어두면, 별도로 말하지 않아도 **LG 브랜드 컬러(`#A50034`)와 환율 환산 기준(`1 USD = 1,380 KRW`), 결측치 제거 규칙**이 모든 프롬프트에 자동 적용됩니다.

---

### 🔹 Step 5-1. `@04_AG_Analytics_lg_appliance_data.csv` (920행) 호출 및 더티 데이터 자동 정제

> **💡 왜 정제가 필요한가요?**  
> 실제 현업에서 내려받은 [`04_AG_Analytics_lg_appliance_data.csv`](./files/04_AG_Analytics_lg_appliance_data.csv) (LG 5대 가전 920행 데이터) 안에는 **① 결측치(빈칸) 23건**, **② 매출 `0원` 오류 레코드 6건**, **③ `KRW`/`USD` 통화 단위 혼재**, **④ 날짜 포맷 불일치(`YYYY-MM-DD` vs `YYYY/MM/DD`)**가 섞여 있습니다. 에이전트에게 `@파일명`만 멘션해 전수 진단 및 정제를 시킵니다.

![Step 5-1 920행 가전 데이터 결측치 23건 및 0원 6건 자동 정제 화면](assets/screenshots/slide_22_ui_1.png)

#### 👆 채팅창에 아래 프롬프트 복사·붙여넣기
```text
@04_AG_Analytics_lg_appliance_data.csv (920행) 파일의 데이터 품질을 전수 스캔해서:
1. 결측치(빈 값 23건)와 매출액 0원 오류 레코드(6건)가 어느 컬럼·제품군에 있는지 요약 표로 먼저 보여줘.
2. .agents/rules/design_guidelines.md 규칙에 따라 결측치 및 0원 오류 행을 정제하고, USD 매출은 1,380원 환율로 통일해 'revenue_krw_clean' 컬럼을 생성한 뒤 정제 전/후 비교 리포트를 출력해줘.
```

---

### 🔹 Step 5-2. 좌측 사이드바에 `4번째 탭([LG 5대 가전 실적·구독 분석])` 추가 및 차트 배치

> **💡 핵심 포인트**: 정제가 끝난 891행 클린 데이터를 바탕으로, 통합 대시보드(`app.py`) 좌측 사이드바에 **`[탭 4. LG 5대 가전 실적·구독 분석]`**을 추가하고 **상단 KPI 요약 카드 3개 + 권역별 매출 바 차트 + 가전 구독(`Subscription`) 비중 추이 차트**를 한 화면에 꽂아 넣습니다.

![Step 5-2 4번째 가전 실적 및 구독 분석 탭 추가 화면](assets/screenshots/slide_23_ui_1.png)

#### 👆 채팅창에 아래 프롬프트 복사·붙여넣기
```text
정제된 @04_AG_Analytics_lg_appliance_data.csv 데이터를 사용해 현재 통합 대시보드(app.py) 좌측 사이드바에 4번째 탭 '[4. LG 5대 가전 실적 & 구독 분석]'을 추가해줘.
- 상단: 5대 제품군(OLED evo, 워시타워, 디오스 냉장고, 휘센 HVAC, 스탠바이미) 필터 + 핵심 KPI 카드 3개(총 정제 매출액, 가전 구독 매출 비중 %, 평균 에너지 효율 등급)
- 중단 좌측: 글로벌 권역별(북미·유럽·한국·아시아) 제품군 매출 비교 인터랙티브 차트
- 중단 우측: 분기별 일반 판매 대비 가전 구독(Subscription) 매출 성장 추이 차트
- 하단: 이상 징후(반품률 급증 또는 구독 전환율 급등) 상위 5개 모델 요약 테이블
을 배치해줘.
```

---

### 🔹 Step 5-3. `/browser` 시각 셀프 힐링 & **독립 세션(`+ New Session`) 95점 품질 검증 게이트**

> **💡 실무 에이전트 활용의 핵심 하이라이트!**  
> 코드를 짠 에이전트에게 "잘 만들었니?"라고 물어보면 자기 코드를 칭찬합니다(**자기 확증 편향**).  
> 따라서 **① `/browser`로 화면 깨짐을 1차 보정**한 뒤, **② 우측 상단 `+ New Session`을 눌러 완전히 독립된 '품질 감사관 세션'을 열고 5대 루브릭 채점(`95점 미만 시 FAIL`)**을 통과시킵니다!

| ① `/browser` 실행: 내장 브라우저로 UI 깨짐 자동 감지·수정 | ② `+ New Session` 독립 검증 세션: `82점 FAIL` ➔ 수정 ➔ `97점 PASS` |
| :---: | :---: |
| ![Step 5-3 browser 시각 셀프 힐링 화면](assets/screenshots/slide_24_ui_1.png) | ![Step 5-3 독립 세션 95점 검증 게이트 화면](assets/screenshots/slide_24_ui_2.png) |

#### 👆 1단계: 현재 제작 세션(`Session A`)에서 `/browser`로 화면 레이아웃 자가 보정하기
```text
/browser 실행 중인 대시보드(http://localhost:8501)의 1번~4번 탭을 차례대로 열고 화면을 캡처해서, KPI 카드 텍스트 줄바꿈 깨짐이나 차트 범례 겹침이 있으면 디자인 가이드라인에 맞게 스스로 CSS/레이아웃 코드를 수정해줘.
```

#### 👆 2단계: 상단 `+ New Session` 클릭 후 **독립 검증 세션(`Session B`)**에 아래 95점 게이트 프롬프트 붙여넣기
```text
너는 지금부터 LG전자 대시보드 품질 감사관(QA Evaluator)이야. 제작 세션의 선입견 없이 현재 워크스페이스의 'app.py'와 '@04_AG_Analytics_lg_appliance_data.csv', '.agents/rules/design_guidelines.md'를 읽고 아래 5개 항목(각 20점, 총 100점 만점)으로 엄격하게 채점해줘:
1. 데이터 정합성 (20점): 결측치 23건 및 0원 오류 6건이 100% 제거되었는가?
2. 통화/단위 통일 (20점): USD 매출이 1,380원 환율로 정확히 KRW 환산되었는가?
3. 4개 탭 완결성 (20점): 좌측 사이드바 1~4번 탭이 누락 없이 모두 전환되는가?
4. 브랜드 & 가독성 (20점): LG 시그니처 레드(#A50034) 헤더와 #F3F4F6 카드 여백이 일관적인가?
5. 경영진 인사이트 (20점): 제품군별 구독 비중 변화와 구체적 액션 아이템이 수치로 제시되었는가?

총점이 95점 미만이면 무조건 [FAIL] 판정을 내리고, 제작 세션(Session A)에 그대로 복사해 전달할 수 있는 '코드 수정 지시서(Hand-off Patch Prompt)'를 출력해줘!
```
> **🔄 Hand-off 루프**: 검증 세션(`Session B`)이 출력해 준 `코드 수정 지시서`를 복사해 다시 제작 세션(`Session A`)에 붙여넣어 수정한 뒤, 재채점 시 **`97점 [PASS]`**가 뜨는 것을 확인합니다!

---

### 🔹 Step 5-4. `/plan` 자율 오케스트레이션으로 경영진 보고 요약본까지 원스톱 도출

![Step 5-4 plan 자율 오케스트레이션 실행 화면](assets/screenshots/slide_25_ui_1.png)

#### 👆 채팅창에 아래 프롬프트 복사·붙여넣기
```text
/plan 지금까지 검증 완료된 4개 탭 대시보드 데이터를 종합해서, 대시보드 최하단에 '[📥 본부장 보고용 Executive Summary 마크다운 내보내기]' 버튼을 추가하고 클릭 시 핵심 실적·시세·뉴스 요약 보고서가 다운로드되도록 마감해줘.
```

---

### 🏆 최종 완성 화면: 4개 사이드 탭을 갖춘 LG 마스터 인텔리전스 포털

3시간 동안 **크롬 GE Web(Part 1~2)**부터 **Antigravity 2.0(Part 3~5)**까지 단계별로 누적 빌드업하여 완성한 최종 4탭 통합 대시보드 화면입니다!

![최종 완성된 4개 탭 LG 마스터 인텔리전스 포털 화면](assets/screenshots/slide_26_ui_1.png)

> 💡 **전체 완성본 코드 즉시 실행하기**: 혹시 중간 단계를 건너뛰었거나 완성본 전체를 바로 띄워보고 싶다면, 터미널에서 아래 명령어 한 줄로 **[`05_Instructor_Solution_app.py`](./files/05_Instructor_Solution_app.py)** 를 실행하세요!
> ```bash
> streamlit run files/05_Instructor_Solution_app.py
> ```
