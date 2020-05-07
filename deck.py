from random import sample, shuffle
from game_constants import card_values, card_suits


class Deck:
    def __init__(self):
        self.complete = []
        self.shuffled = []
        for card_suit in card_suits:
            for card_value in card_values:
                self.complete.append((card_value, card_suit))
        shuffle(self.complete)

    def shuffle_cards(self):
        shuffle(self.complete)
        self.shuffled = sample(self.complete, len(self.complete))

    def deal_card(self):
        return self.shuffled.pop()
