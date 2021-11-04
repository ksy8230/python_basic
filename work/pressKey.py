import time
import os
import keyboard


def selectOne(value=1):
    os.system('cls')
    printOptions(value)
    while 1:
        if keyboard.is_pressed(72):
            value -= 1
            if value < 1:
                value = 3
            os.system('cls')
            printOptions(value)
            time.sleep(0.1)

        if keyboard.is_pressed(80):
            value += 1
            if value > 3:
                value = 1
            os.system('cls')
            printOptions(value)
            time.sleep(0.1)

        if keyboard.is_pressed('enter'):
            return value


def printOptions(selected):
    if selected == 1:
        printWithBg("1번 항목", "black", "bg_red")
    else:
        printWithBg("1번 항목", "white", "bg_black")

    if selected == 2:
        printWithBg("2번 항목", "black", "bg_white")
    else:
        printWithBg("2번 항목", "white", "bg_black")

    if selected == 3:
        printWithBg("3번 항목", "black", "bg_white")
    else:
        printWithBg("3번 항목", "white", "bg_black")

    changeColor('white')
    changeColor('bg_black')  # 커맨드 창을 다시 검은색으로 바꿈


def printWithBg(text, color, bgcolor):
    changeColor(color)
    changeColor(bgcolor)
    print(text)


def changeColor(code):
    colors = {
        'black': 30,
        'white': 37,
        'green': 32,
        'bg_black': 40,
        'bg_white': 47,
        'bg_red': 41
    }
    print('\033[' + str(colors[code]) + 'm', end='\r')
    print("\033[0;37;46m Black      \033[0m")


print('하나를 선택해 주세요!')
time.sleep(1)
result = selectOne()
print(str(result) + "을 선택하셨습니다!")
# time.sleep(1)
