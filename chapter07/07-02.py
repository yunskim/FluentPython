"""
데커레이터는 데커레이트된 함수가 정의된 직후에 실행된다.
이는 일반적으로 파이썬이 로딩되는 시점, 즉 임포트 타임에 실행된다.
"""
registry = list()

def register(func):
    print('running register(%s)' % func)
    registry.append(func)
    return func

@register
def f1():
    print('running f1()')

@register
def f2():
    print('running f2()')

def f3():
    print('running f3()')

def main():
    print('running main()')
    print('registry ->', registry)
    f1()
    f2()
    f3()


if __name__ == '__main__':
    main()

"""
running register(<function f1 at 0x0388C420>)
running register(<function f2 at 0x0388C588>)
running main()
registry -> [<function f1 at 0x0388C420>, <function f2 at 0x0388C588>]
running f1()
running f2()
running f3()

main()이 실행되기 전 decorator가 실행됩니다.
"""
