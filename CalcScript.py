'''

                 Calc 2.1 can do all the functions Calc 2 can do, but also Trig and last num equations
                                             This part is the main script
                                             Was other part of my OOP version of calc

'''


from Calc.CalcCore import *

while True:
    op = int(input("        [Addition] [Subtraction] [Multiplication] [Division]\n"
                   "            0            1               2             3\n"
                   "    [Exponent] [Square Root] [Squared] [Sine] [Cosine] \n"
                   "        4            5           6       7        8\n"
                   "[Tangent] [Quadratic Factoring] [Synthetic Division] [Last Num]\n"
                   "    9               10                    11             12\n"
                   ">: "))
    if op <= 4:
        calc = SimpleCalcCore(op, float(input("Enter first num: ")), float(input("Enter second num: ")))
        print(calc.solve())
    elif 5 <= op <= 6:
        calc = SimplerCalcCore(op, float(input("Enter num: ")))
        print(calc.solve())
    elif op == 10:
        calc = SimpleRootCore(op, float(input("Enter first num: ")), float(input("Enter second num: ")),
                              float(input("Enter third num: ")))
        print(calc.solve())
    elif op == 11:
        top_power = int(input("Enter highest power in equation: "))
        nums = []
        for i in range(top_power):
            nums.append(float(input("Num: ")))
        calc = SyntheticDivCore(op, float(input("Enter divisor: ")), top_power, nums)
        print(calc.solve())
    elif 7 <= op <= 9:
        calc = TrigCore(op, float(input("Enter number: ")), float(input("Enter multiplier: ")))
        print(calc.solve())
    elif op == 12:
        if calc.solve() == float:
            try:
                last_num = calc.solve()
                new_op = int(input("  [Addition] [Subtraction] [Multiplication] [Division]\n"
                                   "      0            1               2             3\n"
                                   "[Exponent] [Square Root] [Squared] [Sine] [Cosine] [Tangent] \n"
                                   "     4           5           6       7        8        9\n"
                                   "                            [Back]\n"
                                   "                              10\n"
                                   ">: "))
                if new_op <= 4:
                    calc = SimpleCalcCore(new_op, last_num, float(input("Enter number: ")))
                    print(calc.solve())
                elif 5 <= new_op <= 6:
                    calc = SimplerCalcCore(new_op, last_num)
                    print(calc.solve())
                elif 7 <= new_op <= 9:
                    calc = TrigCore(new_op, last_num, float(input("Enter multiplier: ")))
                elif new_op == 10:
                    pass
                else:
                    print("Error: Not a listed operator")
            except NameError:
                print("There is no last number")
        else:
            print("Last answer is not a single number")
    elif op == 13:
        print(last_num)
    else:
        print("Error: Not a listed operator")


