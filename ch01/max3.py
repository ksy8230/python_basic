print('세 정수 최댓값 구하기')

a = int(input('정수 a값을 입력 : '))
b = int(input('정수 b값을 입력 : '))
c = int(input('정수 c값을 입력 : '))

maximum = a
if b > maximum:
    maximum = b
if c > maximum:
    maximum = c

print(f'최댓값은 {maximum}')
