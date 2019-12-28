# collections.OrderedDict -> key가 입력된 순서대로 항목을 반복하는 순서를 예측할 수 있다
# collections.ChainMap -> 매핑의 목록을 담고 있다
# collections.Counter -> 모든 키가 각각 정수형 카운터가 있어서 기존 기를 갱신하면 카운터가 늘어난다

import collections
ct = collections.Counter('abracadabra')
print(ct)

ct.update('aaaaazzz')
print(ct)
print(ct.most_common(2))
