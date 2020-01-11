registry = []

def register(func):
    print('running register(%s)' % func)
    registry.append(func)
    return func


@register
def f1():
    print('running f1()')

print('running main()')
print('registry ->', registry)
f1()

# 매개변수화된 등록 데커레이터

registry = set()


def register(active=True):

    def decorate(func):
        print('running register(active=%s) -> decorate(%s' % (active, func))

        if active:
            registry.add(func)
        else:
            registry.discard(func)
        return func

    return decorate

# register는 decorator factory

@register(active=False)
def f1():
    print('running f1()')

@register()
def f2():
    print('running f2()')

def f3():
    print('running f3()')

print(registry)
print(register()(f3))
print(registry)
register(active=False)(f2)
print(registry)



