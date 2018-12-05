'''

                                    This part of Calc 2.1 does all the math
                                    Was my attempt at an OOP version of calc

'''


import math


class SimpleCalcCore:

    def __init__(self, operator, x, y):
        self.operator = operator
        self.x = x
        self.y = y

    def solve(self):
        if self.operator == 0:
            return self.x + self.y
        elif self.operator == 1:
            return self.x - self.y
        elif self.operator == 2:
            return self.x * self.y
        elif self.operator == 3:
            return self.x / self.y
        elif self.operator == 4:
            return self.x ** self.y


class SimplerCalcCore:

    def __init__(self, operator, x):
        self.operator = operator
        self.x = x

    def solve(self):
        if self.operator == 5:
            return self.x ** .5
        elif self.operator == 6:
            return self.x ** 2


class TrigCore:

    def __init__(self, operator, x, a):
        self.operator = operator
        self.x = x
        self.a = a

    def solve(self):
        if self.operator == 7:
            return self.a * (math.sin(self.x))
        elif self.operator == 8:
            return self.a * (math.cos(self.x))
        elif self.operator == 9:
            return self.a * (math.tan(self.x))


class SimpleRootCore:

    def __init__(self, operator, a, b, c):
        self.operator = operator
        self.a = a
        self.b = b
        self.c = c

    def solve(self):
        return ((-self.b) + ((self.b ** 2 - 4 * self.a * self.c) ** .5)) / (2 * self.a), \
               ((-self.b) - ((self.b ** 2 - 4 * self.a * self.c) ** .5)) / (2 * self.a)


class SyntheticDivCore:

    def __init__(self, operator, div, power, nums):
        self.operator = operator
        self.nums = nums
        self.div = div
        self.power = power

    def solve(self):
        fin_synthetic_equation = []
        for i in range(0, self.power):
            if i == 0:
                fin_synthetic_equation.append(self.nums[i])
                next_mult = self.nums[i] * self.div
            else:
                fin_synthetic_equation.append(self.nums[i] + next_mult)
                next_mult = fin_synthetic_equation[i] * self.div
        return fin_synthetic_equation


