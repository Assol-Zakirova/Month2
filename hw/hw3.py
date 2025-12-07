#1

# class Product:
#     def __init__(self, name, price, discount):
#         self.name = name
#         self._price = price
#         self.__discount = discount
#     def get_price(self):
#         return self._price - (self._price * (self.__discount / 100))
#     def set_discount(self, percent):
#         if 0 <= percent <= 50:
#             self.__discount = percent
#             return f'Your discount is now {percent}'
#         return 'Error'
#
#     def apply_extra_discount(self, secret_code):
#         if secret_code == 'VIP123':
#             if self.__discount + 5 <= 50:
#                 self.__discount += 5
#                 return True
#         return 'Incorrect code'
# p = Product("Iphone", 1000, 10)
#
# p.set_discount(20)
# print("Цена со скидкой:", p.get_price())
#
# p.apply_extra_discount("VIP123")
# print("Цена после VIP:", p.get_price())
#
# p.apply_extra_discount("wrong")
# print("Цена итоговая:", p.get_price())

#2

from abc import ABC, abstractmethod
class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass
    @abstractmethod
    def refund(self, amount):
        pass
class CardPayment(PaymentMethod):
    def pay(self, amount):
        return f'Оплата картой: {amount}'
    def refund(self, amount):
        return f'Оплата картой: {amount}'
class CashPayment(PaymentMethod):
    def pay(self, amount):
        return f"Оплата наличными: {amount}"
    def refund(self, amount):
        return f"Оплата наличными: {amount}"
class CryptoPayment(PaymentMethod):
    def pay(self, amount):
        return {"type": "crypto", "amount": amount, "currency": "USDT"}
    def refund(self, amount):
        return {"type": "crypto", "amount": amount, "currency": "USDT"}
class PaymentProcessor:
    def __init__(self, method):
        self.method = method
    def process(self, amount):
        print(self.method.pay(amount))


processor = PaymentProcessor(CardPayment())
processor.process(100)

processor = PaymentProcessor(CashPayment())
processor.process(50)

processor = PaymentProcessor(CryptoPayment())
processor.process(200)


