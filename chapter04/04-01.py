s = 'café'
print(s)
print(len(s))

b = s.encode('utf8')
print(b)
print(len(b))

print(b.decode('utf8'))
print(len(b.decode('utf8')))
