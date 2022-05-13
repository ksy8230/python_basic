import copy


def seq_search(seq, key):  # 선형 검색 함수
    a = copy.deepcopy(seq)
    a.append(key)  # 보초법을 사용하여 찾고자 하는 key를 리스트 끝에 배치 후 검색 실패 시 -1 리턴

    i = 0

    while True:
        if a[i] == key:
            break
        i += 1
    return -1 if i == len(seq) else i


def bin_search(seq, key):  # 이진 검색 함수
    start_idx = 0
    last_idx = len(seq) - 1

    while True:
        center_idx = (start_idx + last_idx) // 2
        if seq[center_idx] == key:
            return center_idx
        elif seq[center_idx] < key:
            start_idx = center_idx + 1
        else:
            last_idx = center_idx - 1
        if start_idx > last_idx:
            break
    return -1


num = int(10000)
x = [None] * num

for i in range(num):
    x[i] = int(i)

input_key = int(input('검색할 값을 입력하세요 : '))

# idx = seq_search(x, input_key)
idx = bin_search(x, input_key)

if idx == -1:
    print('검색값을 갖는 원소가 존재하지 않습니다')
else:
    print(f'검색값은 x[{idx}]에 있습니다')
