'''
d[k]는 failed, when k is not in keys
'''

import sys
import re

WORD_RE = re.compile(r'\w+')
index = {}

with open('zen.txt', encoding='utf-8') as fp:
    # enumerate(iterable, start=0)
    # start는 starting index를 무엇으로 할 것인지 지정한다
    # 기본값은 0
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)
            occurrences = index.get(word, []) # word에 해당하는 key가 없으면 none 대신 []을 return
            occurrences.append(location)
            index[word] = occurrences

for word in sorted(index, key=str.upper):
    print(word, index[word])


import sys
import re

WORD_RE = re.compile(r'\w+')

index = {}

with open('zen.txt', encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, start=1): # file object는 iterator
        for match in WORD_RE.finditer(line):
            word = match.group() # group을 반환
            column_no = match.start() + 1
            location = (line_no, column_no)
            index.setdefault(word, []).append(location) #

for word in sorted(index, key=str.upper):
    print(word, index[word])

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.setdefault("color", "White")

print(car)

