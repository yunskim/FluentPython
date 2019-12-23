import collections

l = [10, 20, 30, 40, 50, 60]
print(l[:2]) # 마지막 인덱스 다음 혹은 개수 혹은 2번 인덱스에서 분할
print(l[2:])
print(l[:3])
print(l[3:])

# s[a:b:c] -> a에서 시작해 b까지 c보폭만큼
s = 'bicycle'
print(s[::3])
print(s[::-1])
print(s[::-2])

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

deck = FrenchDeck()
print(deck[12::13])

# 다차원 슬라이싱을 할 때 __getitem__()은
# tuple을 인풋으로 받는다

l = list(range(10))
print(l)
l[2:5] = [20, 30]
print(l)

del l[5:7]
print(l)
l[3::2] = [11, 22]
try:
    l[2:5] = 100
    print(l)
except:
    print(l)
    l[2:5] = [100]
    print(l)


