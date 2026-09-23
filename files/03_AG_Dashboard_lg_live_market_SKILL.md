---
name: lg-live-market
description: API 키 없이 15줄 파이썬 내장 모듈(urllib) 코드로 LG전자(066570) 실시간 주가, 글로벌 환율(USD/KRW), 최신 구글 뉴스를 수집해 대시보드 탭 2·3번에 바인딩하는 스킬
---

# `/lg-live-market` — 무인증 공개 API 기반 LG 실시간 시세·환율·뉴스 연동 스킬

## 1. 디렉토리 구조
```text
.agents/skills/lg-live-market/
├── SKILL.md
└── scripts/
    └── fetch_lg_live_market.py   # 15줄 무인증 파이썬 수집 스크립트 (API Key & pip 불필요)
```

## 2. 실행 절차 (Instructions)
1. 사용자가 `/lg-live-market` 스킬을 호출하면 `python3 .agents/skills/lg-live-market/scripts/fetch_lg_live_market.py`를 실행하여 실시간 JSON 데이터를 가져옵니다.
2. 수집된 JSON 결과(`close_price`, `fluctuation_rate`, `usd_krw`, `latest_news`)를 대시보드 포털의:
   - **[2번 사이드 탭: LG 실시간 주가·환율]**: LG전자(`066570`) 현재가, 전일대비 등락률, 실시간 원/달러(`USD/KRW`) 환율 카드로 렌더링합니다.
   - **[3번 사이드 탭: LG 최신 뉴스 피드]**: Google News RSS 상위 5건 제목·발행일·원문 링크 리스트로 렌더링합니다.
