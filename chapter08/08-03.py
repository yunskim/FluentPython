# 기본 복사는 shallow copy == reference만 복사한다.

l1 = [3, [55, 44], (7, 8, 9)]
l2 = list(l1)

print(l2)
print(l2 == l1)
print(l2 is l1)

l1 = [3, [66, 55, 44], (7, 8, 9)]
l2 = list(l1)
l1.append(100)
l1[1].remove(55)
print('l1:', l1)
print('l2:', l2)
l2[1] += [33, 22]
l2[2] += (10, 11) # 새로운 tuple을 만든다
print('l1:', l1)
print('l2:', l2)

# tuple에 += 을 실행하면 concatenated




