charles = {'name': 'Charles L. Dodgson', 'born': 1832}
lewis = charles
print(lewis is charles)

print(id(charles), id(lewis))
lewis['balance'] = 950
print(charles)
alex = {'name': 'Charles L. Dodgson', 'born': 1832, 'balance': 950}
print(charles == alex)
print( alex is not charles)

# is 연산자는 id를 (객체의 정체성을)
# == 연산자는 객체의 값을 비교한다.

t1 = (1, 2, [30, 40])
t2 = (1, 2, [30, 40])
print(t1 == t2)
print(t1[-1])
print(id(t1[-1]))
t1[-1].append(99)
print(t1)
print(t1 == t2)
"""
tuple이 불변이라는 것은 tuple이 담고있는 객체의 reference가 변하지 않는다는 뜻이지
객체의 값은 바뀔 수 있다.
"""
