import tkinter
from tkinter import ttk
from tkinter import *


class Calculator:
    def __init__(self, root):
        self.main_window = root
        self.buttons = [["CE", "C", "*", "⌫"],
                        ["7", "8", "9", "/"],
                        ["4", "5", "6", "+"],
                        ["1", "2", "3", "-"],
                        ["±", "0", ",", "="]]
        self.text_entry_widget_calc = StringVar(root, "0")
        self.text_label_widget_calc = StringVar(root, "0")
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
        for i in range(5):
            frame = \
                Frame(self.main_window, bg="#f3f3f3")
            for j in range(4):
                if self.buttons[i][j] in "1234567890":
                    bg = "#FFFFFF"
                    fd = "#010100"
                elif self.buttons[i][j] in "=":
                    bg = "#363533"
                    fd = "#ffffff"
                else:
                    bg = "#f9f9f9"
                    fd = "#010100"
                Button(master=frame,
                       text=f"{self.buttons[i][j]}", command=lambda key=self.buttons[i][j]: self.entering_values(key),
                       font="Calibri 15", bg=bg, foreground=fd, width=10, height=2, relief=FLAT, bd=0, padx=1) \
                    .pack(side=LEFT, padx=1, pady=1, fill=BOTH)
            frame.pack(side=TOP, anchor=NW, padx=5, fill=BOTH)

    def entering_values(self, key):
        print(key)

        if key in "0123456789":
            if self.equally:
                self.text_label_widget_calc.set("")
                self.num_A, self.num_B, self.math_operation = "", "", False
                self.equally = False
                self.text_entry_widget_calc.set(key)
                return
            if self.math_operation:
                self.math_operation = False
                self.text_entry_widget_calc.set(key)
                return
            if self.text_entry_widget_calc.get() == "0":
                if key == "0":
                    return
                else:
                    self.text_entry_widget_calc.set(key)
            else:
                self.text_entry_widget_calc.set(self.text_entry_widget_calc.get() + key)

        elif key in "+-*/":

            if not self.math_operation:
                if self.text_label_widget_calc.get() == "":
                    self.text_label_widget_calc.set(self.text_entry_widget_calc.get() + key)
                    self.num_A = self.text_entry_widget_calc.get()
                    self.math_operation = True
                    return
                last_symbol = self.text_label_widget_calc.get()[-1]
                if last_symbol in "+-*/":
                    if last_symbol == "/" and self.text_entry_widget_calc.get() == "0":
                        self.text_entry_widget_calc.set("Деление на ноль невозможно")
                        return
                    self.num_A = eval(self.text_label_widget_calc.get() + self.text_entry_widget_calc.get())
                    self.text_label_widget_calc.set(str(self.num_A) + key)
                    self.text_entry_widget_calc.set(self.num_A)
                if self.equally:
                    self.text_label_widget_calc.set(self.text_entry_widget_calc.get() + key)
                    self.num_A = self.text_entry_widget_calc.get()
                    self.equally = False
                    return
                else:
                    self.text_label_widget_calc.set(self.text_entry_widget_calc.get() + key)
                    self.num_A = self.text_entry_widget_calc.get()
                self.math_operation = True
            else:
                if self.equally:
                    self.num_A = self.text_entry_widget_calc.get()
                    self.text_label_widget_calc.set(self.text_entry_widget_calc.get() + key)
                    self.math_operation = True
                    self.equally = False
                    return
                self.text_label_widget_calc.set(str(self.num_A) + key)

            if self.text_entry_widget_calc.get() == "-0.0" or self.text_entry_widget_calc.get() == "0.0":
                self.text_entry_widget_calc.set("0")
                self.text_label_widget_calc.set("0" + key)
                self.num_A = "0"

        elif key == "⌫":
            if self.equally:
                self.text_label_widget_calc.set("")
                self.equally = False
                return
            if len(self.text_entry_widget_calc.get()) != 1:
                self.text_entry_widget_calc.set(self.text_entry_widget_calc.get()[:-1])
            else:
                self.text_entry_widget_calc.set("0")

        elif key == "±":
            if self.text_entry_widget_calc.get() != "0":
                self.math_operation = False
                if self.text_entry_widget_calc.get()[0] == "-":
                    self.text_entry_widget_calc.set(self.text_entry_widget_calc.get()[1:])
                else:
                    self.text_entry_widget_calc.set("-" + self.text_entry_widget_calc.get())
        elif key == "C":
            self.text_entry_widget_calc.set("0")
            self.text_label_widget_calc.set("")
            self.num_A, self.num_B, self.math_operation = "", "", False
        elif key == "CE":
            self.text_entry_widget_calc.set("0")
        elif key == "=":
            if self.math_operation:
                if self.equally:

                    self.text_label_widget_calc.set(
                        self.text_entry_widget_calc.get() + self.text_label_widget_calc.get().replace(self.num_A, "",
                                                                                                      1))
                    self.num_A = self.text_entry_widget_calc.get()
                    self.text_entry_widget_calc.set(eval(self.text_label_widget_calc.get()[:-1]))
                    self.equally = True
                    return
                else:
                    self.num_B = self.text_entry_widget_calc.get()
                    self.text_label_widget_calc.set(self.text_label_widget_calc.get() + self.num_B + "=")
                    self.text_entry_widget_calc.set(eval(self.text_label_widget_calc.get()[:-1]))
                    self.equally = True
                    return

                self.num_B = self.num_A
                self.text_label_widget_calc.set(self.text_label_widget_calc.get() + self.num_B + "=")
                self.text_entry_widget_calc.set(eval(self.text_label_widget_calc.get()[:-1]))
                self.equally = True
            else:
                self.num_B = self.text_entry_widget_calc.get()
                self.text_label_widget_calc.set(self.text_label_widget_calc.get() + self.num_B + "=")
                self.text_entry_widget_calc.set(eval(self.text_label_widget_calc.get()[:-1]))
                self.equally = True


if __name__ == "__main__":
    root = tkinter.Tk()
    root.title("Calculator")
    root.geometry("443x405")
    root.resizable(0, 0)
    root.configure(background="#f3f3f3")

    calc = Calculator(root)
    root.mainloop()
