'''
일급객체의 정의
1) 런타임에 생성이 가능하다
2) 데어터 구조체의 변수나 요소에 할당할 수 있다(일급객체를 하나의 묶음으로 다룰 수 있다)
3) 함수 인수로 전달할 수 있다
4) 함수 결과로 반환할 수 있다

파이썬에서 function은 일급객체(first-class object)
'''

def factorial(n):
    '''return n!'''
    return 1 if n < 2 else n * factorial(n-1)

print(factorial(42))
print(factorial.__doc__)
print(type(factorial))

'''
1) 함수를 변수에 할당하고
2) 변수명을 통해 함수를 호출한다
3) 함수를 map함수의 parameter로 전달한다
'''

fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
print(sorted(fruits, key=len))

fact = factorial
print(fact)
print(fact(5))
# map(function, data)
print(list(map(fact, range(11))))

def reversed(word):
    return word[::-1]

print(reversed('testing'))
print(sorted(fruits, key=reversed))


# 5.2.1 map(), filter(), reduce()의 대안
# map, filter, reduce를 사용할 수도 있지만
# 단순히 list를 만든다면 comprehensive list를 사용하세요
print(list(map(fact, range(6))))
print([fact(n) for n in range(6)])

print(list(map(factorial, filter(lambda n: n % 2, range(6)))))
print([factorial(n) for n in range(6) if n % 2])

# reduce는 처음이라
from functools import reduce
from operator import add
print(reduce(add, range(100)))
print(sum(range(100)))