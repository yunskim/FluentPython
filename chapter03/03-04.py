# setdefault를 대신해서 defaultdict를 사용합시다.
# defaultdict는 존재하지 않은 키로 검색할 때 요청에 따라
# 자동으로 항목을 생성하도록 설정되어 있습니다.

import sys
import re
import collections

WORD_RE = re.compile(r'\w+')
index = collections.defaultdict(list) # 없는 키를 검색하면 list를 생성함
with open('zen.txt', encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)
            index[word].append(location)


for word in sorted(index, key=str.upper):
    print(word, index[word])


class StrKeyDict(dict):

    def __missing__(self, key):
        # KeyError가 발생하면 __missing__을 실행합니다
        # key가 str인데 __missing__이라면 원래 없는 키이니 KeyError를 발생하고
        if isinstance(key, str):
            raise KeyError(key)
        # key가 str이 아니면 str으로 바꿔서 다시 한번 시도한다
        return self[str(key)]

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys()


d = StrKeyDict([('2', 'two'), ('4', 'four')])
print(d['2'])
print(d[4])
print(d.get('2'))
print(d.get(4))
print(2 in d)
print(4 in d)


