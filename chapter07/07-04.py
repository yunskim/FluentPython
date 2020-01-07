"""
b = 6
def f2(a):
    print(a)
    print(b)
    b = 9

print(f2(3))
"""
"""
UnboundLocalError: local variable 'b' referenced before assignment
"""

"""
파이썬이 함수 본체를 컴파일할 때 b가 함수 안에서 할당되므로 b를 지역변수로 판단한다.

함수 본체 안에서 할당된 변수는 지역변수로 판단한다.
"""

b = 6
def f3(a):
    global b
    print(a)
    print(b)
    b = 9

f3(3)
print(b)
b = 30
f3(3)
print(b)
