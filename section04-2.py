# 문자열 관련 연산자

# 문자열 길이
str1 = "i am a girl"
str2 = ''
str3 = str()
print(len(str1))
print(len(str2))
print(len(str3))

# escape
escape_str1 = 'Do you have a \"big collection\"'
escape_str2 = 'Tab\t Tab\t'
print(escape_str1)
print(escape_str2)

# Raw String r 뒤에 있는 문자는 escape가 적용되지 않는다
raw_s1 = r'C:\Programs\Test\Bing'
print(raw_s1)

raw_s2 = r"\\a\\a"
print(raw_s2)

# 멀티라인
multi = \
    """
문자열 
멀티라인 
테스트
"""
print(multi)

# 문자열 연산
str_o1 = "*"
str_o2 = "abc "
str_o3 = "def"
str_o4 = "niceman"

print(str_o1 * 100)
print(str_o2 + str_o3)
# error : 형이 달라서 print(str_o1 + 3)
print('a' in str_o4)
# a가 포함되어 있니 => true
print('f' in str_o4)
print('f' not in str_o4)

# 문자열 형 변환
print(str(66) + 'a')

# 문자열 함수

a = 'Niceman'

print(a.islower())  # false
print(a.endswith('n'))  # true
print(a.capitalize())  # NICEMAN
print(a.replace('Nice', 'good'))
print(list(reversed(a)))  # ['n', 'a', 'm', 'e', 'c', 'i', 'N']

b = 'OrangeIsGood'

print(b[0:3])  # 3 전까지 나와서 Ora
print(b[0:len(a)])  # 처음부터 끝까지
print(b[:])  # 처음부터 끝까지
print(b[0:10:2])  # 세번째 숫자를 넣으면 그 숫자만큼 스킵 단위로 지정해(제외시켜서) 해당 패턴 유지하며 10 전까지 출력을 한다
print(b[1:-2])  # 1부터 시작해서 끝에서 -1, -2 전까지 출력해서 rangeIsGo
print(b[::-1])  # 처음부터 끝까지인데 스킵 단위는 -1이라 dooGsIegnarO
