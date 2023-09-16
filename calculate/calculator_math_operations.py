from calculator_errors import ZeroDivisionError,OverflowError
from main import checking_for_an_integer


class CalculatorMathOperations:
    def __init__(self, calculator_logic, calculator_ui):
        self.calculator_logic = calculator_logic
        self.calculator_ui = calculator_ui
        self.MAX_VALUE = 1e100

    def substitution_arithmetic_operations(self, key):
        if self.calculator_logic.math_operation:
            if self.calculator_logic.equally:
                self.calculator_logic.num['A'] = self.calculator_ui.text_entry_widget_calc.get()
                self.calculator_ui.text_label_widget_calc.set(str(self.calculator_logic.num['A']) + key)
                self.calculator_logic.equally = False
                self.calculator_logic.num['B'] = ""
            else:
                self.calculator_ui.text_label_widget_calc.set(str(self.calculator_logic.num['A']) + key)
        elif not self.calculator_logic.math_operation:
            if self.calculator_ui.text_label_widget_calc.get() == "":
                self.calculator_logic.num['A'] = self.calculator_ui.text_entry_widget_calc.get()
                self.calculator_ui.text_label_widget_calc.set(self.calculator_logic.num['A'] + key)
                self.calculator_logic.math_operation = True
            elif self.calculator_ui.text_label_widget_calc.get()[-1] in "+-*/":
                try:
                    result=eval(
                        self.calculator_ui.text_label_widget_calc.get()
                        + self.calculator_ui.text_entry_widget_calc.get())
                    if abs(result)>self.MAX_VALUE:
                        raise OverflowError
                except ZeroDivisionError as e:
                    self.calculator_logic.show_error_message(str(e))
                    return
                except OverflowError as e:
                    self.calculator_logic.show_error_message(str(e))
                    return

                self.calculator_logic.num['A'] = eval(
                    self.calculator_ui.text_label_widget_calc.get() + self.calculator_ui.text_entry_widget_calc.get())
                self.calculator_ui.text_label_widget_calc.set(str(self.calculator_logic.num['A']) + key)
                self.calculator_ui.text_entry_widget_calc.set(checking_for_an_integer(self.calculator_logic.num['A']))
                self.calculator_logic.math_operation = True
            elif self.calculator_logic.equally:
                self.calculator_logic.num['A'], self.calculator_logic.num[
                    'B'] = self.calculator_ui.text_entry_widget_calc.get(), ""
                self.calculator_logic.math_operation, self.calculator_logic.equally = True, False
                self.calculator_ui.text_label_widget_calc.set(self.calculator_ui.text_entry_widget_calc.get() + key)

    def equality_operation(self):
        if self.calculator_logic.num['A'] and self.calculator_logic.math_operation:
            if not self.calculator_logic.num['B']:
                self.calculator_logic.num['B'] = self.calculator_ui.text_entry_widget_calc.get()
                self.calculator_ui.text_label_widget_calc.set(
                    self.calculator_ui.text_label_widget_calc.get() + str(self.calculator_logic.num['B']) + "=")
            else:
                self.calculator_ui.text_label_widget_calc.set(
                    self.calculator_ui.text_label_widget_calc.get().replace(str(self.calculator_logic.num['A']),
                                                                            self.calculator_ui.text_entry_widget_calc.get(),
                                                                            1))
            self.calculator_logic.num['A'] = self.calculator_ui.text_entry_widget_calc.get()
            try:
                result = eval(self.calculator_ui.text_label_widget_calc.get()[:-1])
                if abs(result) > self.MAX_VALUE:
                    raise OverflowError
            except ZeroDivisionError as e:
                self.calculator_logic.show_error_message(str(e))
                return
            except OverflowError as e:
                self.calculator_logic.show_error_message(str(e))
                return
            self.calculator_ui.text_entry_widget_calc.set(
                checking_for_an_integer(eval(self.calculator_ui.text_label_widget_calc.get()[:-1])))
            self.calculator_logic.equally = True
        elif not self.calculator_logic.math_operation and self.calculator_logic.equally:
            self.calculator_logic.math_operation = True
            self.equality_operation()
        elif not self.calculator_logic.math_operation:
            self.calculator_logic.num['B'] = self.calculator_ui.text_entry_widget_calc.get()
            self.calculator_ui.text_label_widget_calc.set(
                self.calculator_ui.text_label_widget_calc.get() + self.calculator_logic.num['B'] + "=")
            try:
                result=eval(self.calculator_ui.text_label_widget_calc.get()[:-1])
                if abs(result) > self.MAX_VALUE:
                    raise OverflowError
            except ZeroDivisionError as e:
                self.calculator_logic.show_error_message(str(e))
                return
            except OverflowError as e:
                self.calculator_logic.show_error_message(str(e))
                return
            self.calculator_ui.text_entry_widget_calc.set(
                checking_for_an_integer(eval(self.calculator_ui.text_label_widget_calc.get()[:-1])))
            self.calculator_logic.equally = True