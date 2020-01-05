import bobo

@bobo.query('/')
def hello(person):
    return 'Hello %s' % person

def clip(text, max_len=80):
    """
    max_len 앞이나 뒤의 마지막 공백에서 잘라낸 텍스트를 반환한다.
    """
    end = None
    if len(text) > max_len:
        # text.rfind returns index of sub from right side of text
        # rfind(sub, start, end)
        space_before = text.rfind(' ', 0, max_len)
        if space_before >= 0: end = space_before
        else:
            space_after = text.rfind(' ', 0, max_len)
            if space_after >= 0:
                end = space_after
    if end is None: # 공백이 없다.
        end = len(text)
    return text[:end].rstrip()


print(clip.__defaults__)
print(clip.__code__)
print(clip.__code__.co_varnames)

from inspect import signature
sig = signature(clip)
print(sig)
for name, param in sig.parameters.items():
    print(param.kind, ':', name, '=', param.default)

my_tag = {'name': 'img', 'title': 'Sunset Boulevard', 'src': 'sunset.jpg', 'cls': 'framed'}
bound_args = sig.bind(**my_tag)
print(bound_args)






    







