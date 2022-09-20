"""Класс данных Card с атрибутами класса, атрибутами данных,
автоматически сгенерированными и явно определенными методами."""
from dataclasses import dataclass
from typing import ClassVar, List


#Декоратор показывает, что класс - класс данных
@dataclass
class Card:
    FACES: ClassVar[List[str]] = ['Ace', '2', '3', '4', '5', '6', '7', 
                                  '8', '9', '10', 'Jack', 'Queen', 'King']
    SUITS: ClassVar[List[str]] = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

    face: str
    suit: str

    @property
    def image_name(self):
        """Возвращает имя файла с изображением карты."""
        return str(self).replace(' ', '_') + '.png'

    def __str__(self):
        """Возвращает строковое представление для str()."""
        return f'{self.face} of {self.suit}'

    def __format__(self, format):
        """Возвращает отформатированное строковое представление."""
        return f'{str(self):{format}}'

