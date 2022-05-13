# 파이썬 흐름제어 - 제어문

print(type(True))
print(type(False))

# 예 1
if True:
    print("Yes")

# 예 2
if False:
    print("No")

# 예 3
if False:
    print("No")
else:
    print("Yes2")

# 관계연산자
# >, >=, <, <=, ==, !=

a = 10
b = 0
print(a == b)
print(a != b)

# 참 거짓의 종류 (True, False)
# 참 : "내용", [내용], (내용), {내용}, 1
# 거짓 : "", [], (), {}, 0

city = ""

if city:
    print('>>>True')
else:
    print(">>>False")

# 논리 연산자
# and or not

a = 100
b = 60
c = 15

print('and : ', a > b and b > c)  # a는 b보다 크고 b는 c보다 크면
print('or : ', a > b or b > c)  # a는 b보다 크거나 b는 c보다 크면
print('not : ', not a > b)  # a는 b보다 크지 않으면

# 산술 > 관계 > 논리 순서로 적용
print('ex1: ', 5 + 10 > 0 and not 7 + 3 == 10)  # False

score1 = 90
score2 = 'A'

if score1 >= 90 and score2 == 'A':
    print("합격하셨습니다")
else:
    print("죄송합니다. 불합격입니다")

# 다중 조건문
num = 90

if num >= 90:
    print("num 등급 A", num)
elif num >= 80:
    print("num 등급 B", num)
elif num >= 70:
    print("num 등급 C", num)
else:
    print("꽝")

# 중첩조건문

age = 27
height = 175

if age >= 20:
    if height >= 170:
        print("a지망 지원 가능")
    elif height >= 160:
        print("b지망 지원 가능")
    else:
        print("지원 불가")
else:
    print("20세 이상 지원 가능")
