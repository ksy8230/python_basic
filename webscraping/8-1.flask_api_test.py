import requests, json
import re
import csv
from bs4 import BeautifulSoup

from flask import Flask, request, jsonify  # 서버 구현을 위한 Flask 객체 import
from flask_cors import CORS
from flask_restx import Api, Resource  # Api 구현을 위한 Api 객체 import
from collections import OrderedDict # object create

app = Flask(__name__)  # Flask 객체 선언, 파라미터로 어플리케이션 패키지의 이름을 넣어줌.
# api = Api(app)  # Flask 객체에 Api 객체 등록
CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/api/list', methods=['GET'])
def get():
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"}
    result_data = { "coupanLists": [], "gmarketLists": [] }    

    # 쿠팡 크롤링
    for i in range(1,6):
        url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&page={}".format(i)
        res = requests.get(url, headers=headers)
        res.raise_for_status()

        soup = BeautifulSoup(res.text, "lxml") # html 문서값 넣어주고 lxml 파서를 통해서 Beatifulsoup 객체로 만들기
        items = soup.find_all("li", attrs={"class":re.compile("^search-product")}) # li 태그에서 class이름이 search-product로 시작하는 모든 li 태그들
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
                data = OrderedDict()
                data["name"] = name
                data["price"] = price
                data["rate"] = rate
                data["url"] = "https://www.coupang.com/"+link

                result_data["coupanLists"].append(data)
    
    # 지마켓 크롤링
    for i in range(1, 3):
        url = "https://browse.gmarket.co.kr/search?keyword=%EB%85%B8%ED%8A%B8%EB%B6%81&k=32&p={}".format(i)
        res = requests.get(url, headers=headers)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, "lxml")
        items = soup.find_all("div", attrs={"class":re.compile("box__component-itemcard--general")})
        for item in items:
            name = item.find("span", attrs={"class": "text__item"})["title"]
            price = item.find("strong", attrs={"class": "text__value"}).get_text()
            rate = item.find("span", attrs={"class": "image__awards-points"})
            if(rate):
                rate = rate.find("span").get_text()[4:-5]
            link = item.find("a", attrs={"class": "link__item"})["href"]
            
            data = OrderedDict()
            data["name"] = name
            data["price"] = price
            data["rate"] = rate
            data["url"] = link

            result_data["gmarketLists"].append(data)

    return jsonify(result_data)

@app.route('/api/list/download', methods=['GET'])
def getCSV():
    url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page="

    title = "N,	종목명,	현재가,	전일비,	등락률,	액면가,	시가총액,상장주식수,외국인비율,	거래량,	PER,ROE"
    # 시가총액 데이터 크롤링
    csvStr = ""
    csvStr += title
    csvStr += "\n"
    for page in range(1, 5):
        res = requests.get(url + str(page))
        res.raise_for_status()
        soup = BeautifulSoup(res.text, "lxml")

        data_rows = soup.find("table", attrs={"class": "type_2"}).find("tbody").find_all("tr")
        for row in data_rows:
            columns = row.find_all("td")
            if len(columns) <= 1:
                continue
            data = [f'"{column.get_text().strip()}"' for column in columns]
            csvStr += ','.join(data)
            csvStr += "\n"
    
    return jsonify(csvStr)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)



        