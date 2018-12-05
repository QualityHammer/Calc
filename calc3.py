'''

            Previously known as guiTest2, Calc 3 now has a calculator interface to use instead of typing
            For now it can only add, subtract, multiply, and divide
            But it can take a much longer equation than previous Calcs

            Version 3.1

'''

import tkinter as tk

# Main window
root = tk.Tk()
root.title("Calculator 3.0.1 a1")
root.configure(background="black")

# All frames
top_frame = tk.Frame(root, height=4, width=42, background="black")
top_frame.pack(side=tk.LEFT)
bottom_frame = tk.Frame(root)
bottom_frame.pack(side=tk.BOTTOM)
frame = tk.Frame(top_frame, background="black")
frame.pack(side=tk.BOTTOM)
right_frame = tk.Frame(bottom_frame, background="black")
right_frame.pack(side=tk.RIGHT)

# Variables
inp_var = ""
equation = tk.StringVar()
total_num = tk.StringVar()

# Text boxes
inp = tk.Entry(top_frame, textvariable=equation, width=42)
inp.pack(side=tk.LEFT, padx=2, pady=2)
outp = tk.Label(top_frame, textvariable=total_num, width=31)
outp.pack(side=tk.LEFT, padx=3, pady=2)


# Functions
def press(num):
    global inp_var
    inp_var += str(num)
    equation.set(inp_var)


def equal_press():
    global inp_var
    try:
        total_num.set(str(eval(inp_var)))
    except SyntaxError:
        total_num.set("Syntax Error")
    equation.set("")
    inp_var = ""


def clear_press():
    global inp_var
    equation.set("")
    inp_var = ""


def all_clear_press():
    global inp_var
    equation.set("")
    total_num.set("")
    inp_var = ""


# Buttons
tk.Button(frame, text='1', height=17, width=14, command=lambda: press(1)).grid(row=0, column=0, padx=2, pady=2,
                                                                               rowspan=2)
tk.Button(frame, text='2', height=17, width=14, command=lambda: press(2)).grid(row=0, column=1, padx=2, pady=2,
                                                                               rowspan=2)
tk.Button(frame, text='3', height=17, width=14, command=lambda: press(3)).grid(row=0, column=2, padx=2, pady=2,
                                                                               rowspan=2)
tk.Button(frame, text='4', height=17, width=14, command=lambda: press(4)).grid(row=2, column=0, padx=2, pady=2,
                                                                               rowspan=2)
tk.Button(frame, text='5', height=17, width=14, command=lambda: press(5)).grid(row=2, column=1, padx=2, pady=2,
                                                                               rowspan=2)
tk.Button(frame, text='6', height=17, width=14, command=lambda: press(6)).grid(row=2, column=2, padx=2, pady=2,
                                                                               rowspan=2)
tk.Button(frame, text='7', height=17, width=14, command=lambda: press(7)).grid(row=4, column=0, padx=2, pady=2,
                                                                               rowspan=2)
tk.Button(frame, text='8', height=17, width=14, command=lambda: press(8)).grid(row=4, column=1, padx=2, pady=2,
                                                                               rowspan=2)
tk.Button(frame, text='9', height=17, width=14, command=lambda: press(9)).grid(row=4, column=2, padx=2, pady=2,
                                                                               rowspan=2)
tk.Button(frame, text="=", height=17, width=14, command=equal_press).grid(row=4, column=3, padx=2, pady=2, columnspan=2,
                                                                          rowspan=2)
tk.Button(frame, text="C", height=17, width=9, command=clear_press).grid(row=0, column=3, padx=2, pady=2, rowspan=2)
tk.Button(frame, text="AC", height=17, width=9, command=all_clear_press).grid(row=0, column=4, padx=2, pady=2,
                                                                              rowspan=2)
tk.Button(frame, text="+", height=8, width=9, command=lambda: press("+")).grid(row=2, column=3, pady=2, padx=2)
tk.Button(frame, text="-", height=8, width=9, command=lambda: press("-")).grid(row=2, column=4, pady=2, padx=2)
tk.Button(frame, text="*", height=8, width=9, command=lambda: press("*")).grid(row=3, column=3, pady=2, padx=2)
tk.Button(frame, text="/", height=8, width=9, command=lambda: press("/")).grid(row=3, column=4, pady=2, padx=2)
tk.Button(frame, text="Sin", height=8, width=9, command=lambda: press("math.sin(")).grid(row=0, column=5, pady=2,
                                                                                         padx=2)
tk.Button(frame, text="Cos", height=8, width=9, command=lambda: press("math.cos(")).grid(row=0, column=6, pady=2,
                                                                                         padx=2)
tk.Button(frame, text="Tan", height=8, width=9, command=lambda: press("math.tan(")).grid(row=1, column=5, pady=2,
                                                                                         padx=2)
tk.Button(frame, text=")", height=8, width=9, command=lambda: press(")")).grid(row=1, column=6, pady=2, padx=2)
tk.Button(frame, text="x^2", height=8, width=9, command=lambda: press("**2")).grid(row=2, column=5, pady=2, padx=2)
tk.Button(frame, text="Sqrt", height=8, width=9, command=lambda: press("**.5")).grid(row=2, column=6, pady=2, padx=2)
tk.Button(frame, text="x^y", height=8, width=9, command=lambda: press("pow(")).grid(row=3, column=5, pady=2, padx=2)
tk.Button(frame, text=",", height=8, width=9, command=lambda: press(",")).grid(row=3, column=6, pady=2, padx=2)


root.mainloop()
