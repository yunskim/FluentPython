# 파이썬 함수의 매개변수는 call by sharing으로 전달됩니다.
# 다른 말로 하면 함수 안의 매개변수는 실제 인수의 별명이다.

def f(a, b):
    a += b
    return a # 이렇게 하면 새로 정의된 함수의 reference를 return 하는 것임

x = 1
y = 2
print(f(x, y))
print(x, y)

a = [1, 2]
b = [3, 4]
print(f(a, b))
print(a, b)

t = (10, 20)
u = (30, 40)
print(f(t, u))
print(t, u)

class HauntedBus:

    def __init__(self, passengers=[]):
        self.passengers = passengers

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)

    def __repr__(self):
        return '<Bus {}>'.format(repr(self.passengers))


bus1 = HauntedBus(['Alice', 'Bill'])
print(bus1)
bus1.pick('Charlie')
print(bus1)

bus2 = HauntedBus()
bus2.pick('Charlie')
print(bus2)

# 함수가 로드될 때 []의 참조가 기본값으로 정해지고 그 참조가 계속 사용된다.
bus3 = HauntedBus()
print(bus3)

# 가변값을 받는 매개변수의 기본값으로 None을 사용하는 것이 좋다.
# None이 아닌 경우 인수의 사본을 오브젝트에 저장하는 것이 좋다.


class TwilightBus:

    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = [] # 늘 새로운 []을 사용한다.
        else:
            self.passengers = list(passengers) # 모든 반복 가능한 객체를 받으므로 list를 사용할 수 있다.

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)

basketball_team = ['Sue', 'Tina', 'Maya', 'Diana', 'Pat']
bus = TwilightBus(basketball_team)
bus.drop('Tina')
bus.drop('Pat')
print(basketball_team)
print(bus.passengers)







