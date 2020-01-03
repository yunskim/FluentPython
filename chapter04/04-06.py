# unicode에는 발음 구별기호(diacritical mark)가 있어
# 인쇄할 때 앞 문자와 하나로 결합되어 출력된다.

s1 = 'café'
s2 = 'cafe\u0301'

print(s1, s2)
print(len(s1))
print(len(s2))
print(s1 == s2)

# 유니코드 표준에서는 이 두 개의 시퀸스를 규범적으로 동일하독 하며, 어플리케이션은
# 이 두 시퀸스를 동일하게 처리해야 한다.
# 하지만 파이썬은 서로 다른 두 개의 코드 포인트 시퀸스로 보고 이 둘을 서로
# 동일하지 않다고 판단한다.

# 해결책은 유니코드 정규화
# 방법 1
# Normalization Form C 문자와 코드포잉트를 조합해 가장 짧은 동일문자열로 구성
# Normalization Form D 무조합된 문자를 기본문자와 별도의 결합문자로 분리한다.
from unicodedata import normalize

print(len(normalize('NFC', s1)), len(normalize('NFC', s2)))
print(len(normalize('NFD', s1)), len(normalize('NFD', s2)))

print(normalize('NFC', s1) == normalize('NFC', s2))
print(normalize('NFD', s1) == normalize('NFD', s2))

# 키보드는 일반적으로 NFC
# 하지만 조심하자

from unicodedata import normalize, name

ohm = '\u2126'
print(ohm)
print(name(ohm))
ohm_c = normalize('NFC', ohm)
print(ohm_c)
print(name(ohm_c))
print(ohm == ohm_c)
print(normalize('NFC', ohm) == normalize('NFC', ohm_c))

# 하나의 문자가 하나의 규범적인 코드를 가지는 것이 유니코드의 목표이지만
# 예외도 있습니다.

from unicodedata import normalize, name

half = '½'
print(half)
print(normalize('NFKC', half))
print(len(normalize('NFKC', half)))
four_squared = '4²'
print(normalize('NFKC', four_squared))
micro = 'µ'
micro_kc = normalize('NFKC', micro)
print(micro, micro_kc)
print(ord(micro), ord(micro_kc))
print(name(micro), name(micro_kc))

# 쿼리할 때는 NFKC, NFKD 정규화가 도움이 될 것입니다. 저장하거나 영구보관하는 것은 권하지 않습니다.

# case folding
# 모든 텍스트를 소문자로 변환하는 연산
micro = 'µ'
print(name(micro))
micro_cf = micro.casefold()
print(name(micro_cf))
print(micro, micro_cf)
# eszett = '\u00DF'
# print(name(eszett))
# eszett_cf = eszett.casefold()
# print(name(eszett_cf))

from unicodedata import normalize


def nfc_equal(str1, str2):
    return normalize('NFC', str1) == normalize('NFC', str2)


def fold_equal(str1, str2):
    return normalize('NFC', str1.casefold()) == normalize('NFC', str2.casefold())


s3 = 'Straße'
s4 = 'strasse'

print(s3 == s4)
print(nfc_equal(s3, s4))
print(fold_equal(s3, s4))
print(fold_equal(s1, s2))
print(fold_equal('A', 'a'))

import unicodedata
import string


def shave_marks(txt):
    norm_txt = unicodedata.normalize('NFD', txt)
    shaved = ''.join(c for c in norm_txt if not unicodedata.combining(c))
    return unicodedata.normalize('NFC', shaved)


order = '“Herr Voß: • ½ cup of Œtker™ caffè latte • bowl of açaí.”'
print(shave_marks(order))
Greek = 'Ζέφυρος, Zéfiro'
print(shave_marks(Greek))


def shave_marks_latin(txt):
    norm_txt = unicodedata.normalize('NFD', txt)
    latin_base = False
    keepers = []
    for c in norm_txt:
        if unicodedata.combining(c) and latin_base:
            continue
        keepers.append(c)

        if not unicodedata.combining(c):
            latin_base = c in string.ascii_letters
        shaved = ''.join(keepers)
        return unicodedata.normalize('NFC', shaved)


print(shave_marks_latin(order))
print(shave_marks_latin(Greek))

'''
Python string method translate() returns a copy of the string in which
all characters have been translated using table
(constructed with the maketrans() function in the string module),
optionally deleting all characters found in the string deletechars.
'''

single_map = str.maketrans("""‚ƒ„†ˆ‹‘’“”•–—˜›""",  # <1>
                           """'f"*^<''""---~>""")

multi_map = str.maketrans({  # <2>
    '€': '<euro>',
    '…': '...',
    'Œ': 'OE',
    '™': '(TM)',
    'œ': 'oe',
    '‰': '<per mille>',
    '‡': '**',
})

multi_map.update(single_map)


def dewinize(txt):
    return txt.translate(multi_map)


def asciize(txt):
    no_marks = shave_marks_latin(dewinize(txt))
    no_marks = no_marks.replace('ß', 'ss')
    return unicodedata.normalize('NFKC', no_marks)

print(dewinize(order))
print(asciize(order))
