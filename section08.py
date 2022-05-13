# 파이썬 패키지

# 패키지 옞
# 상대 경로
# .. : 부모 디렉토리
# . : 현재 디렉토리

# 사용1(클래스)
import pkg.prints as p
from pkg.calculrations import div as d
import pkg.calculrations as cal
from pkg.fibonacci import Fibonacci as fb
from pkg.fibonacci import Fibonacci


Fibonacci.fib(300)

print(Fibonacci.fib2(400))
print(Fibonacci().title)

# 사용3(클래스)

fb.fib(300)

print(fb.fib2(400))
print(fb().title)


# 사용4(함수)

print(cal.add(10, 100))

# 사용5(함수)
print(int(d(100, 10)))

# 사용6

print(p.prt1())
