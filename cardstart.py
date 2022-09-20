from deck import DeckOfCards
from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


deck_of_cards = DeckOfCards()
print(deck_of_cards)
'''
deck_of_cards.shuffle()
deck_of_cards.deal_card()

print(deck_of_cards)
card = deck_of_cards.deal_card()
print(card)

print(card.image_name)
image_name = card.image_name
'''

#%matplotlib
path = Path('.').joinpath('card_images')
figure, axes_list = plt.subplots(nrows=4, ncols=13)


for axes in axes_list.ravel():
    axes.get_xaxis().set_visible(False)
    axes.get_yaxis().set_visible(False)
    image_name = deck_of_cards.deal_card().image_name
    print(path.joinpath(image_name))
    img = mpimg.imread(str(path.joinpath(image_name).resolve()))
    plt.show()
    axes.imshow(img)


figure.tight_layout()

'''
print(deck_of_cards.shuffle())
print(deck_of_cards.deal_card())

card = deck_of_cards.deal_card()
print(str(card))

print(card.image_name)
'''