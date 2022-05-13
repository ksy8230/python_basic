# 파일 읽기, 쓰기
# 읽기 모드 : r, 쓰기 모드(기존 파일 삭제) : w, 추가 모드(파일 생성 또는 추가) : a
# .. : 상대 경로, . : 절대 경로
#
f = open('./resource/review.txt', 'r')
content = f.read()
print(content)

# 반드시 close 리소스 반환하기
f.close()

# 예제 2 : with문은 close를 자동으로 반환
with open('./resource/review.txt', 'r') as f:
    c = f.read()
    print(c)
    print(list(c))
    print(iter(c))


print('----------------------')

# 예제 3
with open('./resource/review.txt', 'r') as f:
    for c in f:
        print(c.strip())


print('----------------------')


# 예제 4
with open('./resource/review.txt', 'r') as f:
    content = f.read()
    print('>', content)
    content = f.read()  # 내용 없음
    print('>', content)

print('----------------------')

# 예제 5
with open('./resource/review.txt', 'r') as f:
    line = f.readline()
    print(line)
    while line:  # true, false
        print(line, end='### ')
        line = f.readline()

print('----------------------')
print('6----------------------')

# 예제 6
with open('./resource/review.txt', 'r') as f:
    contents = f.readlines() # list 호출
    print(contents)
    for c in contents:
        print(c, end=' *****')

print('----------------------')
print('7----------------------')

# 예제 7
with open('./resource/score.txt', 'r') as f:
    score = []
    for line in f:
        score.append(int(line))
    print(score)

print('average: {:6.3}'.format(sum(score)/len(score)) ) # 6자리고 소수 셋째자리까지 나와라

# 파일 쓰기
# 예제 1
with open('./resource/text1.txt', 'w') as f:
    f.write('niceman!\n')

with open('./resource/text1.txt', 'a') as f:
    f.write('niceman?\n')

# 예제 3
from random import randint
with open('./resource/text2.txt', 'w') as f:
    for cnt in range(6):
        f.write(str(randint(1, 100)))
        f.write('\n')

# 예제 4
with open('./resource/text3.txt', 'w') as f:
    lists = ['Kim\n', 'Park\n', 'Cho\n']
    f.writelines(lists)

# 예제 5
with open('./resource/text4.txt', 'w') as f:
    print('Test Contents', file=f) # 파일로 로그 기록할 때
