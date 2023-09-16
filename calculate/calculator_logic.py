from calculator_math_operations import CalculatorMathOperations


class CalculatorLogic:
    def __init__(self, calculator_ui):
        self.calculator_ui = calculator_ui
        self.num = {'A': "", 'B': ""}
        self.math_operation = False
        self.equally = False
        self.error = False
        self.calculator_math_operations = CalculatorMathOperations(self, self.calculator_ui)

    def enter_numbers(self, key):
        if self.equally:
            self.calculator_ui.text_label_widget_calc.set("")
            self.calculator_ui.text_entry_widget_calc.set(key)
            self.num['A'], self.num['B'], self.equally, self.math_operation = "", "", False, False
        elif self.math_operation:
            self.math_operation = False
            self.calculator_ui.text_entry_widget_calc.set(key)
        elif self.calculator_ui.text_entry_widget_calc.get() == "0":
            self.calculator_ui.text_entry_widget_calc.set(key)
        else:
            self.calculator_ui.text_entry_widget_calc.set(self.calculator_ui.text_entry_widget_calc.get() + key)

    def clean(self):
        self.calculator_ui.text_entry_widget_calc.set("0")
        self.calculator_ui.text_label_widget_calc.set("")
        self.num['A'], self.num['B'], self.math_operation, self.equally = "", "", False, False

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
            self.num['A'] = self.calculator_ui.text_entry_widget_calc.get()
            self.num['B'] = ""
        else:
            self.calculator_ui.text_entry_widget_calc.set(
                self.calculator_ui.text_entry_widget_calc.get()[:-1] if len(
                    self.calculator_ui.text_entry_widget_calc.get()) != 1 else "0")

    def processing_operation(self, key):
        if self.error:
            self.clean()
            self.error = False
        operations = {
            'C': self.clean,
            'CE': self.clean_expression,
            '±': self.sign_change,
            '.': self.decimal_point,
            '⌫': self.delete_symbol,
            '=': self.calculator_math_operations.equality_operation
        }
        if key.isdigit():
            self.enter_numbers(key)
        elif key in "+-*/":
            self.calculator_math_operations.substitution_arithmetic_operations(key)
        elif key in operations:
            operations[key]()

    def show_error_message(self, error_message):
        self.clean()
        self.error = True
        self.calculator_ui.text_entry_widget_calc.set(error_message)
        self.calculator_ui.text_label_widget_calc.set("")
