# 사용자가 매핑을 변경하지 못하게 제한하고 싶을 때
from types import MappingProxyType

d = {1: 'A'}
d_proxy = MappingProxyType(d)
print(d_proxy)
print(d_proxy[1])

d[2] = 'B'
print(d_proxy[2])

# d_proxy는 매핑을 변경할 수 없고
# d를 통해 간접적으로만 접근이 가능하다



