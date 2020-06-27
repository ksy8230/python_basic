# 몸풀기 코딩 실습

# import this
import sys

# 파이썬 기본 인코딩 // 파이썬은 입출력 인코딩이 utf-8이다
print(sys.stdin.encoding)
print(sys.stdout.encoding)

# 출력문
print('my name is good boy')

# 변수 선언
myvar = 'if Gooboy'

# 조건문
if myvar == "if Gooboy":
    print('ok')

# 반복문
for i in range(0, 10):
    for j in range(1, 10):
        print('%d * %d = ' % (i, j), i*j)

# 함수 선언


def greet():
    print('안녕하세요.')


greet()


# 클래스
class Cookie:
    pass


# 객체 생성
cookie = Cookie()

print(id(cookie))
print(dir(cookie))
