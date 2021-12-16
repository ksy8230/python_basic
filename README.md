## 파이썬 (인터프리터 언어 - 한줄씩 바로 실행하는 방식의 언어 = 동시통역)

### 파이썬을 이용한 웹 스크랩핑 연습

#### 웹 스크랩핑

- 많은 웹 사이트들을 체계적으로 돌아다니면서 URL, 키워드 등을 수집하는 개념

#### 웹 크롤링

- 특정 웹 사이트에서 데이터를 추출하는 개념

#### x-path

- html 문서에서 어떤 정보를 얻고자할 때 엘리먼트의 단계에 따라 엘리먼트1/엘리먼트2/엘리먼트3... 식으로 경로를 따는 것

#### User-Agent

- 요청 헤더에 사용자임을 알려주는 정보 넣어주기

#### beautifulsoup4

```
pip install beautifulsoup4 lxml
```

- html 문서값 넣어주고 lxml 파서를 통해서 Beatifulsoup 객체로 만들어주는 라이브러리

#### CSV

- 엑셀 파일에서 한글이 깨지는 경우 open 함수의 encoding 값을 "utf-8-sig"로 설정

```
f = open(filename, "w", encoding="utf-8-sig", newline="")
```

#### TODO

- [x] 크롤링한 데이터 REST API로 만들어서 웹에서 GET 요청해 보기
- [ ] 크롤링한 데이터 REST API로 만들어서 웹에서 버튼 클릭시 엑셀 파일 다운로드 해 보기
