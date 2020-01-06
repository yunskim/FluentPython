from abc import ABC, abstractmethod
from collections import namedtuple

Customer = namedtuple('Customer', 'name fidelity')
joe = Customer('Jone Doe', 0)
ann = Customer('Ann Smith', 1100)


class LineItem:

    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.quantity * self.price


class Order:

    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion

    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion.discount(self)
        return self.total() - discount

    def __repr__(self):
        fmt = '<Order total: {:.2f} due: {:.2f}>'
        return fmt.format(self.total(), self.due())


class Promotion(ABC):

    @abstractmethod
    def discount(self, order):
        '''할인액을 구체적인 숫자로 반환한다.'''

class FidelityPromo(Promotion):

    def discount(self, order):
        return order.total() * .05 if order.customer.fidelity >= 1000 else 0


class BulkItemPromo(Promotion):

    def discount(self, order):
        discount = 0
        for item in order.cart:
            if item.quantity >= 20:
                discount += item.total() * .01
        return discount

class LargeOrderPromo(Promotion):

    def discount(self, order):
        distinct_items = {item.product for item in order.cart}
        if len(distinct_items) >= 10:
            return order.total() * .07
        return 0

cart = [LineItem('banana', 4, .5),
        LineItem('apple', 10, 1.5),
        LineItem('watermellon', 5, 5.0)]

print(Order(joe, cart, FidelityPromo()))
print(Order(ann, cart, FidelityPromo()))

banana_cart = [LineItem('banana', 30, .5),
               LineItem('apple', 10, 1.5)]


print(Order(joe, banana_cart, BulkItemPromo()))

long_order = [LineItem(str(item_code), 1, 1.0) for item_code in range(10)]
print(Order(joe, long_order, LargeOrderPromo()))
print(Order(joe, cart, LargeOrderPromo()))

# 함수지향전략

from collections import namedtuple
Customer = namedtuple('Customer', 'name fidelity')


class LineItem:

    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.quantity * self.price


class Order:

    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion

    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion(self)
        return self.total() - discount

    def __repr__(self):
        fmt = '<Order total:{:.2f} due: {:.2f}>'
        return fmt.format(self.total(), self.due())


def fidelity_promo(order):
    """충성도 포인트가 100점 이상인 고객에게 전체 5% 할인 적용"""
    return order.total() * .05 if order.customer.fidelity >= 1000 else 0

def bulk_item_promo(order):
    """20개 이산의 동일 상품을 구입하면 10% 할인 적용"""
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * 0.1
    return discount

def large_order_promo(order):
    """10종류 이상의 상품을 구입하면 전체 7% 할인 적용"""
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * 0.07
    return 0

print(Order(joe, cart, fidelity_promo))
print(Order(ann, cart, fidelity_promo))
print(Order(joe, banana_cart, bulk_item_promo))
print(Order(joe, long_order, large_order_promo))
print(Order(joe, cart, large_order_promo))


promos = [fidelity_promo, bulk_item_promo, large_order_promo]

def best_promo(order):
    return max(promo(order) for promo in promos)

print(Order(joe, cart, best_promo))
print(Order(joe, banana_cart, best_promo))
print(Order(joe, long_order, best_promo))
print(Order(joe, cart, best_promo))

# globals()은 딕셔너리 객체를 반환하는데 이 딕셔너리는 현재 모듈에 대한 내용,
# 함수나 메서드 안에서 호출할 때, 함수를 호출한 모듈이 아니라 함수가 정의된
# 모듈을 나타낸다.

promos =[globals()[name] for name in globals()
          if name.endswith('_promo')
          and name != 'best_promo']

print(promos)

print('\n'.join(globals())) # module의 전역변수 딕셔너리를 반환한다.




