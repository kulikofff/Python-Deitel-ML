from dataclass import Card

c1 = Card(Card.FACES[0], Card.SUITS[3])
print(c1, c1.face, c1.suit, c1.image_name)

c2 = Card(Card.FACES[0], Card.SUITS[3])
c3 = Card(Card.FACES[0], Card.SUITS[0])

if c1 == c2:
    print('True')
else:
    print('False')    

if c2 == c3:
    print('True')
else:
    print('False')  