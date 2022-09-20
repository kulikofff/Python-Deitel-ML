#from complexnumber import Complex

#import cmath

#x = complex(2, 4)
#y = complex(2, -1)

#print(x+y)

#x += y
#print(x)
#print(y)

#Реализация

class complexx:
    """Класс Complex, представляющий комплексное число
    с действительной и мнимой частью."""
    
    def __init__(self, real, imaginary):
        """Инициализирует атрибуты класса Complex."""
        self.real = real
        self.imaginary = imaginary

    def __add__(self, right):
        """Переопределяет оператор +."""
        return complexx(self.real + right.real, 
                       self.imaginary + right.imaginary)

    def __iadd__(self, right):
        """Перегружает оператор +=."""
        self.real += right.real
        self.imaginary += right.imaginary
        return self

    def __repr__(self):
        """Возвращает строковое представление для repr()."""
        return (f'({self.real} ' + 
                ('+' if self.imaginary >= 0 else '-') +
                f' {abs(self.imaginary)}i)' ' ->> всего доброго')



x1 = complexx(2, 4)
y1 = complexx(2, -1)
y2 = complexx(8, -8)

print(x1+y1+y2)