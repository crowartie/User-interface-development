from tkinter import *


def checking_for_an_integer(c):
    return int(c) if c == float(int(c)) else c


class Calculator:
    def __init__(self, root):
        self.main_window = root
        self.buttons = [["CE", "C", "*", "⌫"],
                        ["7", "8", "9", "/"],
                        ["4", "5", "6", "+"],
                        ["1", "2", "3", "-"],
                        ["±", "0", ".", "="]]
        self.text_entry_widget_calc = StringVar(root, "0")
        self.text_label_widget_calc = StringVar(root, "")
        self.create_interface()
        self.num_A = ""
        self.num_B = ""
        self.math_operation = False
        self.equally = False

    def create_interface(self):
        entry_widget_calc = Entry(self.main_window, textvariable=self.text_entry_widget_calc, justify=RIGHT,
                                     selectbackground="#f3f3f3", font="Segoe 15 bold", selectforeground="#000000",
                                     readonlybackground="#f3f3f3", relief=FLAT, state="readonly")
        entry_widget_calc.pack(pady=5, anchor=N, padx=6, fill=X)
        calculated_lbl = Label(self.main_window, textvariable=self.text_label_widget_calc, anchor=E, bg="#f3f3f3",
                                  relief=FLAT, bd=0, font="Segoe 9 bold")
        calculated_lbl.pack(pady=0, anchor=N, padx=6, fill=X)

        button_styles = {
            "numbers": {"bg": "#FFFFFF", "foreground": "#010100", "font": "Calibri 15", "width": 10, "height": 2},
            "operators": {"bg": "#f9f9f9", "foreground": "#010100", "font": "Calibri 15", "width": 10, "height": 2},
            "equals": {"bg": "#363533", "foreground": "#ffffff", "font": "Calibri 15", "width": 10, "height": 2}
        }

        for i in range(5):
            frame = Frame(self.main_window, bg="#f3f3f3")
            for j in range(4):
                key = self.buttons[i][j]
                style = button_styles["numbers"] if key.isdigit() else (
                    button_styles["equals"] if key == "=" else button_styles["operators"]
                )

                Button(master=frame, text=key, command=lambda k=key: self.entering_values(k), relief=FLAT, bd=0,
                          padx=1, **style).pack(side=LEFT, padx=1, pady=1, fill=BOTH)
            frame.pack(side=TOP, anchor=NW, padx=5, fill=BOTH)

    def enter_numbers(self, key):
        if self.equally:
            self.text_label_widget_calc.set("")
            self.text_entry_widget_calc.set(key)
            self.num_A, self.num_B, self.equally, self.math_operation = "", "", False, False
        elif self.math_operation:
            self.math_operation = False
            self.text_entry_widget_calc.set(key)
        elif self.text_entry_widget_calc.get() == "0":
            self.text_entry_widget_calc.set(key)
        else:
            self.text_entry_widget_calc.set(self.text_entry_widget_calc.get() + key)

    def substitution_arithmetic_operations(self, key):
        if self.math_operation:

            if self.equally:
                self.num_A = self.text_entry_widget_calc.get()
                self.text_label_widget_calc.set(str(self.num_A) + key)
                self.equally = False
                self.num_B = ""
            else:
                self.text_label_widget_calc.set(str(self.num_A) + key)

        elif not self.math_operation:
            if self.text_label_widget_calc.get() == "":
                self.num_A = self.text_entry_widget_calc.get()
                self.text_label_widget_calc.set(self.num_A + key)
                self.math_operation = True
            elif self.text_label_widget_calc.get()[-1] in "+-*/":
                try:
                    eval(self.text_label_widget_calc.get() + self.text_entry_widget_calc.get())
                except ZeroDivisionError:
                    return self.clean()
                self.num_A = eval(self.text_label_widget_calc.get() + self.text_entry_widget_calc.get())
                self.text_label_widget_calc.set(str(self.num_A) + key)
                self.text_entry_widget_calc.set(checking_for_an_integer(self.num_A))
                self.math_operation = True
            elif self.equally:
                self.num_A, self.num_B = self.text_entry_widget_calc.get(), ""
                self.math_operation, self.equally = True, False
                self.text_label_widget_calc.set(self.text_entry_widget_calc.get() + key)

    def equality_operation(self):
        if self.num_A and self.math_operation:
            if not self.num_B:
                self.num_B = self.text_entry_widget_calc.get()
                self.text_label_widget_calc.set(self.text_label_widget_calc.get() + str(self.num_B) + "=")
            else:
                self.text_label_widget_calc.set(
                    self.text_label_widget_calc.get().replace(str(self.num_A), self.text_entry_widget_calc.get(), 1))
            self.num_A = self.text_entry_widget_calc.get()
            try:
                eval(self.text_label_widget_calc.get()[:-1])
            except ZeroDivisionError:
                return self.clean()
            self.text_entry_widget_calc.set(checking_for_an_integer(eval(self.text_label_widget_calc.get()[:-1])))
            self.equally = True
        elif not self.math_operation and self.equally:
            self.math_operation = True
            self.equality_operation()
        elif not self.math_operation:
            self.num_B = self.text_entry_widget_calc.get()
            self.text_label_widget_calc.set(self.text_label_widget_calc.get() + self.num_B + "=")
            try:
                eval(self.text_label_widget_calc.get()[:-1])
            except ZeroDivisionError:
                return self.clean()

            self.text_entry_widget_calc.set(checking_for_an_integer(eval(self.text_label_widget_calc.get()[:-1])))
            self.equally = True

    def clean(self):
        self.text_entry_widget_calc.set("0")
        self.text_label_widget_calc.set("")
        self.num_A, self.num_B, self.math_operation, self.equally = "", "", False, False

    def clean_expression(self):
        self.text_entry_widget_calc.set("0")

    def sign_change(self):
        if self.text_entry_widget_calc.get() != "0":
            self.math_operation = False
            if self.text_entry_widget_calc.get()[0] == "-":
                self.text_entry_widget_calc.set(self.text_entry_widget_calc.get()[1:])
            else:
                self.text_entry_widget_calc.set("-" + self.text_entry_widget_calc.get())

    def decimal_point(self):
        if self.math_operation:
            self.text_entry_widget_calc.set("0.")
            self.math_operation = False
        elif self.equally and not self.math_operation:
            self.text_entry_widget_calc.set("0.")
            self.text_label_widget_calc.set("")
            self.equally = False
        elif "." not in self.text_entry_widget_calc.get():
            self.text_entry_widget_calc.set(self.text_entry_widget_calc.get() + ".")

    def delete_symbol(self):
        if self.equally or self.math_operation:
            self.text_label_widget_calc.set("")
            self.equally = False
            self.math_operation = False
            self.num_A = self.text_entry_widget_calc.get()
            self.num_B = ""
        else:
            self.text_entry_widget_calc.set(
                self.text_entry_widget_calc.get()[:-1] if len(self.text_entry_widget_calc.get()) != 1 else "0")

    def entering_values(self, key):
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


if __name__ == "__main__":
    root = Tk()
    root.title("Calculator")
    root.geometry("443x405")
    root.resizable(0, 0)
    root.configure(background="#f3f3f3")
    calc = Calculator(root)
    root.mainloop()
