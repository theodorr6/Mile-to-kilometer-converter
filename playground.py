# def add(*args):
#     sum = 0
#     for n in args:
#         sum += n
#     return sum
#
#
# print(add(1, 2, 3, 4, 5, 6, 7))
#
#
# def calculate(n,**kwargs):
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#     print(n)
#
#
# calculate(2, add=3, multiply=5)

class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw("model")

my_car = Car(make= "nissan", model="GTR")
print(my_car)