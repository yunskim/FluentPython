from functools import reduce
from operator import mul


def fact(n):
    return reduce(lambda a, b: a * b, range(1, n + 1))


def fact2(n):
    return reduce(mul, range(1, n+1))


metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),   # <1>
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]

from operator import itemgetter

cc_name = itemgetter(1, 0)

for city in sorted(metro_areas, key=itemgetter(1)):
    print(city)

for city in metro_areas:
    print(cc_name(city))

from collections import namedtuple
LatLong = namedtuple('LatLong', 'lat long')
Metropolis = namedtuple('Metropolis', 'name cc pop coord')
metro_areas = [Metropolis(name, cc, pop, LatLong(lat, long)) for name, cc, pop, (lat, long) in metro_areas]
print(metro_areas[0])
print(metro_areas[0].coord.lat)

from operator import attrgetter

name_lat = attrgetter('name', 'coord.lat')
for city in sorted(metro_areas, key=attrgetter('coord.lat')):
    print(name_lat(city))

from operator import methodcaller
s = 'The time has come'
upcase = methodcaller('upper') # str의 upper method
print(upcase(s))

hiphenate = methodcaller('replace', ' ', '-')
print(hiphenate(s)) # str의 replace method

print(s.replace(' ', '-'))

from operator import mul
from functools import partial
triple = partial(mul, 3)
print(triple(7))

print(list(map(triple, range(1, 10))))

import unicodedata, functools
nfc = partial(unicodedata.normalize, 'NFC')
s1 = 'café'
s2 = 'cafe\u0301'

print(s1, s2)
print(s1 == s2)
print(nfc(s1) == nfc(s2))


def tag(name, *content, cls=None, **attrs):
    '''하나 이상의 HTML 태그를 생성한다.'''
    if cls is not None:
        attrs['class'] = cls
    if attrs:
        attr_str = ''.join(' %s="%s"' % (attr, value) for attr, value in sorted(attrs.items()))
    else:
        attr_str = ''
    if content:
        return '\n'.join('<%s%s>%s</%s>' % (name, attr_str, c, name) for c in content)

    else:
        return '<%s%s />' % (name, attr_str)


print(tag)
picture = partial(tag, 'img', cls='pic-frame')
print(picture(src='wumpus.jpeg'))
print(picture)
print(picture.func)
print(picture.args)
print(picture.keywords )

