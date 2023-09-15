from functools import partial
from tkinter import *


def checking_for_an_integer(c):
    return int(c) if c == float(int(c)) else c


class CalculatorUI:
    def __init__(self, root):

        self.root = root
        self.root.title("Calculator")
        self.root.geometry("443x405")
        self.root.resizable(0, 0)
        self.root.configure(background="#f3f3f3")
        self.calculator_logic = CalculatorLogic(self)
        self.create_interface()

    def create_interface(self):
        self.text_entry_widget_calc = StringVar(self.root, "0")
        entry_widget_calc = Entry(self.root, textvariable=self.text_entry_widget_calc, justify=RIGHT,
                                  selectbackground="#f3f3f3", font="Segoe 15 bold", selectforeground="#000000",
                                  readonlybackground="#f3f3f3", relief=FLAT, state="readonly")
        entry_widget_calc.pack(pady=5, anchor=N, padx=6, fill=X)

        self.text_label_widget_calc = StringVar(self.root, "")
        calculated_lbl = Label(self.root, textvariable=self.text_label_widget_calc, anchor=E, bg="#f3f3f3",
                               relief=FLAT, bd=0, font="Segoe 9 bold")
        calculated_lbl.pack(pady=0, anchor=N, padx=6, fill=X)
        button_styles = {
            "numbers": {"bg": "#FFFFFF", "foreground": "#010100", "font": "Calibri 15", "width": 10, "height": 2},
            "operators": {"bg": "#f9f9f9", "foreground": "#010100", "font": "Calibri 15", "width": 10, "height": 2},
            "equals": {"bg": "#363533", "foreground": "#ffffff", "font": "Calibri 15", "width": 10, "height": 2}
        }
        buttons = [["CE", "C", "*", "⌫"],
                   ["7", "8", "9", "/"],
                   ["4", "5", "6", "+"],
                   ["1", "2", "3", "-"],
                   ["±", "0", ".", "="]]
        for i in range(5):
            frame = Frame(self.root, bg="#f3f3f3")
            for j in range(4):
                key = buttons[i][j]
                style = button_styles["numbers"] if key.isdigit() else (
                    button_styles["equals"] if key == "=" else button_styles["operators"]
                )
                button = Button(master=frame,
                                text=key,
                                relief=FLAT,
                                bd=0,
                                padx=1, **style)
                button.pack(side=LEFT, padx=1, pady=1, fill=BOTH)
                button.configure(command=partial(self.button_click, key))
            frame.pack(side=TOP, anchor=NW, padx=5, fill=BOTH)

    def button_click(self, key):
        self.calculator_logic.processing_operation(key)


class CalculatorLogic:
    def __init__(self, calculator_ui,):
        self.calculator_ui = calculator_ui
        self.num_A = ""
        self.num_B = ""
        self.math_operation = False
        self.equally = False
        self.error=False

    def enter_numbers(self, key):
        if self.equally:
            self.calculator_ui.text_label_widget_calc.set("")
            self.calculator_ui.text_entry_widget_calc.set(key)
            self.num_A, self.num_B, self.equally, self.math_operation = "", "", False, False
        elif self.math_operation:
            self.math_operation = False
            self.calculator_ui.text_entry_widget_calc.set(key)
        elif self.calculator_ui.text_entry_widget_calc.get() == "0":
            self.calculator_ui.text_entry_widget_calc.set(key)
        else:
            self.calculator_ui.text_entry_widget_calc.set(self.calculator_ui.text_entry_widget_calc.get() + key)

    def substitution_arithmetic_operations(self, key):
        if self.math_operation:
            if self.equally:
                self.num_A = self.calculator_ui.text_entry_widget_calc.get()
                self.calculator_ui.text_label_widget_calc.set(str(self.num_A) + key)
                self.equally = False
                self.num_B = ""
            else:
                self.calculator_ui.text_label_widget_calc.set(str(self.num_A) + key)

        elif not self.math_operation:
            if self.calculator_ui.text_label_widget_calc.get() == "":
                self.num_A = self.calculator_ui.text_entry_widget_calc.get()
                self.calculator_ui.text_label_widget_calc.set(self.num_A + key)
                self.math_operation = True
            elif self.calculator_ui.text_label_widget_calc.get()[-1] in "+-*/":
                try:
                    eval(
                        self.calculator_ui.text_label_widget_calc.get() + self.calculator_ui.text_entry_widget_calc.get())
                except ZeroDivisionError as e:
                    error_message = "Ошибка деления на ноль: " + str(e)
                    self.show_error_message(error_message)
                    return


                self.num_A = eval(
                    self.calculator_ui.text_label_widget_calc.get() + self.calculator_ui.text_entry_widget_calc.get())
                self.calculator_ui.text_label_widget_calc.set(str(self.num_A) + key)
                self.calculator_ui.text_entry_widget_calc.set(checking_for_an_integer(self.num_A))
                self.math_operation = True
            elif self.equally:
                self.num_A, self.num_B = self.calculator_ui.text_entry_widget_calc.get(), ""
                self.math_operation, self.equally = True, False
                self.calculator_ui.text_label_widget_calc.set(self.calculator_ui.text_entry_widget_calc.get() + key)

    def equality_operation(self):
        if self.num_A and self.math_operation:
            if not self.num_B:
                self.num_B = self.calculator_ui.text_entry_widget_calc.get()
                self.calculator_ui.text_label_widget_calc.set(
                    self.calculator_ui.text_label_widget_calc.get() + str(self.num_B) + "=")
            else:
                self.calculator_ui.text_label_widget_calc.set(
                    self.calculator_ui.text_label_widget_calc.get().replace(str(self.num_A),
                                                                            self.calculator_ui.text_entry_widget_calc.get(),
                                                                            1))
            self.num_A = self.calculator_ui.text_entry_widget_calc.get()
            try:
                eval(self.calculator_ui.text_label_widget_calc.get()[:-1])
            except ZeroDivisionError as e:
                error_message = "Ошибка деления на ноль: " + str(e)
                self.show_error_message(error_message)
                return
            self.calculator_ui.text_entry_widget_calc.set(
                checking_for_an_integer(eval(self.calculator_ui.text_label_widget_calc.get()[:-1])))
            self.equally = True
        elif not self.math_operation and self.equally:
            self.math_operation = True
            self.equality_operation()
        elif not self.math_operation:
            self.num_B = self.calculator_ui.text_entry_widget_calc.get()
            self.calculator_ui.text_label_widget_calc.set(
                self.calculator_ui.text_label_widget_calc.get() + self.num_B + "=")
            try:
                eval(self.calculator_ui.text_label_widget_calc.get()[:-1])
            except ZeroDivisionError as e:
                error_message = "Ошибка деления на ноль: " + str(e)
                self.show_error_message(error_message)
                return

            self.calculator_ui.text_entry_widget_calc.set(
                checking_for_an_integer(eval(self.calculator_ui.text_label_widget_calc.get()[:-1])))
            self.equally = True

    def clean(self):
        self.calculator_ui.text_entry_widget_calc.set("0")
        self.calculator_ui.text_label_widget_calc.set("")
        self.num_A, self.num_B, self.math_operation, self.equally = "", "", False, False

    def clean_expression(self):
        self.calculator_ui.text_entry_widget_calc.set("0")

    def sign_change(self):
        if self.calculator_ui.text_entry_widget_calc.get() != "0":
            self.math_operation = False
            if self.calculator_ui.text_entry_widget_calc.get()[0] == "-":
                self.calculator_ui.text_entry_widget_calc.set(self.calculator_ui.text_entry_widget_calc.get()[1:])
            else:
                self.calculator_ui.text_entry_widget_calc.set("-" + self.calculator_ui.text_entry_widget_calc.get())

    def decimal_point(self):
        if self.math_operation:
            self.calculator_ui.text_entry_widget_calc.set("0.")
            self.math_operation = False
        elif self.equally and not self.math_operation:
            self.calculator_ui.text_entry_widget_calc.set("0.")
            self.calculator_ui.text_label_widget_calc.set("")
            self.equally = False
        elif "." not in self.calculator_ui.text_entry_widget_calc.get():
            self.calculator_ui.text_entry_widget_calc.set(self.calculator_ui.text_entry_widget_calc.get() + ".")

    def delete_symbol(self):
        if self.equally or self.math_operation:

            self.calculator_ui.text_label_widget_calc.set("")
            self.equally = False
            self.math_operation = False
            self.num_A = self.calculator_ui.text_entry_widget_calc.get()
            self.num_B = ""
        else:
            self.calculator_ui.text_entry_widget_calc.set(
                self.calculator_ui.text_entry_widget_calc.get()[:-1] if len(
                    self.calculator_ui.text_entry_widget_calc.get()) != 1 else "0")

    def processing_operation(self, key):
        if self.error==True:
            self.clean()
            self.error=False
        if key.isdigit():
            self.enter_numbers(key)
        elif key in "+-*/":
            self.substitution_arithmetic_operations(key)
        elif key == "=":
            self.equality_operation()
        elif key == "C":
            self.clean()
        elif key == "CE":
            self.clean_expression()
        elif key == "±":
            self.sign_change()
        elif key == ".":
            self.decimal_point()
        elif key == "⌫":
            self.delete_symbol()

    def show_error_message(self,error_message):
        self.clean()
        self.error = True
        self.calculator_ui.text_entry_widget_calc.set(error_message)
        self.calculator_ui.text_label_widget_calc.set("")


if __name__ == "__main__":
    root = Tk()

    calc = CalculatorUI(root)
    root.mainloop()
