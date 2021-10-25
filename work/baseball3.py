# [PYTHON 3.X]
# -*- coding:utf-8 -*-
# 파일 인코딩은 "UTF-8"로 맞춰주시길 바랍니다.
# 사용 버전 : 파이썬 3.3

# import

import os
import random

# 유틸리티 클래스
class Util:
    # 화면 정리
    def clearDisplay():
        os.system( [ 'clear', 'cls' ][ os.name == 'nt' ] )

# 난수 생성 클래스
class Random:
    LIMIT_NUM_CNT = 4    # createNumberList 호출시 최대 반환 되는 숫자 갯수
    NumList = []

    def __init__(self, limit):
        self.LIMIT_NUM_CNT = limit

    def createNumberList(self):
        i = 0
        while True:
            num = self.createRandomNumber()
            if not self.isNumber(num):
                self.NumList.append(num)
                i = i + 1
            if i >= self.LIMIT_NUM_CNT : break
        return self.NumList

    def isNumber(self, chkNum):
        for i in range(len(self.NumList)):
            if int(self.NumList[i]) == chkNum :
                return True
        return False

    def createRandomNumber(self):
        return random.randrange(0,10)

# 야구게임 클래스
class BBGame:

    MODE_INIT = { 'title':'게임 초기화', 'value':0 }
    MODE_START = { 'title':'게임 시작', 'value':1 }
    MODE_EXIT = { 'title':'게임 종료', 'value':2 }

    MODE_LIST = [ MODE_INIT, MODE_START, MODE_EXIT ]

    STATE_WIN = True
    STATE_LOSE = False

    LIMIT_NUM_CNT = 4 # 맞춰야할 숫자 갯수
    LIMIT_CNT = 10    # 기회 제한 횟수

    # 초기화 메소드
    def __init__(self):
        self.mode = self.MODE_INIT['value']    # 게임 모드를 "초기화"

    # 비즈니스 로직 시작 메소드
    def start(self):
        Util.clearDisplay()    # 화면 정리
        if self.mode == self.MODE_INIT['value']: self.startInit()
        elif self.mode == self.MODE_START['value']: self.startGame()
        elif self.mode == self.MODE_EXIT['value']: self.exitGame()
        
        return self.state

    # 게임 초기화 메소드
    def startInit(self):
        self.state = self.STATE_LOSE    # 상태는 "패배" 로 초기화.

        # 메뉴명 출력
        for i in range(1,len(self.MODE_LIST)):
            print(str(self.MODE_LIST[i]['value'])+". "+self.MODE_LIST[i]['title'])

        # 메뉴 선택
        try:
            cmd = int(input("번호 입력>> "))
            self.mode = cmd
            self.start()
        except:
            print("해당 번호가 없거나 입력이 잘못 되었습니다.")
            input("아무 키나 누르세요.")
            self.mode = self.MODE_INIT['value']
            self.start()
    
    # 게임 플레이 메소드
    def startGame(self):
        print("난수 생성중입니다..")
        randomCls = Random(self.LIMIT_NUM_CNT)
        numList = randomCls.createNumberList()
        print("게임을 시작합니다..")
        print("숫자 입력방법) 1 2 4 6 ")
        print("게임에서 나가고 싶으면 999 를 입력하세요. 대신 게임은 패배합니다.")

        strike = 0
        ball = 0
        out = 0

        for i in range(0, self.LIMIT_CNT):
            remainPoint = int(self.LIMIT_CNT) - int(i)
            print("남은 기회 : "+str(remainPoint))
            inputList = input("숫자 입력>> ")

            chkList = inputList.split()

            # 게임 종료
            if int(chkList[0]) == 999 and len(chkList) == 1 : 
                self.state = self.STATE_LOSE
                self.mode = self.MODE_EXIT['value']
                break
            
            if len(chkList) == self.LIMIT_NUM_CNT :

                strike = 0
                ball = 0
                out = 0

                # 스트라이크 판정
                for j in range(0, self.LIMIT_NUM_CNT):
                    if int(chkList[j]) == int(numList[j]) : 
                        strike = strike + 1
                
                # 볼 판정
                for j in range(0, self.LIMIT_NUM_CNT):
                    if chkList.count(str(numList[j])) > 0 and int(chkList[j]) != int(numList[j]):
                        ball = ball + 1

                # 아웃 판정
                out = self.LIMIT_NUM_CNT - strike - ball

                print( str(strike)+"Strike "+str(ball)+"Ball"+str(out)+"Out" )

                # 모두 스트라이크면 게임 승리
                if int(strike) == self.LIMIT_NUM_CNT :
                    self.state = self.STATE_WIN
                    self.mode = self.MODE_EXIT['value']
                    break
            else:
                print("입력이 잘못 되었습니다.")

            if int(remainPoint) == 1 :
                self.mode = self.MODE_EXIT['value']
                break

        self.start()

    # 게임 종료 메소드
    def exitGame(self):
        print("게임이 종료되었습니다.")

# main logic

game = BBGame()
result = game.start()
if result : print("당신이 이겼습니다.")
else: print("당신이 졌습니다.")