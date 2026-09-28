---
name: python-api-trend
description: API 키 없이 15줄 파이썬 내장 모듈(urllib) 코드로 LG전자(066570) 실시간 주가, 글로벌 환율(USD/KRW), 최신 구글 뉴스를 수집해 대시보드 실시간 시장·뉴스(LIVE) 탭에 바인딩하는 스킬
---

# `/python-api-trend` — 무인증 공개 API 기반 LG 실시간 시세·환율·뉴스 연동 스킬

## 1. 디렉토리 구조
```text
.agents/skills/python-api-trend/
├── SKILL.md
└── scripts/
    └── fetch_lg_live_market.py   # 15줄 무인증 파이썬 수집 스크립트 (API Key & pip 불필요)
```

## 2. 실행 절차 (Instructions)
1. 사용자가 `/python-api-trend` 스킬을 호출하면 `python3 03_AG_Dashboard_fetch_lg_live_market.py` (또는 `.agents/skills/python-api-trend/scripts/fetch_lg_live_market.py`)를 실행하여 실시간 JSON 데이터를 가져옵니다.
2. 수집된 JSON 결과(`close_price`, `fluctuation_rate`, `usd_krw`, `latest_news`)를 `index.html` 내부 데이터에 인라인 바인딩하여(더블클릭 `file://` 실행 시에도 CORS 에러 없이 즉시 표시되도록 보장):
   - **[사이드바 2번 탭: 실시간 시장·뉴스(LIVE)]**: LG전자(`066570`) 현재가, 전일대비 등락률, 실시간 원/달러(`USD/KRW`)·유로(`EUR/KRW`) 환율 카드 및 Google News RSS 상위 5건(클릭 시 원문 이동) 리스트로 렌더링합니다.
