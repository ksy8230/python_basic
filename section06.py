# Section 06
# 파이썬 람수식 및 람다 (lambda)

# 함수 정의 방법
# def 함수명(parameter)
#   code

# 함수 호출
# 함수명(parameter)

# 함수 선언 위치 중요

# 예제 1 : 리턴 값이 없는 함수
def hello(value):
    print('hello def', value)


hello("python!")

# 예제 2 : 문자열을 리턴하는 함수


def hello_return(value):
    val = 'hello def' + str(value)
    return val


str = hello_return("Python!")
print(str)

# 예제 3 : 다중 리턴


def function_mul(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return y1, y2, y3


val1, val2, val3 = function_mul(100)
print(val1, val2, val3)

# 예제 3 : 다중 리턴 (데이터 타입 반환)


def function_mul2(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return [y1, y2, y3]


lt = function_mul2(100)
print(lt)

# 예제 4
# *args, **kwarge : 매개변수가 몇 개가 넘어가는지 모를 때

# args


def args_function(*args):
    # for t in args:
    #    print(t)
    for i, v in enumerate(args):
        print(i, v)


args_function('kim', 'park')

# kwarge: 매개변수를 딕셔너리로 넘길 수 있다


def kwarg_function(**kwargs):
    for k, v in kwargs.items():
        print(k, v)


kwarg_function(name1='kim', name2='park')

# 전체 혼합


def example_mul(arg1, arg2, *args, **kwargs):
    print(arg1, arg2, args, kwargs)


example_mul(10, 20)  # 10 20 () {}
example_mul(10, 20, 'kim', 'park')  # 10 20 ('kim', 'park') {}
example_mul(10, 20, 'kim', 'park',
            name='kim',
            name2='park')  # 10 20 ('kim', 'park') {'name': 'kim', 'name2': 'park'}

# 중첩 함수(클로저)


def nested_function(num):
    def func_in_func(num):
        print('>>>', num)
    print('in func')
    func_in_func(num + 1000)


nested_function(10000)

# 예제 6 : hint


def function_mul3(x: int) -> list:
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return [y1, y2, y3]


print(function_mul3(5.0))

# 람다식 예제
# 람다식 : 메모리 절약, 가독성 향상, 코드 간결
# 함수는 객체 생성 -> 리소스(메모리) 할당
# 람다는 즉시 실행(Heap 초기화) -> 메모리 초기화


def mul_10(num: int) -> int:
    return num * 10


var_func = mul_10
print(var_func) # 메모리 할당됨 : <function mul_10 at 0x000001EA3CC585E0>
print(type(var_func))

lambda_mul_10 = lambda num: num * 10
print('>>>', lambda_mul_10(10))

def func_final(x,y,func):
    print(x * y * func(10))

func_final(10, 10, lambda_mul_10)

print(func_final(10, 10, lambda x : x * 1000))