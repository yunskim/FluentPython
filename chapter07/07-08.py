import functools
from chapter07.clockdeco import clock

@clock
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)


print(fibonacci(6))

@functools.lru_cache() # lru_cache()는 parameter를 받는 decorator
@clock
def fibonacci2(n):
    if n < 2:
        return n
    else:
        return fibonacci2(n - 2) + fibonacci2(n - 1)

print(fibonacci2(6))

"""
lru_cache(maxsize=128, typed=False)
maxsize는 cache의 크기
typed는 type이 다르면 다른 결과로 보관할 것인지 여부
decorated된 함수는 hashable한 parameters를 사용해야 합니다.
내부적으로 dictionary를 사용하기 때문입니다.
"""

import html

def htmlize(obj):
    content = html.escape(repr(obj))
    return '<pre>{}</pre>'.format(content)

print(htmlize({1, 2, 3}))
print(htmlize(abs))
print(htmlize('Heimlich & Co. `n- a game'))
print(htmlize(42))
print(htmlize(['alpha', 66, {3, 2, 1}]))
# 파이썬에서는 메서드나 함수의 오버로딩을 지원하지 않으므로
# 서로 다르게 처리하고자 하는 자료형별로 서로 다른 시그너처를 가진 htmlize()를
# 만들 수 없다.

from functools import singledispatch
from collections import abc
import numbers
import html

"""
https://soooprmx.com/archives/5852
singledispatch는 제네릭을 생성하는 표준라이브러리이다.

단일 디스패치 제네릭을 구현하는 방법을 제공한다.
singledispatch는 함수를 패링하는 함수이고, 래핑된 결과는 각각의 타입에 대해
어떻게 사용될 지 구체적으로 정의한다.

한마디로 말하면 singledispatch는 decorator를 생성하는 decorator를 생성하는
decorator이다.

singledispatch를 사용해 임의의 함수 func를 만든다. func는 타입이 정의되지 않은
함수로  기본적으로 일반 파이썬 함수와 동일하다.

func.register(type)을 통해 특정 파라미터 타입에 대한 함수를 정의할 수 있다.

"""

from functools import singledispatch
from collections import abc
import numbers
import html

@singledispatch
def htmlize(obj):
    content = html.escape(repr(obj))
    return '<pre>{}</pre>'.format(content)

@htmlize.register(str)
def _(text): # 특화된 함수의 이름이 필요없으므로 언더바로 함수명을 저장한다.
    content = html.escape(text).replace('\n', '<br>\n')
    return '<p>{}</p>'.format(content)

@htmlize.register(numbers.Integral)
def _(n):
    return '<pre>{0} {0x{0:x})</pre>'.format(n)

@htmlize.register(tuple)
@htmlize.register(abc.MutableSequence)
def _(seq):
    inner ='</li>\n<li>'.join(htmlize(item) for item in seq)
    return '<ul>\n<li>' + inner + '</li>\n<\/ul>'


