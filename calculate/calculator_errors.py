class Error(Exception):
    """Базовый класс для других исключений"""
    pass


class ZeroDivisionError(Error):
    def __init__(self):
        self.message = "Ошибка деления на ноль"
        super().__init__(self.message)


class OverflowError(Error):
    def __init__(self):
        self.message = "Ошибка переполнения"
        super().__init__(self.message)
