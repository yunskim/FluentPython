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