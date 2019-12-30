# bytes는 immutable
# bytearray는 mutable

cafe = bytes('café', encoding='utf_8')
print(cafe)
print(cafe[0])
print(cafe[:1])
cafe_arr = bytearray(cafe)
print(cafe_arr)
print(cafe_arr[-1:])

import array
numbers = array.array('h', [-2, -1, 0, 1, 2]) # short integer
octets = bytes(numbers)
print(octets)

import struct
fmt = '<3S3SHH'
with open('filter.gif', 'rb') as fp:
    img = memoryview(fp.read())

header = img[:10]
bytes(header)
struct.unpack(fmt, header)
del header
del img

