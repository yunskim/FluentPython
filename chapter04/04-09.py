import re
re_numbers_str = re.compile(r'\d+')
re_words_str = re.compile(r'\w+')
re_numbers_byte = re.compile(rb'\d+')
re_words_byte = re.compile(rb'\w+')

text_str = text_str = ("Ramanujan saw \u0be7\u0bed\u0be8\u0bef"  # <3>
            " as 1729 = 1³ + 12³ = 9³ + 10³.")
print(text_str)
text_bytes = text_str.encode('utf_8')
print(text_bytes)

print('Text', repr(text_str), sep='\n   ')
print('Numbers')
print('    str    :', re_numbers_str.findall(text_str))
print('    bytes  :', re_numbers_byte.findall(text_bytes))
print('Words')
print('    str    :', re_words_str.findall(text_str))
print('    bytes  :', re_words_byte.findall(text_bytes))

import os
print(os.listdir('.'))
print(os.listdir(b'.'))

pi_name_bytes = os.listdir(b'.')[1]
pi_name_str = pi_name_bytes.decode('ascii', 'surrogateescape')
print(pi_name_str)
print(pi_name_str.encode('ascii', 'surrogateescape'))
