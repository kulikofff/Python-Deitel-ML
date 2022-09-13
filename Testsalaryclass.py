from salaryclass import CommissionEmployee
from salarycommissionclass import SalariedCommissionEmployee
from decimal import Decimal

c = CommissionEmployee('Boby', 'Dealon', '222-22-22222', Decimal('104000.00'), Decimal('0.07'))
print(c)
print(f'Ваш заработок {c.earnings()}')
print(c.buy())
print()

b = SalariedCommissionEmployee('Sue', 'Jones', '333-33-3333', Decimal('10000.00'), Decimal('0.06'), Decimal('100000.00'))
print(b)
print(f'Ваш заработок {b.earnings()}')
print(b.buy())

print(issubclass(SalariedCommissionEmployee, CommissionEmployee))

print(isinstance(c, CommissionEmployee))

employees = [c, b]
for i in employees:
    print(i)