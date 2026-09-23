#!/usr/bin/env python3
"""[Part 4 실습용 15줄 무인증 파이썬 스킬 코드]
API Key 발급이나 외부 패키지 설치(pip) 없이 파이썬 기본 내장 모듈(urllib, json, xml)만으로
1) 네이버 금융 LG전자(066570) 실시간 주가/시세
2) Frankfurter(유럽중앙은행) 실시간 USD/KRW 및 EUR/KRW 글로벌 환율
3) Google News RSS 실시간 'LG전자 AI 가전' 최신 뉴스 5건
을 수집하여 JSON으로 출력합니다.
"""
import urllib.request, urllib.parse, json, xml.etree.ElementTree as ET

def fetch_lg_live_dashboard_data(stock_code="066570", keyword="LG전자 AI 가전"):
    headers = {"User-Agent": "Mozilla/5.0"}
    # 1. [No-Key] 네이버 금융 LG전자(066570) 실시간 시세 JSON
    req = urllib.request.Request(f"https://m.stock.naver.com/api/stock/{stock_code}/basic", headers=headers)
    stock = json.loads(urllib.request.urlopen(req, timeout=5).read().decode("utf-8"))
    # 2. [No-Key] Frankfurter 실시간 글로벌 환율 (USD -> KRW, EUR, JPY) JSON
    fx = json.loads(urllib.request.urlopen("https://api.frankfurter.dev/v1/latest?base=USD&symbols=KRW,EUR,JPY", timeout=5).read().decode("utf-8"))
    # 3. [No-Key] Google News RSS 실시간 최신 뉴스 5건
    rss_url = f"https://news.google.com/rss/search?q={urllib.parse.quote(keyword)}&hl=ko&gl=KR&ceid=KR:ko"
    root = ET.fromstring(urllib.request.urlopen(rss_url, timeout=5).read())
    news = [{"title": item.findtext("title"), "pubDate": item.findtext("pubDate"), "link": item.findtext("link")} for item in root.findall(".//item")[:5]]
    return {
        "stock_name": stock.get("stockName", "LG전자"),
        "stock_code": stock_code,
        "close_price": stock.get("closePrice"),
        "fluctuation_rate": stock.get("fluctuationsRatio"),
        "usd_krw": fx["rates"]["KRW"],
        "usd_eur": fx["rates"]["EUR"],
        "latest_news": news,
    }

if __name__ == "__main__":
    print(json.dumps(fetch_lg_live_dashboard_data(), ensure_ascii=False, indent=2))
