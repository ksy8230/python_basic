# section10
# 파이썬 예외처리의 이해

# 예외 종류
# 문법적으로 에러가 없지만 코드실행에서 발생하는 예외처리
# lineter: 코드 스타일, 문법 체크

# SyntaxError : 잘못된 문법

# NameError : 참조변수 없음
a = 10
b = 15
# print(c)

# IndexError : 인덱스 범위 오버

# KeyError 
dic = {'name':'kim', 'age': 30}
# print(dic['hobby'])
print(dic.get('hobby'))

# AttributeError : 모듈, 클래스에 있는 잘못된 속성 사용시에 예외
import time
print(time.time())
# print(time.month())

# ValueError : 참조값이 없을 때 발생

# filenotFountError : 파일 없음

# f = open('test.txt', r)

# TypeError

x = [1,2]
y = (1,2)
z = 'test'

# print(x + y) 리스트와 튜플은 결합할 수 없다

# 항상 예외가 발생하지 않을 것으로 가정하고 먼저 코딩
# 그 후 런타임 예외 발생시 예외 처리 코딩 권장 (EAFP 코딩)

# 예외 처리 기본
# try : 에러가 발생할 가능성이 있는 코드 실행
# except: 에러명1
# except: 에러명2
# else: 에러가 발생하지 않았을 경우 실행
# finally : 항상 실행

# 예제 1
name = ['kim', 'lee', 'park']

try:
    z = 'kim'
    x = name.index(z)
    print(x)
    print('{} Fount it! in name'.format(z, x+1))
except ValueError: 
    print('Not Fount it!')
else :
    print('ok')

# 예제 2

try:
    z = 'aa'
    x = name.index(z)
    print(x)
    print('{} Fount it! in name'.format(z, x+1))
except: 
    print('Not Fount it! - error')
else :
    print('ok')
finally :
    print('anyway end')

# 예제4
# 예외처리는 하지 않지만 무조건 수행되는 코딩 패턴
try:
    print('try')
finally:
    print('end')

# 예제5
try:
    z = 'kim'
    x = name.index(z)
    print(x)
    print('{} Fount it! in name'.format(z, x+1))
except ValueError as l:
    print(l) 
    print('Not Fount it! - value')
except IndexError: 
    print('Not Fount it! -index')
except Exception: 
    print('Not Fount it! -occured')
else :
    print('ok')

# 예제6
# 예외 발생: raise
# raise 키워드로 예외 직업 발생

try:
    a = 'Kim'
    if a == 'Kim':
        print('ok 허가')
    else:
        raise ValueError
except ValueError:
    print('문제 발생')
except Exception as f:
    print('문제 발생', f)
else:
    print('ok')