from random import randint

cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
suits = ["\u2666", "\u2663", "\u2660", "\u2665"]
deck = []

for suit in suits:
    for card in cards:
        deck.append((card, suit))

def y_n_input(message):
    while True:
        y_n = input(message).lower()
        if y_n != "y" and y_n != "n":
            print("You must choose either 'y' or 'n'.")
            continue
        else:
            return y_n

def deal_card():
    card = None
    while card in delt_cards:
        card = randint(0, 51)
    delt_cards.append(card)
    return card

def first_deal():
    for i in range(2):
        player_cards.append(deal_card())
    for i in range(2):
        dealer_cards.append(deal_card())

def print_card(card):
    print(deck[card][0] + deck[card][1])

def show_hand(player):
    if player == "P":
        print("Your cards:")
        for card in player_cards:
            print_card(card)
    else:
        print("Dealer's cards:")
        for card in dealer_cards:
            if card == dealer_cards[0]:
                print("\u2630")
            else:
                print_card(card)

print("Welcome to Blackjack!\n")
play = y_n_input("Ready to play? (y/n): ")
while play == "y":
    delt_cards = [None]
    player_cards = []
    dealer_cards = []

    first_deal()
    show_hand("P")
    show_hand("D")

    play = y_n_input("Would you like to play again? (y/n): ")
print("Goodbye!")
#print(card)
#print(deck[card][0] + deck[card][1])