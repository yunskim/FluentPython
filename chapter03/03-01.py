my_dict = {}
import collections.abc
print(isinstance(my_dict, collections.abc.Mapping))

tt = (1, 2, (30, 40))
print(hash(tt))
tl = (1, 2, ([30, 40])) # 모든 요소가 hashable 해야 합니다
#  print(hash(tl))

tf = (1, 2, frozenset([30, 40]))
print(hash(tf))

a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
'''
zip(*iterables)
iterables을  zipping합니다.
J에서 ,.과 유사하다고 할 수 있습니다
'''
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'three': 3, 'one': 1, 'two': 2})
print(a == b == c == d == e)


