'''

                     Simple Calculator 2.0 can do simple math equations and some quadratics

'''


def addition(x, y):
    return x + y


def subtraction(x, y):
    return x - y


def multiplication(x, y):
    return x * y


def division(x, y):
    return x / y


def exponent(x, y):
    return x ** y


def square_root(x):
    return x ** .5


def quad_equation_factor(a, b, c):
    return ((-b) + ((b ** 2 - 4 * a * c) ** .5)) / (2 * a), ((-b) - ((b ** 2 - 4 * a * c) ** .5)) / (2 * a)


def synthetic_division(div):
    synthetic_equation = []
    fin_synthetic_equation = []
    for i in range(0, power):
        synthetic_equation.append(float(input(":: ")))
    for i in range(0, power):
        if i == 0:
            fin_synthetic_equation.append(synthetic_equation[i])
            next_mult = synthetic_equation[i] * div
        else:
            fin_synthetic_equation.append(synthetic_equation[i] + next_mult)
            next_mult = fin_synthetic_equation[i] * div
    return fin_synthetic_equation


def simple_operators(op_num):
    try:
        first = float(input("First number: "))
        second = float(input("Second number: "))
        if op_num == 0:
            return addition(first, second)
        elif op_num == 1:
            return subtraction(first, second)
        elif op_num == 2:
            return multiplication(first, second)
        elif op_num == 3:
            return division(first, second)
        elif op_num == 4:
            return exponent(first, second)
    except ValueError:
        return "Not a real number."


def simpler_operators(op_num):
    try:
        num = float(input("Enter number: "))
        if op_num == 5:
            return square_root(num)
    except ValueError:
        return "Not a real number."


def factor_operators():
    try:
        first = float(input("First number: "))
        second = float(input("Second number: "))
        third = float(input("Third number: "))
        return quad_equation_factor(first, second, third)
    except ValueError:
        return "Not a real number."


while True:
    print("   [Addition] [Subtraction] [multiplication] [Division]\n"
          "    0            1               2             3\n"
          "[Exponent] [Square Root] [Quadratic factoring] [Last Num]\n"
          "    4            5                 6                7\n"
          "              [Synthetic Division] [Exit]\n"
          "                        8            9")
    try:
        op = int(input(":: "))
    except ValueError:
        continue
    if op <= 4:
        last_num = simple_operators(op)
        print(last_num)
    elif op == 5:
        last_num = simpler_operators(op)
        print(last_num)
    elif op == 6:
        last_num = factor_operators()
        print(last_num)
    elif op == 7:
        print("Not yet implemented :D")
        pass
    elif op == 8:
        try:
            power = int(input("Enter highest power of equation: "))
            divisor = float(input("Enter divisor: "))
            print("Enter each coefficient.")
            last_num = synthetic_division(divisor)
            print(last_num)
        except ValueError:
            pass
    elif op == 9:
        break
