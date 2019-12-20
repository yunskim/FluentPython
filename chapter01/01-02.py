# 특별메서드는 내가 아니라 인터프리터가 호출한다.
# for i in x: 는 iter(x)를 호출하고 내부적으로 다시 x.__iter__()를 호출한다.

from math import hypot

class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        '''
        __repr__은 object가 구별가능하게
        '%r' String(converts any Python object using repr()).
        '''
        # TODO
        # 이거 어떻게 format()으로 바꾸지?
        return 'Vector(%r, %r)' % (self.x, self.y)
        # !r을 사용하면 가능합니다.
        return 'Vector({!r}, {!r})'.format(self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        # 의도적으로 새 객체를 생성합니다.
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

v1 = Vector(2, 4)
v2 = Vector(2, 1)

print(v1 + v2)
v = Vector(3, 4)
print(abs(v))
print(v * 3)
print(abs(v * 3))