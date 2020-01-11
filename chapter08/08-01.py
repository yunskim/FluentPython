# 변수는 이름표, 상자가 아니다.

a = [1, 2, 3]
b = a
a.append(4)
print(b)

# 객체가 변수에 할당되기 전에 생성된다.
class Gizmo:

    def __init__(self):
        print('Gizmo id: %s' % id(self))

x = Gizmo()
y = Gizmo() * 10