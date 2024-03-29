# Section 11
# 파이썬 외부 파일 처리
# 파이썬 Excel, CSV 파일 읽기 및 쓰기

# CSV : MIME - text/csv

import csv

# 예제1
with open('./resource/sample1.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # 헤더줄 지나치기 (1행을 스킵)
    # 확인
    print(reader)
    print(type(reader))
    print(dir(reader))
    print()

    for c in reader:
        print(c)
        
# 예제2
with open('./resource/sample2.csv', 'r') as f:
    reader = csv.reader(f, delimiter='|') # delimiter : 어떤 구분으로 자를지
    next(reader) # 헤더줄 지나치기 (1행을 스킵)
    # 확인
    print(reader)
    print(type(reader))
    print(dir(reader))
    print()

    for c in reader:
        print(c)

print('---------')

# 예제3
with open('./resource/sample1.csv', 'r') as f:
    reader = csv.DictReader(f) 

    for c in reader:
        for k,v in c.items():
            print(k, v)
        print('----------------')

# 예제4
w = [[1,2,3],[4,5,6],[7,8,9],[11,12,13],[14,15,16],[17,18,19]]

with open('./resource/sample3.csv', 'w', newline='') as f:
    wt = csv.writer(f)

    for v in w:
        wt.writerow(v)