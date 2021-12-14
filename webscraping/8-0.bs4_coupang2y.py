import requests
import re
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"
}

for i in range(1,6):
    url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&page={}".format(i)
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    # html 문서값 넣어주고 lxml 파서를 통해서 Beatifulsoup 객체로 만들기
    soup = BeautifulSoup(res.text, "lxml")

    # li 태그에서 class이름이 search-product로 시작하는 모든 li 태그들
    items = soup.find_all("li", attrs={"class":re.compile("^search-product")})

    for item in items:

        ad_tag = item.find("span", attrs={"class": "ad-badge"})
        name = item.find("div", attrs={"class":"name"}).get_text()
        price = item.find("strong", attrs={"class":"price-value"}).get_text()
        rate = item.find("em", attrs={"class":"rating"})
        if(rate) :
            rate = rate.get_text()
        else :
            # print("<<평점 없는>> 상품 제외")
            continue

        # 광고 제품은 제외
        if ad_tag:
            # print("<<광고>> 상품 제외")
            continue

        # apple 제품 제외
        if "Apple" in name :
            # print("<<애플>> 제품 제외")
            continue

        link = item.find("a", attrs={"class": "search-product-link"})["href"]

        # 별점 4.5 이상
        if float(rate) >= 4.5 :
            print(f"name: {name}")
            print(f"price: {price}")
            print(f"rate: {rate}")
            print("{}".format("https://www.coupang.com/"+link))
            print("-"*100)

        