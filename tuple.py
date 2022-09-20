from collections import namedtuple

Card = namedtuple('Card', ['face', 'suit'])
card = Card(face='Ace', suit='Spades')
print(card, card.face, card.suit)

values = ['Queen', 'Hearts']
card = Card._make(values)
print(card)

print(card._asdict())