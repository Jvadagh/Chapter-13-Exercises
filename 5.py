"""
5. Given the definition of the Rational number class, complete the following method named reduce:
class Rational:
    # Other details omitted here ...
    # Returns an object of the same value reduced
    # to lowest terms
    def reduce(self):
        # Details go here
"""
from functools import reduce
from math import gcd

num1 = input('insert first number : ')
num2 = input('insert second number : ')
print(num1, '/', num2)
ratio = num1 + '/' + num2


class Rational():
    def __init__(self, ratio):
        self.ratio = ratio

    def solve(self):
        numbers = [int(i) for i in self.ratio.split('/')]
        denominater = reduce(gcd, numbers)
        solved = [i / denominater for i in numbers]
        return '/'.join(str(i) for i in solved)


Numbers = Rational(ratio)
print(Numbers.solve())
