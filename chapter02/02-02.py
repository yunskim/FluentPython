symbols = '$¢£¥€¤'
codes = []
for symbol in symbols:
    codes.append(ord(symbol))

print(codes)

codes = [ord(symbol) for symbol in symbols]
print(codes)

beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]
print(beyond_ascii)

beyond_ascii = list(filter(lambda c: c > 127, map(ord, symbols)))
print(beyond_ascii)

colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshrits = [(color, size) for color in colors for size in sizes]
print(tshrits)

for color in colors:
    for size in sizes:
        print((color, size))

'''
generator expression을 사용하면 list나 tuple을 만들 필요없이
다음 값을 하나씩 만들 수 있어 list전체를 만드는데 필요한 메모리를
절약할 수 있습니다.
'''

print(tuple(ord(symbol) for symbol in symbols))
import array

# 배열생성자는 인수를 두 개 받으며 제너레이터 표현식 앞뒤에 반드시 괄호를
# 넣어야 한다.
print(array.array('I', (ord(symbol) for symbol in symbols)))


# 예제 2-6 제너레이터 표현식에서의 데카르트 곱
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
for tshrits in ('{} {}'.format(c, s) for c in colors for s in sizes):
    # generator는 괄호로 표현됩니다
    # 한 번에 하나씩 항목을 생성하며 리스트를 생성하지 않습니다
    print(tshrits)