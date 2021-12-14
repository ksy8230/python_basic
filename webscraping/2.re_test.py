# 주민등록번호
# 911213-1234567

# 이메일 주소
# naver@naver.com
# naver2@naver.com

# 차량 번호
# 11가 1234

# ip 주소
# 192.204.0.1
# 1000.2000.3000.4000

import re

p = re.compile("ca.e")
# . (ca.e) : 하나의 문자를 의미 -> care, cafe, case ...
# ^ (^de) : 문자열의 시작 -> desk, destination ...
# $ (se$) : 문자열의 끝 -> case, base ...


def print_match(m):
    if m:
        print("m.group() : ", m.group())  # 매치된 문자열을 한꺼번에 반환, 매치되지 않으면 에러가 발생
        print("m.string : ", m.string)  # 입력 받은 문자열
        print("m.start() : ", m.start())  # 일치하는 문자열의 시작 index
        print("m.end() : ", m.end())  # 일치하는 문자열의 끝 index

        print("m.span() : ", m.span())  # 일치하는 문자열의 시작 / 끝 index
    else:
        print("매칭되지 않았습니다.")


# m = p.match("caseless")  # 주어진 문자열의 처음부터 일치하는지 확인
# print_match(m)

# m = p.search("good care")  # 주어진 문자열 중에 일치하는게 있는지 확인
# print_match(m)

lst = p.findall("good care cafe")  # 일치하는 모든 것을 리스트 형태로 반환
print(lst)
