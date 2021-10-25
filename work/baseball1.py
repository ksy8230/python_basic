import os
import random


# 1~9까지 랜덤 숫자 maxNumber 자리 생성 함수
def makeRandomNumbers(maxNumber):
    pick_nums = set()
    while len(pick_nums) < maxNumber:
        pick_nums.add(str(random.randint(1,9)))

    ran_num = ''.join(list(pick_nums))
    return ran_num

# 올바른 입력인지 판별 함수
def checkInputNumbers(inputNumbers) :
    print("\n")
    if (inputNumbers == "") :
        print("입력값이 없습니다. 다시 입력해 주세요!")
        return 0
    if (len(inputNumbers) != 4) :
        print(f"숫자 4자리만 입력해주세요. 다시 입력해 주세요!")
        return 0
    if (len(inputNumbers) != len(set(inputNumbers))) :
        print("중복된 값이 있습니다. 다시 입력해 주세요!")
        return 0
    if (inputNumbers[0] == '0') :
        print("첫번째 숫자가 0입니다. 다시 입력해 주세요!")
        return 0
    else :
        return 1

# 파라미터 값을 메세지로 질문하는 함수
def yesOrNo(message) :
    while True :
        reply = str(input(message + ' (y/n): ')).lower().strip()
        if reply[0] == 'y' :
            return True
        if reply[0] == 'n' :
            return False

# 화면 정리 함수
def clearDisplay():
    os.system( [ 'clear', 'cls' ][ os.name == 'nt' ] )

MAX_NUM_COUNT = 4 # 최대 숫자 갯수  
numList = makeRandomNumbers(MAX_NUM_COUNT) # 컴퓨터 임의의 수 4자리
# print('컴퓨터 임의의 수 4자리', numList)

try_count = 1 # 시도 횟수 
strike_count = 0 # 스트라이크 횟수
ball_count = 0 # 볼 횟수
out_count = 0 # 아웃 횟수
state = 1 # 게임 상태 on
records = [] # 게임 기록을 담은 배열


while (strike_count < 4 and state == 1):
    clearDisplay()    # 화면 정리
    print("\n<<<<< SCORE >>>>>")
    for i in records :
        print(f"{i['tryNumber']} -> s: {i['s']}, b: {i['b']}, o: {i['o']}")
    print("\n==================")
    print(f"{try_count}번째 도전입니다.")
    print("==================\n")
    answer = str(input("4자리 수를 입력해주세요. >> "))

    if (checkInputNumbers(answer) == 1) :
        strike_count = 0
        ball_count = 0
        out_count = 0
        for i in range(0, 4):
            for j in range(0, 4):
                # 스트라이크 판정
                if (str(answer[i]) == str(numList[j]) and i == j):
                    strike_count += 1
                # 볼 판정
                elif (str(answer[i]) == str(numList[j]) and i != j):
                    ball_count += 1
            # 아웃 판정
            out_count = MAX_NUM_COUNT - strike_count - ball_count
        
        print("------------------------------")
        print(f'{strike_count} 스트라이크 | {ball_count} 볼 | {out_count} 아웃')
        print("------------------------------\n")
        try_count += 1

        # 4자리 숫자 입력 후 분기 처리 (계속 진행 or 종료)
        if (strike_count != MAX_NUM_COUNT) :
            if (yesOrNo("재도전 하시겠습니까?") == 1) :
                # 스코어에 대한 기록 저장
                score_obj = {
                    "s" : strike_count,
                    "b" : ball_count,
                    "o" : out_count,
                    "tryNumber": answer
                }
                records.append(score_obj)
            else :
                break    
        
    else :
        print("\n")
        input("계속 하려면 아무 키나 누르십시오...")

state = 0
print("해답을 찾는데 걸린 시간 출력하고 종료")

# todo... 🚩
# 해답을 찾는데 걸린 시간 출력

