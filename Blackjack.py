from random import randint

# INITIATE DECK OF CARDS
cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
suits = ["\u2666", "\u2663", "\u2660", "\u2665"]
unshuffled_deck = []
for suit in suits:
    for card in cards:
        unshuffled_deck.append((card, suit))

# SHUFFLE DECK
deck = []
while unshuffled_deck:
    pick = randint(0, len(unshuffled_deck) - 1)
    deck.append(unshuffled_deck.pop(pick))


class Hand:
    def __init__(self):
        self.hand = []

    def add_to_hand(self):
        self.hand.append(deal_card())

    def sum_hand(self):
        totals = [0]
        aces = 0
        for card in self.hand:
            if card[0] == "A":
                aces += 1
                continue
            elif card[0] == "J" or card[0] == "Q" or card[0] == "K":
                card_value = 10
            else:
                card_value = int(card[0])
            totals[0] += card_value
        for ace in range(aces):
            totals.append(totals[0] + 1)
            totals.append(totals[0] + 11)
        return totals

    def hand_string(self):
        hand = ""
        for card in self.hand:
            hand += card_face(card) + " "
        return hand

    def check_result(self):
        totals = self.sum_hand()
        busts = 0
        for total in totals:
            if total == 21:
                return "21!!! You win!!!"
            if total > 21:
                busts += 1
        if busts == len(totals):
            return "BUST!!! You lose!!!"
        return ""


def y_n_input(message):
    while True:
        y_n = input(message).lower()
        if y_n != "y" and y_n != "n":
            print("You must choose either 'y' or 'n'.")
            continue
        else:
            return y_n


def deal_card():
    return deck.pop()


def card_face(card):
    return card[0] + card[1]


print("Welcome to Blackjack!\n")
play = y_n_input("Ready to play? (y/n): ")
print()
while play == "y":
    player1 = Hand()
    dealer = Hand()

    # FIRST DEAL
    for i in range(2):
        player1.add_to_hand()
    print("Your cards:")
    print(player1.hand_string())
    result = player1.check_result()
    if result != "":
        print(result)

    for i in range(2):
        dealer.add_to_hand()
    print("Dealer's cards:")
    dealer_hand = dealer.hand_string()
    print("\u2630" + dealer_hand[dealer_hand.find(" "):])

    while result == "":
        break



    play = y_n_input("\nWould you like to play again? (y/n): ")
print("Goodbye!")
