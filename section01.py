# Section 01
# 파이썬 소개 및 작업 환경 설정

# 기본 출력
print("hello python!")

# task runner

# Separator 옵션 사용

print('T', 'E', 'S', 'T', sep='')
print('2019', '02', '19', '11', sep='-')

# end 옵션 사용
print('welcom To', end=' ')
print('the black paradaise', end=' ')
print('next line')
print('next line')

# format 사용 [], {}, () // You and Me and Me
print('{0} and {1} and {1}'.format('You', 'Me'))
print('{a} and {b}'.format(a='You', b='Me'))

# %s : 문자, %d : 정수, %f : 실수
print("%s's favorite number is %d" % ('Eunki', 7))

# 5자리 숫자의 정수가 온다 // 3자리의 숫자와 2자리의 소숫점
print("Test1: %5d, Price: %4.2f" % (12345, 1654.2345))
print("Test1: {0: 5d}, Price:{1: 4.2f}".format(12345, 1654.2345))
print("Test1: {a: 5d}, Price:{b: 4.2f}".format(a=12345, b=1654.2345))

# escape

print("'you'")
print('\'you\'')
print('\\you\'')
print('\\you\\n\n\n\n\n\n')
print('\t\t\ttest')
