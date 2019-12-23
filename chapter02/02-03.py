lax_coordinates = (33.9425, -118.408056)
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
# tuple을 레코드처럼 사용하는 방법입니다
traveler_ids = [('USA', '311958955'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]
for passport in sorted(traveler_ids):
    print("{}/{}".format(*passport))
    # print("%s/%s" % passport) 로 사용할 수도 있습니다

# tuple unpacking
lax_coordinates = (33.9425, -118.408056)
latitude, longitude = lax_coordinates

print(latitude)
print(longitude)

print(divmod(20, 8))

t = (20, 8)
print(divmod(*t))

quotient, remainder = divmod(*t)
print(quotient)
print(remainder)

import os
_, filename = os.path.split('/home/luciano/.ssh/idrsa.pub')
print(_)
print(filename)

# 초과항목을 잡기 위해 * 사용

a, b, *rest = range(5)
print(a, b, rest)

a, b, *rest = range(3)
print(a, b, rest)

a, b, *rest = range(2)
print(a, b, rest)

a, *body, c, d = range(5)
print(a, body, c, d)

*head, b, c, d = range(5)
print(head, b, c, d)

metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),   # <1>
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]
# '^' -> Forces the field to be centered within the available space.
print("{:<30}".format('left alignment'))
print("{:>30}".format('right alignment'))
print("{:^30}".format('center alignment'))

print("{:30}".format('reserved spaces'))

print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
fmt = '{:15} | {:9.4f} | {:9.4f}'

# f -> fixed point notation
for name, cc, pop, (latitude, longitude) in metro_areas:
    if longitude <= 0:
        print(fmt.format(name, latitude, longitude))

# named tuple
# named tuple은 tuple의 subclass입니다

from collections import namedtuple

Card = namedtuple('Card', (['rank', 'suit']))

# Card는 factory 함수의 이름
# subclass의 이름은 Card

City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 36933, (35.689722, 139.691))
print(tokyo)

# 지금까지는 record로서의 tuple
# 이제부터는 immutable list로서의 tuple



