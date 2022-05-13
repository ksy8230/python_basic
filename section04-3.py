# 리스트, 튜플

# 리스트는 데이터타입이다.
# 리스트는 순서 중복 수정 삭제 o

# 선언
a = []
b = list()
c = [1, 2, 3, 4]
d = [10, 100, 1000, 'pen', 'banana']
e = [10, 100, 1000, ['pen', 'banana', 'apple', 'mellon']]

# 인덱싱
print(d[3])
print(d[-2])
print(d[0] + d[1])
print(e[3][1])
print(e[-1][-2])

# 슬라이싱
print(d[0:3])
print(e[3][1:3])

# 연산
print(c+d)
print(c * 3)
print(str(c[0]) + ' hi')

# 리스트 수정, 삭제
c[0] = 77
print(c)  # [77, 2, 3, 4]
c[1:3] = [100, 1000, 10000]
print(c)

c[1] = ['a', 'b', 'c']
print(c)

del c[1]
print(c)

# 리스트 함수
y = [5, 1, 3, 4, 2]
print(y)
y.append(6)
print(y)
y.sort()
print(y)  # [1, 2, 3, 4, 5, 6]
y.reverse()
print(y)  # [6, 5, 4, 3, 2, 1]
y.insert(2, 7)  # [6, 5, 7, 4, 3, 2, 1]
print(y)
y.remove(2)
print(y)

# del일 때는 인덱스를 지웠지만 remove는 해당 숫자를 지운다
a = y.pop()
print(a)
print(y)  # Last In, First Out ?

ex = [8, 99]
y.extend(ex)
print(y)  # [6, 5, 7, 4, 3, 8, 99]
# append는 그 자체가 들어가고, extend는 원소가 들어간다

# 삭제 : del, remove, pop
# 추가 : append, extend


# 튜플
# 순서, 중복 O
# 수정, 삭제 x

a = ()
b = (1,)
c = (1, 2, 3, 4)
d = (10, 100, ('a', 'b', 'c'))

print(c[2])
print(c[3])
print(d[2][1])

# d의 index 2부터 다 나와
print(d[2:])
print(d[2][0:2])
print(c + d)
print(c * 3)

# 튜플 함수
z = (5, 2, 1, 3, 7, 1)
print(z)
print(3 in z)
print(z.index(7))
print(z.count(1))
