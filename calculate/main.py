from tkinter import *


def checking_for_an_integer(c):
    return int(c) if c == float(int(c)) else c


if __name__ == "__main__":
    root = Tk()
    from calculator_ui import CalculatorUI
    calc = CalculatorUI(root)
    root.mainloop()
