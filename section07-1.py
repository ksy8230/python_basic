# 파이썬 클래스 상세 이해
# Self, 클래스, 인스턴스 변수

# 선언
# class ClassName: (클래스 선언시 첫글자는 대문자로 표기)
#    함수
#    함수

# 예제 1
class UserInfo:
    # 속성, 메소드
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def user_info_p(self):
        print('Name: ', self.name)

# 클래스를 이용해 인스턴스화 시켜 사용한다
# uer1, user2는 독립적인 변수이며 서로 다르다


# 네임스페이스 : 객체를 인스턴스화 할 때 저장된 독립적인 공간
# 클래스 변수 : 직접 사용 가능, 객체보다 먼저 생성
# 인스턴스 변수 : 객체마다 별도로 존재, 인스턴스 생성 후 사용

# 인스턴스 만들기
user1 = UserInfo('Kim', 165)
user1.user_info_p()  # Name:  Kim
user2 = UserInfo('Park', 180)
user2.user_info_p()  # Name:  Park


print(id(user1))
print(id(user2))
print(user1.__dict__)  # {'name': 'Kim', 'height': 165}
print(user2.__dict__)  # {'name': 'Park', 'height': 180}

# 예제 2
# self의 이해


class SelfTest():
    def function1():  # self 인자 없어서 인스턴스에서 호출 불가능하고 클래스에서 직접 호출해야한다
        print('func1 called')

    def function2(self):  # self가 있으면 인스턴스 함수이다
        print(id(self))
        print('func2 called')


self_test = SelfTest()
# self_test.function1()
# -> SelfTest.function1()
self_test.function2()

print(id(self_test))

# 예제 3
# 클래스 변수, 인스턴스 변수


class WareHouse:
    # 클래스 변수
    stock_num = 0

    def __init__(self, name):
        # 인스턴스 변수
        self.name = name
        WareHouse.stock_num += 1

    def __del__(self):  # 인스턴스가 종료될 때 호출되는 함수
        WareHouse.stock_num -= 1


user1 = WareHouse('kim')
user2 = WareHouse('park')
user3 = WareHouse('lee')

print(user1.__dict__)  # {'name': 'kim'}
print(user2.__dict__)
print(user3.__dict__)

print('01.', WareHouse.__dict__)  # 01. 클래스 네임스페이스, 클래스 변수(공유)

print(user1.name)
print(user2.name)
print(user3.name)

print(user1.stock_num)  # 3: 자기 네임스페이스에 변수가 없으면 클래스로 가서 찾는다

del user1
print(user2.stock_num)
