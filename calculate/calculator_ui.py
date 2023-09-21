from functools import partial
from tkinter import *

from calculator_logic import CalculatorLogic


class CalculatorUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("443x385")
        self.root.resizable(0, 0)
        self.root.configure(background="#f3f3f3")
        self.calculator_logic = CalculatorLogic(self)
        self.root.bind("<Key>", self.handle_keypress)
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

    def handle_keypress(self, event):
        arithmetic_dictionary = {"Delete": "CE", "Escape": "C", "asterisk": "*",
                                 "BackSpace": "⌫", "slash": "/", "plus": "+",
                                 "minus": "-", "period": ".", "Return": "=", "equal": "="}
        key = event.keysym
        if arithmetic_dictionary.get(key) or key.isdigit():
            self.button_click(arithmetic_dictionary.get(key, key))
        else:
            return
