"""
1) 파이썬이 데커레이터 구문을 평가하는 방식
2) 변수가 지역변수인지 파이썬이 판단하는 방식
3) 클로저의 존재 이유와 작동 방식
을 알고 난 후

a) 잘 작동하는 데커레이터 구현하기
b) 표준 라이브러리에서 제공하는 재미있는 데커레이터들
c) 매개변수화된 데커레이터 구현하기
를 살펴볼 것입니다.
"""

"""
@decorator
def target():
    print('running target()')

과 

target = decorator(target)은 동일합니다.
원래 정의된 target과 decorator의 반환형 target은 다른 함수객체입니다.

"""

def deco(func):
    def inner():
        print('running inner()')
    return inner

@deco
def target():
    print('running target()')

target()
print(target)
