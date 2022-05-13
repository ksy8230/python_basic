import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekdayList?week=mon"
res = requests.get(url)
res.raise_for_status()

# html 문서값 넣어주고 lxml 파서를 통해서 Beatifulsoup 객체로 만들기
soup = BeautifulSoup(res.text, "lxml")

# print(soup.title.get_text())
# print(soup.a)
# print(soup.a.attrs)
# print(soup.a["href"])

soup.find("a", attrs={"class": "Nbtn_upload"})  # 특정 a 태그 찾기
rank1 = soup.find("li", attrs={"class": "rank01"})
# print(rank1.a)
# print(rank1.a.get_text())
# rank2 = rank1.next_sibling.next_sibling
# print(rank2.a.get_text())
# rank3 = rank2.next_sibling.next_sibling
# print(rank3.a.get_text())

# rank2 = rank1.find_next_sibling("li")
# print(rank2.a.get_text())

lstRanks = rank1.find_next_siblings("li")  # li 형제 객체들 다 찾아오기

webtoonTopList = []
for i in lstRanks:
    obj = {
        "title": i.a.get_text(),
        "link": i.a["href"]
    }
    webtoonTopList.append(obj)

print(webtoonTopList)
