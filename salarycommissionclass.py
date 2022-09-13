from salaryclass import CommissionEmployee
from decimal import Decimal

class SalariedCommissionEmployee(CommissionEmployee):
    """Работник, получающий зарплату и комиссионные,
    вычисляемые как процент от продаж."""

    def __init__(self, first_name, last_name, ssn,
        gross_sales, commission_rate, base_salary):
        """Инициализирует атрибуты SalariedCommissionEmployee."""
        super().__init__(first_name, last_name, ssn,
                        gross_sales, commission_rate)
        self.base_salary = base_salary # validate via property

    @property
    def base_salary(self):
        return self._base_salary

    @base_salary.setter
    def base_salary(self, salary):
        """Задает базовую зарплату или выдает ошибку ValueError."""
        if salary < Decimal('0.00'):
            raise ValueError('Base salary must be >= to 0')

        self._base_salary = salary

    def earnings(self):
        """Вычисляем доход."""
        return super().earnings() + self.base_salary

    def __repr__(self):
        """Возвращает строковое представление для repr()."""
        return ('Salaried' + super().__repr__() +
                f'\nbase salary: {self.base_salary:.2f}')