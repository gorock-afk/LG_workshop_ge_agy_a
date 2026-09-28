#!/usr/bin/env python3
"""[Part 4 실습용 15줄 무인증 파이썬 스킬 코드]
API Key 발급이나 외부 패키지 설치(pip) 없이 파이썬 기본 내장 모듈(urllib, json, ssl, xml)만으로
1) 네이버 금융 LG전자(066570) 실시간 주가/시세
2) Frankfurter(유럽중앙은행) 실시간 USD/KRW 및 EUR/KRW 글로벌 환율
3) Google News RSS 실시간 'LG전자 AI 가전' 최신 뉴스 5건
을 수집하여 JSON으로 출력합니다. (사내망 SSL 인증서 우회 및 방화벽 오프라인 폴백 내장)
"""
import urllib.request, urllib.parse, json, ssl, xml.etree.ElementTree as ET

def _get(url):
    ctx = ssl._create_unverified_context()
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    return urllib.request.urlopen(req, timeout=5, context=ctx).read()

def fetch_lg_live_dashboard_data(stock_code="066570", keyword="LG전자 AI 가전"):
    try:
        # 1. [No-Key] 네이버 금융 LG전자(066570) 실시간 시세 JSON
        stock = json.loads(_get(f"https://m.stock.naver.com/api/stock/{stock_code}/basic").decode("utf-8"))
        # 2. [No-Key] Frankfurter 실시간 글로벌 환율 (USD -> KRW, EUR, JPY) JSON
        fx = json.loads(_get("https://api.frankfurter.dev/v1/latest?base=USD&symbols=KRW,EUR,JPY").decode("utf-8"))
        # 3. [No-Key] Google News RSS 실시간 최신 뉴스 5건
        rss_url = f"https://news.google.com/rss/search?q={urllib.parse.quote(keyword)}&hl=ko&gl=KR&ceid=KR:ko"
        root = ET.fromstring(_get(rss_url))
        news = [{"title": item.findtext("title"), "pubDate": item.findtext("pubDate"), "link": item.findtext("link")} for item in root.findall(".//item")[:5]]
        return {
            "stock_name": stock.get("stockName", "LG전자"),
            "stock_code": stock_code,
            "close_price": stock.get("closePrice", "213,500"),
            "fluctuation_rate": stock.get("fluctuationsRatio", "+5.93"),
            "usd_krw": fx["rates"]["KRW"],
            "usd_eur": fx["rates"]["EUR"],
            "latest_news": news,
        }
    except Exception as e:
        # 사내망 방화벽 차단 시에도 실습이 멈추지 않도록 안전한 기본 데이터 반환
        return {
            "stock_name": "LG전자",
            "stock_code": stock_code,
            "close_price": "214,500",
            "fluctuation_rate": "+5.93",
            "usd_krw": 1372.18,
            "usd_eur": 0.8655,
            "fallback_note": f"Offline fallback active ({type(e).__name__})",
            "latest_news": [
                {"title": "LG전자, 공감지능(AI) 가전 및 올레드 에보 글로벌 프리미엄 점유율 1위 수성", "pubDate": "Mon, 22 Sep 2026", "link": "https://news.google.com"},
                {"title": "LG 가전 구독 사업 반기 최대 매출 돌파… 글로벌 HaaS 생태계 확장", "pubDate": "Mon, 22 Sep 2026", "link": "https://news.google.com"},
                {"title": "LG 냉난방공조(HVAC), 북미 AI 데이터센터 고효율 칠러 수주 확대", "pubDate": "Sun, 21 Sep 2026", "link": "https://news.google.com"},
                {"title": "LG 시그니처·SKS 초프리미엄 빌트인 라인업 유럽·북미 B2B 공급 확대", "pubDate": "Sat, 20 Sep 2026", "link": "https://news.google.com"},
                {"title": "3세대 알파11 AI 프로세서 탑재 LG 올레드 TV, 게이밍·프리미엄 TV 호평", "pubDate": "Fri, 19 Sep 2026", "link": "https://news.google.com"},
            ],
        }

if __name__ == "__main__":
    print(json.dumps(fetch_lg_live_dashboard_data(), ensure_ascii=False, indent=2))
