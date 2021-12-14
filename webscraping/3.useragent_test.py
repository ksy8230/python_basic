import requests
url = "http://nadocoding.tistory.com"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"}

res = requests.get(url, headers=headers)
res.raise_for_status()  # requests를 통해서 문제가 있다면 바로 프로그램 종료

# 요청 페이지의 text를 긁어와서 utf8로 인코딩 후 .html 파일로 만들기
with open("testUserAgent.html", "w", encoding="utf8") as f:
    f.write(res.text)
