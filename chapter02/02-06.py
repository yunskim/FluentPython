# Augmented Assignment Statement
# Inplace ADD를 mutable 객체가 호출하면 i.e.
# a += b 는 a.__iadd__(b) 를 호출하고
# a 의 내용을 바꿉니다
l = [1, 2, 3]
print(id(l))
print(l)
l *= 2
print(id(l))
print(l)

# immuutable 객체에 inplace operation을 적용하면
# 새로운 객체를 생성합니다

t = (1, 2, 3)
print(id(t))
print(t)

t *= 2
print(id(t))
print(t)

# 이상한 inplace operation

t = (1, 2, [30, 40])
t[2] += [50, 60]
print(t)

# 하지만 나는 error가 뜨는데?


