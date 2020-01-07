'''
명령 디자인 패턴
명령패턴의 목적은 연산을 실행하는 객체(호출자 invoker)와
연산을 구현하는 객체(수신자 receiver)를 분리하는 것이다.
예를 들어 GUI의 메뉴항목이 호출자이고 편집되고 있는 문서나
애플리케이션 자신이 수신자다.

명령 객체를 수신자와 호출자 사이에 놓고 , 멸령은 execute()라는 단 사나의 메서드로 인터페이스를 구현한다.
execute()는 원하는 연산자를 수행하기 위해 수신자가 가지고 있는 메서드를 호출한다.

호출자는 수신자의 인터페이스를 알 필요가 없고, 멸령의 서브클래스를 통해 서로 다른 수신자를 추가할 수 있다.

초출자는 구체적인 명열으로 설정되며, 연산을 실행하기 위해 execute()메서드를 호출한다.

명령은 콜백에 대한 객체지향식 대체물이다.

https://mrw0119.tistory.com/69
Command 패턴은 특정 객체에 대한 명령을 캡슐화하여 처리하는 패턴이다.

패턴의 주체는 Invoker, Command, Receiver이다.

1) Invoker: 명령을 가지고 있으며 요청에 따라 명령을 실행시킨다.
2) Command: 수신자에게 특정작업을 지시한다.
3) Receiver: 명령의 지시대로 작업을 수행한다

예)

Invoker
    Command A
    Command B
    Command C

A ~ ReceiverA
B ~ ReceiverA
C ~ ReceiverB

예)

Switch
    On
    Off

On ~ Light
Off ~ Light

Switch는 on, off 명령을 가지고 있는 invoker이고
light는 on, off 명령에 따라 작업을 수행하는 receiver이다.

스위치는 온오프 명령을 받고, 해당 명령을 실행한다.
해당 명령은 라이트에게 온오프를 지시한다.
라이트는 명령에 따라 자신을 온오프한다.
'''

class MacroCommand:
    """명령 리스트를 실행하는 명령"""
    def __init__(self, commands):
        self.commands = list(commands)

    def __call__(self):
        for command in self.commands:
            command()

'''
invoker가 command를 호출하면 됩니다. __call__()을 사용해 객체를 callable로 만들 수 있다.
'''


