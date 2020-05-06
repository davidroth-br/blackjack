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

    def shuffle(self):
        shuffle(self.complete)
        self.shuffled = sample(self.complete, len(self.complete))

    def deal_card(self):
        return self.shuffled.pop()


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
        self.soft = 0
        self.hard = 0
        for card in self.hand:
            if card[0] == "A":
                aces += 1
            elif card[0] == "J" or card[0] == "Q" or card[0] == "K":
                self.soft += 10
                self.hard += 10
            else:
                self.soft += int(card[0])
                self.hard += int(card[0])
        if aces > 0:
            self.soft += aces + 10
            self.hard += aces
        if self.soft > 21:
            self.points = self.hard
        else:
            if self.hard < self.soft:
                self.points = self.soft
            else:
                self.points = self.hard

    def hand_string(self):
        hand = ""
        for card in self.hand:
            hand += card[0] + card[1] + " "
        return hand


def checked_input(message, valid_options):
    while True:
        user_input = input(message).upper()
        if user_input not in valid_options:
            print("You must choose a valid option")
            continue
        else:
            return user_input


print("Welcome to Blackjack!\n")
play = checked_input("Ready to play? (Y/N): ", ["Y", "N"])

deck1 = Deck()

while play == "Y":
    deck1.shuffle()
    player = Hand()
    dealer = Hand()

    # FIRST DEAL
    for i in range(2):
        player.add_to_hand(deck1.deal_card())
    for i in range(2):
        dealer.add_to_hand(deck1.deal_card())

    keep_going = True
    dealer_turn = False
    end = False
    while keep_going:
        player.sum_hand()
        dealer.sum_hand()
        keep_going = False

        # SHOW HANDS
        print("\nYour cards:")
        print(player.hand_string())
        print("Dealer's cards:")
        if not dealer_turn and dealer.points != 21:
            dealer_hand = dealer.hand_string()
            print("\u2630" + dealer_hand[dealer_hand.find(" "):])
        else:
            print(dealer.hand_string())

        # CHECK FOR WINNERS
        if player.points == 21:
            if dealer.points == 21:
                print("\nPUSH!!! No winner!!!")
            else:
                print("\n21!!! YOU WIN!!!")
        elif player.points > 21:
            print("\nBUST!!! You lose!!!")
        elif dealer.points == 21:
            print("\nThe dealer has 21!!! You lose!!!")
        elif dealer.points > 21:
            print("\nThe dealer busted!!! YOU WIN!!!")
        elif end:
            print("\nThe dealer has {0} points and you have {1} points.".format(dealer.points, player.points))
            if dealer.points > player.points:
                print("You lose!!!")
            elif dealer.points < player.points:
                print("YOU WIN!!!")
            else:
                print("PUSH!!! No winner!!!")
        else:
            keep_going = True

        # GAME LOGIC
        if keep_going:
            if not dealer_turn:  # PLAYER'S TURN
                request = checked_input("\nH - Hit\nS - Stand\nWhat would you like to do? ", ["H", "S"])
                if request == "H":
                    print("\nYou hit.")
                    player.add_to_hand(deck1.deal_card())
                else:
                    print("\nYou stand.")
                    dealer_turn = True
            else:  # DEALER'S TURN
                dealer.sum_hand()
                player.sum_hand()
                if dealer.soft == dealer.hard:  # NO ACES IN HAND
                    if dealer.points < player.points:
                        print("\nDealer hits.")
                        dealer.add_to_hand(deck1.deal_card())
                    else:
                        print("\nDealer stands.")
                        end = True
                else:  # ACES IN HAND
                    if dealer.points <= 17 and dealer.points < player.points:
                        print("\nDealer hits.")
                        dealer.add_to_hand(deck1.deal_card())
                    else:
                        print("\nDealer stands.")
                        end = True

    play = checked_input("\nWould you like to play again? (Y/N): ", ["Y", "N"])
print("Goodbye!")
