fruits = ['caju', 'atemoia', 'cajá', 'açaí', 'acerola']
print(sorted(fruits))
import locale
# locale을 정의하는 거라서 처음 프로세스를 돌릴 때 실행합니다
print(locale.setlocale(locale.LC_COLLATE, 'pt_BR.UTF-8'))
sorted_fruits = sorted(fruits, key=locale.strxfrm)
print(sorted_fruits)

import pyuca
coll = pyuca.Collator()
sorted_fruits = sorted(fruits, key=coll.sort_key)
print(sorted_fruits)