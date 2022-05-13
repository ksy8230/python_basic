# 파이썬 데이터 타입 (자료형)
# 딕셔너리, 집합 자료형

# 딕셔녀리(Dictionary) : 순서 x, 중복 x, 수정 o, 삭제 o
# Key와 Value를 가지고 있는 json 형식과 비슷하다

# 선언
a = {'name': 'kim', 'Phone': '010-111-111', 'birth': 911213}
c = {'arr': [1, 2, 3, 4, 5]}
print(a)

print(a['name'])
print(a.get('name'))
# 없는 경우 none이 출력되어서 안전하다
print(a.get('address'))
print(c['arr'][1:3])

# 딕셔너리 추가
a['adress'] = 'Seoul'
print(a)
a['rank'] = [1, 3, 4]
a['rank2'] = (1, 2, 3,)
print(a)

# keys, values, items
print(a.keys())
# list로 형변환해야 리스트에서 가능했던 배열 기능이 된다
print(list(a.keys()))

temp = list(a.keys())
print(temp[1:3])

print(a.values())
print(list(a.values()))

print(a.items())
# dict_items([('name', 'kim'), ('Phone', '010-111-111'), ('birth', 911213), ('adress', 'Seoul'), ('rank', [1, 3, 4]), ('rank2', (1, 2, 3))])
print(list(a.items()))
# [('name', 'kim'), ('Phone', '010-111-111'), ('birth', 911213), ('adress', 'Seoul'), ('rank', [1, 3, 4]), ('rank2', (1, 2, 3))]

# 집합 (Sets) (순서 x, 중복x)
a = set()
b = set([1, 2, 3, 4])
c = set([1, 4, 5, 6, 6])

print(type(a))  # <class 'set'>
print(c)  # {1, 4, 5, 6}

# set은 주로 변환을 해서 사용한다
t = tuple(b)
print(b)  # {1, 2, 3, 4}
l = tuple(b)
print(l)  # (1, 2, 3, 4)

s1 = set([1, 2, 3, 4, 5])
s2 = set([4, 5, 6, 7, 8])
print(s1.intersection(s2))  # {4, 5}
print(s1 & s2)

print(s1 | s2)  # {1, 2, 3, 4, 5, 6, 7, 8}
print(s1.union(s2))

print(s1 - s2)  # {1, 2, 3}
print(s1.difference(s2))

# 추가 & 제거
s3 = set([7, 8, 10, 15])
s3.add(18)
s3.add(7)
print(s3)  # {7, 8, 10, 15, 18}
