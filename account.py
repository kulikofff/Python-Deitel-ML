from decimal import Decimal
class Account:
    """Класс Account для ведения банковского счета."""
    def __init__(self, name, balance):
        """Инициализация объекта Account."""
        # Если balance меньше 0.00, выдать исключение
        if balance < Decimal('0.00'):
            raise ValueError('Initial balance must be >= to 0.00.')

        self.name = name
        self.balance = balance


    def deposit(self, amount):
        """Внесение средств на счет."""

        # Если amount меньше 0.00, выдать исключение
        if amount < Decimal('0.00'):
            raise ValueError('amount must be positive.')

        self.balance += amount