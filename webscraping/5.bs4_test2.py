import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()

# html 문서값 넣어주고 lxml 파서를 통해서 Beatifulsoup 객체로 만들기
soup = BeautifulSoup(res.text, "lxml")

# 조건에 해당하는 모든 엘리먼트 찾기
cartoons = soup.find_all("a", attrs= {"class": "title"}) 
# 네이버 웹툰 전체 목록 가져오기
for cartoon in cartoons: 
    print(cartoon.get_text())