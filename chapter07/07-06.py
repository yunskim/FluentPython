"""
make_averager()는 효율적이지 않다.
합계와 항목 수를 저장한 수 평균을 계산하는 것이 더 효율적이다.
"""


"""
잘못된 closure

def make_averager():
    count = 0
    total = 0

    def averager(new_value):
        count += 1
        total += new_value
        return total / count

    return averager

avg = make_averager()
print(avg(10))
"""

def make_averager():
    total = 0
    count = 0

    def averager(new_value):
        # 함수 안에서 nonlocal이 선언되면
        # 변수에 새로운 값이 할당되더라도
        # free variable로 취급한다.
        # 새로운 값으로 갱신되면 closure에
        # 저장된 바인딩이 갱신된다.
        nonlocal total, count
        total += new_value
        count += 1
        return total / count

    return averager

avg = make_averager()
print(avg(10))
print(avg(11))
print(avg(12))


