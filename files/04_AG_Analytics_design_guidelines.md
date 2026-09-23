---
trigger: always_on
description: LG전자 통합 업무 포털(4개 사이드 탭) 브랜드 스타일 및 가전 데이터 정제 필수 규칙
---

# LG Electronics Work Portal & Appliance Analytics Design Guidelines

## 1. 브랜드 컬러 팔레트 (LG Clean Minimalist Theme)
- **메인 캔버스 배경**: `#FFFFFF` (순백색)
- **사이드바 네비게이션**: `#111827` (다크 네이비 차콜)
- **카드 서피스**: `#F9FAFB` (연회색) + `1px solid #E5E7EB` 테두리
- **LG 시그니처 포인트 컬러**: **`#A50034`** (활성화된 사이드 탭 배지, 주요 KPI 상단 보더, 품질 경고 배지)
- **상태 표시 컬러**: 정상 `#0D652D` (그린), ThinQ 만족도 80점 미만 경고 `#A50034` (레드 배지)

## 2. 4개 사이드 탭 통합 아키텍처 (기존 탭 덮어쓰기 금지)
반드시 기존 1~3번 탭을 그대로 보존한 상태에서 4번째 탭을 추가해야 합니다:
1. **[탭 1] LG AI 가전·OLED 트렌드 웹**: Part 3에서 제작한 5장 발표용 웹 슬라이드(`hello_world_slides.html`) 임베딩
2. **[탭 2] LG전자(066570) 실시간 시세·환율**: `/lg-live-market` 15줄 무인증 파이썬 스킬로 수집한 현재가·등락률 및 `USD/KRW`, `EUR/KRW` 실시간 환율 카드
3. **[탭 3] Google News RSS 실시간 뉴스**: `/lg-live-market` 스킬이 수집한 LG전자 AI 가전·OLED 최신 뉴스 5건 피드
4. **[탭 4] LG 가전 제품군 실적·구독 Analytics**: `04_AG_Analytics_lg_appliance_data.csv` (920행) 기반 5대 기기군(`OLED evo`, `WashTower`, `DIOS`, `Whisen & HVAC`, `StanbyME`) 매출·구독 결합률 차트 및 권역별(`북미`, `유럽`, `한국`, `인도·아시아`) 필터

## 3. LG 가전 데이터 정제 및 예외 방어 규칙 (엄격 준수)
1. **ThinQ 스마트진단 만족도 결측치(NaN) 보간**:
   - `thinq_satisfaction_score` 컬럼의 빈 값(결측치 23건)은 0점으로 처리하지 말고, **해당 제품군(`product_line`)의 중앙값(Median)**으로 안전하게 보간한다.
2. **스탠바이미 시제품(`revenue_krw = 0`) 0 나눗셈 방어**:
   - `StanbyME & Care (신가전·시제품)` 행 중 필드테스트 물량(`revenue_krw == 0`, 18건)은 영업이익률(`(revenue_krw - cost_krw) / revenue_krw`) 계산 시 **`ZeroDivisionError`가 발생하지 않도록 분모에서 제외**하고, 별도 `'R&D 시제품 테스트(18건)'` 요약 카드로 분리 표기한다.
3. **품질 집중 점검 배지**:
   - `thinq_satisfaction_score < 80.0`인 행과 제품군은 테이블 및 차트에서 **`[집중점검 <80점]` (`#A50034`)** 경고 배지를 표시한다.
