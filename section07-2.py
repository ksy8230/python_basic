# 파이썬 클래스
# 상속, 다중 상속

# 예제 1
# 상속 기본
# 슈퍼 클래스(부모) 및 서브 클래스(자식) -> 모든 속성, 메소드 사용 가능

class Car:
    """Parent Class"""

    def __init__(self, tp, color):
        self.type = tp
        self.color = color

    def show(self):
        return 'Car Class "Show Method"'


class BmwCar(Car):
    """Sub Class"""

    def __init__(self, car_name, tp, color):
        super().__init__(tp, color)
        self.car_name = car_name

    def show_model(self) -> None:
        return "Your Car Name : %s" % self.car_name


class BenzCar(Car):
    """Sub Class"""

    def __init__(self, car_name, tp, color):
        super().__init__(tp, color)
        self.car_name = car_name

    def show_model(self) -> None:
        return "Your Car Name : %s" % self.car_name

    def show(self):
        print(super().show())
        return 'Car Info: %s %s %s' % (self.car_name, self.type, self.color)


# 일반 사용
model1 = BmwCar('520d', 'sedan', 'red')

print(model1.color)  # Super
print(model1.type)  # Super
print(model1.car_name)  # Sub

print(model1.show())  # Super
print(model1.show_model())
print(model1.show_model())
print(model1.__dict__)

# Method Overriding (오버라이딩)
model2 = BenzCar('220d', 'suv', 'black')
print(model2.show())  # Super Class에 있는 메서드를 자식에서 오버라이딩

# Parent Method Call
model3 = BenzCar('350s', 'sedan', 'silver')
print(model3.show())

# Inheritance Info
# 상속 정보를 리스트 타입으로 반환
# [<class '__main__.BmwCar'>, <class '__main__.Car'>, <class 'object'>]
print(BmwCar.mro())


# 예제 2
# 다중 상속
class X():
    pass


class Y():
    pass


class Z():
    pass


class A(X, Y):
    pass


class B(Y, Z):
    pass


class M(B, A, Z):
    pass


print(M.mro())  # 복잡한 다중 상속은 코드가 읽히지 않는다
print(A.mro())
