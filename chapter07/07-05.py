"""
클로저 is not equal to 익명함수!

클로저는 함수본체에서 정의핮 않고 참조하는 비전역변수를 포함한 확장범위를 가진 함수이다.
함수 본체 외부에 정의되 ㄴ비전역변수에 접근할 수 잇다는 것이 중요하다.

"""
class Average():

    def __init__(self):
        self.series = []

    def __call__(self, new_value):
        self.series.append(new_value)
        total = sum(self.series)
        return total / len(self.series)

avg = Average()
print(avg(10))
print(avg(11))
print(avg(12))

def make_averager():
    series = []
    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total / len(series)

    return averager

avg = make_averager()
print(avg(10))
print(avg(11))
print(avg(12))

"""
series는 자유변수: 지역 범위에 바인딩되어 있지 않은 변수를 말한다
"""

print(avg.__code__.co_varnames)
print(avg.__code__.co_freevars)
print(avg.__closure__)
print(avg.__closure__[0].cell_contents)

"""
함수가 비전역 외부 변수를 다루는 경우는 그 함수가 다른 함수 안에 정의된
경우뿐이라는 점에 주의하라.
"""




