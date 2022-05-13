# 데이터 타입

import math
v_str1 = 'nice str'
v_bool = True
v_str2 = 'good str'
v_float = 10.3
v_int = 7
v_dict = {
    "name": "kim",
    "age": 25
}

v_list = [3, 5, 7]
v_tuple = 3, 5, 7
v_set = {7, 8, 9}

print(type(v_float))
print(type(v_set))
print(type(v_bool))
print(type(v_dict))
print(type(v_tuple))
print(type(v_int))
print(type(v_list))

i1 = 39
i2 = 939
big_int1 = 9999999
big_int2 = 7777777
f1 = 1.234
f2 = 3.784
f3 = .5
f4 = 10.

print(i1 * i2)
print(big_int1 / big_int2)
print(f1 ** f2)
print(f1 + f2)
print(f3 + i2)

result = f3 + i2
print(result, type(result))

# 형변환
# int, float, complex (복소수)
c = 10
# 10. 0
print(float(c))
print(complex(3))
# 1
print(int(True))
# 0
print(int(False))

print(type(int('3')))

print(complex(False))

# 단항 연산자
y = 100
y += 100
y *= 100
print(y)

# 수치 연산 함수
# https://docs.python.org/3/library/math.html

print(abs(-5))

# 몫과 나머지
n, m = divmod(100, 8)
print(n, m)


print(math.ceil(5.1))
print(math.floor(3.875))
