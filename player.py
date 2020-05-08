from game_constants import face_cards, ace, face_card_value, max_score, min_bet, max_bet


class Player:
    def __init__(self):
        self.hand = []
        self.chips = 100
        self.bet = 0
        self.winnings = 0
        self.result = ""
        self.points = 0
        self.soft = 0
        self.hard = 0

    def empty_hand(self):
        self.hand = []

    def add_to_hand(self, card):
        self.hand.append(card)

    def sum_hand(self):
        aces = 0
        self.soft = 0
        self.hard = 0
        for card in self.hand:
            if card[0] == ace:
                aces += 1
            elif card[0] in face_cards:
                self.soft += face_card_value
            else:
                self.soft += int(card[0])
        self.hard = self.soft
        if aces > 0:
            self.soft += aces + 10
            self.hard += aces
        if self.soft > max_score:
            self.points = self.hard
        else:
            if self.hard < self.soft:
                self.points = self.soft
            else:
                self.points = self.hard

    def all_cards(self):
        hand = ""
        for card in self.hand:
            hand += card[0] + card[1] + " "
        return hand

    def place_bet(self):
        while True:
            try:
                self.bet = int(input(f"\nYou have {self.chips} chips.\nHow many would you like to bet? "))
            except ValueError:
                print("\nYou must enter a number.")
                continue
            if (min_bet <= self.bet <= max_bet) and (self.bet <= self.chips):
                break
            else:
                print("""\nYou must enter an amount of chips between 5 and 50
without exceeding your total amount of chips.
Please try again.""")
