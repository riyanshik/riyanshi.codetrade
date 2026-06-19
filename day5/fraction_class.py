# fraction_class.py
# This program demonstrates dunder (magic) methods:
# __str__, __add__, __eq__, and __lt__

import math


class Fraction:
    def __init__(self, numerator: int, denominator: int):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero")

        self.numerator = numerator
        self.denominator = denominator

    def simplify(self):
        """Returns a simplified fraction."""
        gcd = math.gcd(self.numerator, self.denominator)

        return Fraction(
            self.numerator // gcd,
            self.denominator // gcd
        )

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, other):
        new_num = (
            self.numerator * other.denominator
            + other.numerator * self.denominator
        )

        new_den = self.denominator * other.denominator

        result = Fraction(new_num, new_den)
        return result.simplify()

    def __eq__(self, other):
        f1 = self.simplify()
        f2 = other.simplify()

        return (
            f1.numerator == f2.numerator
            and f1.denominator == f2.denominator
        )

    def __lt__(self, other):
        return (
            self.numerator * other.denominator
            < other.numerator * self.denominator
        )


# Test Pair 1
f1 = Fraction(1, 2)
f2 = Fraction(1, 4)

print("Pair 1:")
print("f1 =", f1)
print("f2 =", f2)
print("Addition:", f1 + f2)
print("Equal?", f1 == f2)
print("f1 < f2 ?", f1 < f2)


# Test Pair 2
f3 = Fraction(2, 4)
f4 = Fraction(1, 2)

print("\nPair 2:")
print("f3 =", f3)
print("f4 =", f4)
print("Addition:", f3 + f4)
print("Equal?", f3 == f4)
print("f3 < f4 ?", f3 < f4)


# Test Pair 3
f5 = Fraction(3, 5)
f6 = Fraction(4, 5)

print("\nPair 3:")
print("f5 =", f5)
print("f6 =", f6)
print("Addition:", f5 + f6)
print("Equal?", f5 == f6)
print("f5 < f6 ?", f5 < f6)


# Explore:
# @functools.total_ordering can automatically generate
# the remaining comparison methods if we define __eq__
# and one comparison method like __lt__.
# This reduces the amount of code needed.