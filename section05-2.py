# 파이썬 흐름제어 - 반복문

# 기본 반복문 : for, while


v1 = 1
while v1 < 11:
    print("v1 is :", v1)
    v1 += 1

for v2 in range(10):
    print('v2 is :', v2)

# 1 - 100 합
sum1 = 0
cnt1 = 1
while cnt1 <= 100:
    sum1 += cnt1
    cnt1 += 1

print('1 ~ 100', sum1)
print('1 ~ 100', sum(range(1, 101)))
print('1 ~ 100 짝수의 합', sum(range(1, 101, 2)))  # 1 부터 100까지 2개 단위로 건너뛰면서 더하기


# 시퀀스 (순서가 있는) 자료형 반복
# 문자열, 리스트, 튜플, 집합, 사전
# iterable : range, reversed, enumerate, filter, map, zip

names = ["kim", "park", "lee", "choi", "yoo"]

for name in names:
    print('you are', name)

word = "dreams"

for s in word:
    print("word", s)

my_info = {
    "name": "kim",
    "age": 33,
    "city": "seoul"
}

for key in my_info:
    print("my_info", key)

for key in my_info.keys():
    print("my_info", key)

for key in my_info.values():
    print("my_info", key)

for key, value in my_info.items():
    print("key:", key, 'value:', value)

name = "KennRY"

for n in name:
    if n.isupper():
        print(n.lower())
    else:
        print(n.upper())


# break
numbers = [14, 2, 556, 23, 33, 55, 34, 100, 12, 355]

for num in numbers:
    if num == 33:
        print('found', num)
        break
    else:
        print('not fount...')

# for - else 구문 (반복문이 정상적으로 수행 된 경우 else 블럭 수행)
for num in numbers:
    if num == 33:
        print('found', num)
    else:
        print('not fount...')
else:
    print("Not fount 33....")

# continue
li = ["1", 2, 5, True, 4.3, complex(4)]
for v in li:
    if type(v) is float:
        continue
    print("타입:", type(v))
