
#Type the first number, the math symbol, and the last number, pressing enter after each


import keyboard
import tkinter


top = tkinter.Tk()


def addition():
    num_sum = x + y
    return num_sum


def division():
    dividend = x / y
    return dividend


def multiplication():
    product = x * y
    return product


def subtraction():
    difference = x - y
    return difference


def exponent():
    exponential = x ** y
    return exponential


def square_root():
    sqart = x ** .5
    return sqart


top.mainloop()
while True:
    try:
        if keyboard.is_pressed('ctrl'):
            break
        else:
            print("Function?: ")
            func = input("")
            x = float(input('1st: '))
            if func != "square root":
                y = float(input('2nd: '))
            if func == "addition":
                print(addition())
            elif func == "subtraction":
                print(subtraction())
            elif func == "multiplication":
                print(multiplication())
            elif func == "division":
                print(division())
            elif func == "exponent":
                print(exponent())
            elif func == "square root":
                print(square_root())
    except Exception as e:
        break


