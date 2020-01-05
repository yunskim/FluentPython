'''
모든 파이썬 객체를 함수처럼 사용할 수 있습니다.
__call__() 메서드를 추가하시면 가능합니다.
'''

import random

class BingoCage:

    def __init__(self, items):
        self._items = list(items)
        random.shuffle(self._items)
        """Shuffle list x in place, and return None.
        Optional argument random is a 0-argument function returning a
        random float in [0.0, 1.0); if it is the default None, the
        standard random.random will be used.
        """

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BignCage')

    def __call__(self):
        return self.pick()

bingo = BingoCage(range(3))
print(bingo.pick())
print(bingo())
print(callable(bingo))
