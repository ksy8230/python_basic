# 사용한 버전 : Python 3.8.3
# 실행 환경 : window CMD

import os
import random
import time


def makeRandomNumbers(maxNumber):  # 1~9까지 랜덤 숫자 maxNumber 자리 생성 함수
    pick_nums = set()
    while len(pick_nums) < maxNumber:
        pick_nums.add(str(random.randint(1, 9)))

    ran_num = ''.join(list(pick_nums))
    return ran_num


def checkInputNumbers(inputNumbers):  # 올바른 입력인지 판별 함수
    print("\n")
    if (inputNumbers == ""):
        print("입력값이 없습니다. 다시 입력해 주세요!")
        return 0
    if (inputNumbers.isdecimal() != True):
        print("숫자만 입력해 주세요")
        return 0
    if (len(inputNumbers) != 4):
        print("숫자 4자리만 입력해주세요. 다시 입력해 주세요!")
        return 0
    if (len(inputNumbers) != len(set(inputNumbers))):
        print("중복된 값이 있습니다. 다시 입력해 주세요!")
        return 0
    if (inputNumbers[0] == '0'):
        print("첫번째 숫자가 0입니다. 다시 입력해 주세요!")
        return 0
    else:
        return 1


def yesOrNo(message):  # 파라미터 값을 메세지로 질문하는 함수
    while True:
        reply = str(input(message + ' (y/n): ')).lower().strip()
        if reply[0] == 'y':
            return True
        if reply[0] == 'n':
            return False


def clearDisplay():  # 화면 정리 함수
    os.system(['clear', 'cls'][os.name == 'nt'])


def printTime(startTime, endTime):  # 초를 시분초로 변환하는 함수
    seconds = endTime - startTime
    result = time.strftime(
        "\n 경과한 시간 : %H 시간 %M 분 %S 초", time.gmtime(seconds))
    print(result)


MAX_NUM_COUNT = 4  # 최대 숫자 갯수
global numList
numList = makeRandomNumbers(MAX_NUM_COUNT)  # 컴퓨터 임의의 수 4자리


class BaseBallGame:

    try_count = 1  # 시도 횟수
    strike_count = 0  # 스트라이크 횟수
    ball_count = 0  # 볼 횟수
    out_count = 0  # 아웃 횟수
    records = []  # 게임 기록을 담은 배열
    STATE_LIST = [{'title': '게임 시작', 'value': 1},
                  {'title': '게임 종료', 'value': 0}]

    def IntroGame(self):  # 게임 인트로 메소드

        clearDisplay()  # 화면 정리
        for i in range(0, len(self.STATE_LIST)):
            print(str(self.STATE_LIST[i]['value']) +
                  ". "+self.STATE_LIST[i]['title'])

        cmd = int(input("번호 입력 >> "))
        if(cmd == self.STATE_LIST[0]['value']):
            self.playGame()
        else:
            self.exitGame()

    def continueGame(self, answer):  # 게임 계속 진행 여부 메소드

        if (self.strike_count != MAX_NUM_COUNT and yesOrNo("\n 재도전 하시겠습니까?") == 1):  # 스코어에 대한 기록 저장
            score_obj = {
                "s": self.strike_count,
                "b": self.ball_count,
                "o": self.out_count,
                "tryNumber": answer
            }
            self.records.append(score_obj)
            return 'yes'
        else:  # 스코어에 기록 저장하지 않고 0 리턴
            return 0

    def playGame(self):  # 게임 플레이 메소드

        startTime = time.time()
        while (self.strike_count < 4):
            clearDisplay()  # 화면 정리
            # print(numList)  # 디버깅용 정답 (실제 게임 시엔 주석)
            print("\n<<<<< SCORE >>>>>")
            for i in self.records:
                print(
                    f"{i['tryNumber']} -> s: {i['s']}, b: {i['b']}, o: {i['o']}")
            print("\n==================")
            print(f"{self.try_count}번째 도전입니다.")
            print("==================\n")
            answer = str(input("4자리 수를 입력해주세요. >> "))

            if (checkInputNumbers(answer) == 1):
                self.strike_count = 0
                self.ball_count = 0
                self.out_count = 0
                for i in range(0, 4):
                    for j in range(0, 4):
                        # 스트라이크 판정
                        if (str(answer[i]) == str(numList[j]) and i == j):
                            self.strike_count += 1
                        # 볼 판정
                        elif (str(answer[i]) == str(numList[j]) and i != j):
                            self.ball_count += 1
                    # 아웃 판정
                    self.out_count = MAX_NUM_COUNT - self.strike_count - self.ball_count
                # 시도 횟수 추가
                self.try_count += 1
                print("------------------------------")
                print(
                    f'{self.strike_count} 스트라이크 | {self.ball_count} 볼 | {self.out_count} 아웃')
                print("------------------------------\n")

                if(self.continueGame(answer) == 'yes'):
                    continue
                else:
                    break
            else:
                input("\n 계속 하려면 아무 키나 누르십시오...")
        if (self.strike_count == 4):  # 모두 스크라이크 시 경과 시간 출력
            endTime = time.time()
            print("정답!\n")
            printTime(startTime, endTime)
            input("\n 종료 하려면 아무 키나 누르십시오...")

        self.exitGame()

    def exitGame(self):  # 게임 종료 메소드
        exit()


game = BaseBallGame()
game.IntroGame()
