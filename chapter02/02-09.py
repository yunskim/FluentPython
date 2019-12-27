# list보다 효율적인 자료구조형이 있을 때
# array는 같은 type의 list

from array import array
from random import random
floats = array('d', (random() for i in range(10**7)))
print(floats[-1])

# file mode write and binary
fp = open('floats.bin', 'wb')
floats.tofile(fp)
fp.close()

fp = open('floats.bin', 'rb')
floats2 = array('d')
floats2.fromfile(fp, 10**7)
fp.close()
print(floats2[-1])
floats2 == floats

import array
numbers = array.array('h', [-2, -1, 0, 1, 2] ) #	h: signed short
memv = memoryview(numbers)

print(len(memv))
print(memv[0])

memv_oct = memv.cast('B')
print(memv_oct.tolist())
memv_oct[5] = 4
print(numbers)

import numpy as np
a = np.arange(12)
print(a)
print(type(a))
print(a.shape)
a.shape = 3, 4
print(a)
print(a[2])
print(a[2, 1])
print(a[2, 1].shape) # J의 인덱스와 매우 유사하다
print(a[:, 1])
print(a.transpose())

floats = np.array([random() for x in range(10 ** 7)], dtype='float64')
print(floats[-3:])
from time import perf_counter as pc # performance counter
t0 = pc()
floats /= 3
print(pc() - t0)
np.save('floats-10M', floats)
floats2 = np.load('floats-10M.npy', 'r+')
floats2 *= 6
floats2[-3:]


from collections import deque # double ends queue
dq = deque(range(10), maxlen=10)
print(dq)
dq.rotate(3)
print(dq)
dq.rotate(-4)
print(dq)
dq.appendleft(-1)
print(dq)
dq.extend([11, 22, 33])
print(dq)
dq.extendleft([10, 20, 30, 40])
print(dq)







