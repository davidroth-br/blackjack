from random import sample, shuffle


class Deck:
    def __init__(self):
        card_values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        card_suits = ["\u2666", "\u2663", "\u2660", "\u2665"]
        self.complete = []
        self.shuffled = []
        for card_suit in card_suits:
            for card_value in card_values:
                self.complete.append((card_value, card_suit))
        shuffle(self.complete)

    def shuffle_deck(self):
        shuffle(self.complete)
        self.shuffled = sample(self.complete, len(self.complete))

    def deal_card(self):
        return self.shuffled.pop()
