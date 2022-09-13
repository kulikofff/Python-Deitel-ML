from decimal import Decimal

class CommissionEmployee:
    """Сотрудник, получающий процент от продаж."""

    def __init__(self, first_name, last_name, ssn, gross_sales, commission_rate):
        """Инициализирует атрибуты CommissionEmployee."""
        self._first_name = first_name
        self._last_name = last_name
        self._ssn = ssn
        self.gross_sales = gross_sales # Проверка через свойство
        self.commission_rate = commission_rate # Проверка через свойство 
          

    def __repr__(self):
        """Возвращает строковое представление для repr()."""
        return ('CommissionEmployee: ' +
            f'{self.first_name} {self.last_name}\n' +
            f'social security number: {self.ssn}\n' +
            f'gross sales: {self.gross_sales:.2f}\n' +
            f'commission rate: {self.commission_rate:.2f}')

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    @property
    def ssn(self):
        return self._ssn

    @property
    def gross_sales(self):
        return self._gross_sales

    @gross_sales.setter
    def gross_sales(self, sales):
        """Задает объем продаж или выдает ошибку ValueError."""
        if sales < Decimal('0.00'):
            raise ValueError('Gross sales must be >= to 0')

        self._gross_sales = sales


    @property
    def commission_rate(self):
        return self._commission_rate

    @commission_rate.setter
    def commission_rate(self, rate):
        """Задает комиссионную ставку или выдает ошибку ValueError."""
        if not (Decimal('0.0') < rate < Decimal('1.0')):
            raise ValueError('Interest rate must be greater than 0 and less than 1')

        self._commission_rate = rate

    def earnings(self):
        """Вычисляет заработок."""
        return self.gross_sales * self.commission_rate

    def buy(self):
        return 'Вы бы побольше зарабатывали конечно:)'


'''
#Запрос из другого файла
from  salaryclass import CommissionEmployee
from decimal import Decimal

c = CommissionEmployee('Sue', 'Jones', '333-33-3333', Decimal('10000.00'), Decimal('0.06'))
print(c)
print(f'Ваш заработок {c.earnings()}')
print(c.buy())

#С подклассом:
from salaryclass import CommissionEmployee
from salarycommissionclass import SalariedCommissionEmployee
from decimal import Decimal

c = CommissionEmployee('Sue', 'Jones', '333-33-3333', Decimal('10000.00'), Decimal('0.06'))
print(c)
print(f'Ваш заработок {c.earnings()}')
print(c.buy())

b = SalariedCommissionEmployee('Sue', 'Jones', '333-33-3333', Decimal('10000.00'), Decimal('0.06'), Decimal('100000.00'))
print(b)
print(f'Ваш заработок {b.earnings()}')
print(b.buy())

'''
