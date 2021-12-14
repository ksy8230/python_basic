import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/bestChallenge/list?titleId=511287"
res = requests.get(url)
res.raise_for_status()

# html 문서값 넣어주고 lxml 파서를 통해서 Beatifulsoup 객체로 만들기
soup = BeautifulSoup(res.text, "lxml")

# 조건에 해당하는 모든 엘리먼트 찾기
# cartoons = soup.find_all("td", attrs={"class": "title"})
# title = cartoons[3].a.get_text()
# link = cartoons[3].a["href"]
# print(title)
# print("https://comic.naver.com"+link)

# for i in cartoons:
#     if(i.a) :
#         title = i.a.get_text()
#         link = "https://comic.naver.com" + i.a["href"]
#         print(title, link)

# 평점 정보 구하기
cartoons = soup.find_all("div", attrs={"class": "rating_type"})
total_rates = 0
for item in cartoons:
    if(item.strong) :
        rate = item.find("strong").get_text()
        print(rate)
        total_rates += float(rate)

print("전체 점수", total_rates)
print("평균 점수", total_rates/len(cartoons))
    
    