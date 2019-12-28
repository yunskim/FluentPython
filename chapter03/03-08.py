l = ['spam', 'spam', 'egg', 'egg']
print(set(l))

print(list(set(l)))

# intersection의 크기를 구하는 여러가지 방법

needles = set([1, 2, 3])
haystack = set(range(10))


found = len(needles & haystack)
print(found)

found = 0
for n in needles:
    for h in haystack:
        if n == h:
            found += 1

print(found)

found = len(set(needles) & set(haystack))
print(found)
found = len(set(needles).intersection(haystack))
print(found)

# 공집합은 set()로 표기합니다
s = {1}
print(type(s))
print(s)
print(s.pop())
print(s)

from dis import dis
dis('{1}')
dis('set([1])')
print(frozenset(range(10)))

from unicodedata import name
'''
def name(*args, **kwargs): # real signature unknown
    """
    Returns the name assigned to the character chr as a string.
    
    If no name is defined, default is returned, or, if not given,
    ValueError is raised.
    """
    pass
'''

print({chr(i) for i in range(32, 256) if 'SIGN' in name(chr(i), '')})
