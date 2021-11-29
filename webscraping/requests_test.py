import requests
res = requests.get("http://google.com")
# res = requests.get("http://nadocoding.tistory.com")

# if res.status_code == requests.codes.ok:
#     print("정상적으로 요청했습니다.")
# else:
#     print("요청에 문제가 생겼습니다.")

res.raise_for_status()  # requests를 통해서 문제가 있다면 바로 프로그램 종료
print(len(res.text))  # 요청한 페이지의 텍스트 총 글자수

# 요청 페이지의 text를 긁어와서 utf8로 인코딩 후 .html 파일로 만들기
with open("mygoogle.html", "w", encoding="utf8") as f:
    f.write(res.text)
