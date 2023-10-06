from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label


def checking_for_an_integer(c):
    return int(c) if c == float(int(c)) else c


class CalculatorUI(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.width = 385
        self.height = 443

    def build(self):
        from CalculatorLogic import CalculatorLogic
        Config.set('graphics', 'resizable', 0)
        Config.set('graphics', 'width', self.width)
        Config.set('graphics', 'height', self.height)
        self.logic = CalculatorLogic(self)
        buttons = [["CE", "C", "*", "⌫"],
                   ["7", "8", "9", "/"],
                   ["4", "5", "6", "+"],
                   ["1", "2", "3", "-"],
                   ["±", "0", ".", "="]]
        box = BoxLayout(orientation='vertical', padding=3, spacing=0)
        self.text_entry_widget_calc = Label(text="0", font_size=40, size_hint_y=None, halign="right", valign="center",
                                            size_hint=(1, .4), text_size=(self.width + 50, self.height))
        box.add_widget(self.text_entry_widget_calc)
        self.text_label_widget_calc = Label(text="", font_size=40, size_hint_y=None, halign="right", valign="center",
                                            size_hint=(1, .4), text_size=(self.width + 50, self.height))
        box.add_widget(self.text_label_widget_calc)
        grid = GridLayout(cols=4, spacing=3)

        for i in range(5):
            for j in range(4):
                button = Button(text=f"{buttons[i][j]}")
                button.bind(on_press=self.logic.processing_operation)
                grid.add_widget(button)
        box.add_widget(grid)

        return box


if __name__ == "__main__":
    CalculatorUI().run()
