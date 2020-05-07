class Hand:
    def __init__(self):
        self.hand = []
        self.result = ""
        self.points = 0
        self.soft = 0
        self.hard = 0

    def add_to_hand(self, card):
        self.hand.append(card)

    def sum_hand(self):
        aces = 0
        max_points = 21
        face_card_value = 10
        face_cards = ["J", "Q", "K"]
        self.soft = 0
        self.hard = 0
        for card in self.hand:
            if card[0] == "A":
                aces += 1
            elif card[0] in face_cards:
                self.soft += face_card_value
                self.hard += face_card_value
            else:
                self.soft += int(card[0])
                self.hard += int(card[0])
        if aces > 0:
            self.soft += aces + 10
            self.hard += aces
        if self.soft > max_points:
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
