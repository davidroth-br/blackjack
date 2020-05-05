from random import sample, shuffle

class Deck:
    def __init__(self):
        card_values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        card_suits = ["\u2666", "\u2663", "\u2660", "\u2665"]
        self.complete = []
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
        self.totals = []
        self.result = ""
        self.bust = False
        self.twenty_one = False

    def add_to_hand(self, card):
        self.hand.append(card)

    def sum_hand(self):
        self.totals = []
        total = 0
        aces = 0
        for card in self.hand:
            if card[0] == "A":
                aces += 1
                continue
            elif card[0] == "J" or card[0] == "Q" or card[0] == "K":
                card_value = 10
            else:
                card_value = int(card[0])
            total += card_value
        if aces > 0:
            for ace in range(aces):
                self.totals.append(total + 1)
                self.totals.append(total + 11)
        else:
            self.totals.append(total)
        self.bust = all(total > 21 for total in self.totals)
        self.twenty_one = any(total == 21 for total in self.totals)
#        return totals

    def hand_string(self):
        hand = ""
        for card in self.hand:
            hand += card[0] + card[1] + " "
        return hand

    def check_result(self):
        totals = self.sum_hand()
        busts = 0
        for total in totals:
            if total == 21:
                self.result = "21"
            if total > 21:
                busts += 1
        if busts == len(totals):
            self.result = "BUST"


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
    player1 = Hand()
    dealer = Hand()

    # FIRST DEAL
    for i in range(2):
        player1.add_to_hand(deck1.deal_card())
    for i in range(2):
        dealer.add_to_hand(deck1.deal_card())

    keep_going = True
    dealer_turn = False
    end = False
    while keep_going:
        player1.sum_hand()
        dealer.sum_hand()
        keep_going = False

        # SHOW HANDS
        print("\nYour cards:")
        print(player1.hand_string())
        print("Dealer's cards:")
        if not dealer_turn:
            dealer_hand = dealer.hand_string()
            print("\u2630" + dealer_hand[dealer_hand.find(" "):])
        else:
            print(dealer.hand_string())

        # CHECK FOR WINNERS
        if player1.twenty_one:
            if dealer.twenty_one:
                print("\nPUSH!!! No winner!!!")
            else:
                print("\n21!!! YOU WIN!!!")
        elif player1.bust:
            print("\nBUST!!! You lose!!!")
        elif dealer.twenty_one:
            print("\nThe dealer has 21!!! You lose!!!")
        elif dealer.bust:
            print("\nThe dealer busted!!! YOU WIN!!!")
        elif end:
            print("\nThe dealer has {0} points and you have {1} points.".format(dealer_points, player1_points))
            if dealer_points > player1_points:
                print("You lose!!!")
            elif dealer_points < player1_points:
                print("YOU WIN!!!")
            else:
                print("PUSH!!! No winner!!!")
        else:
            keep_going = True

        # GAME LOGIC
        if keep_going:
            if not dealer_turn:
                request = checked_input("\nH - Hit\nS - Stand\nWhat would you like to do? ", ["H", "S"])
                if request == "H":
                    print("\nYou hit.")
                    player1.add_to_hand(deck1.deal_card())
                else:
                    print("\nYou stand.")
                    dealer_turn = True
            else:
                dealer.sum_hand()
                if len(dealer.totals) == 1:
                    if dealer.totals[0] < 17:
                        print("\nDealer hits.")
                        dealer.add_to_hand(deck1.deal_card())
                    else:
                        print("\nDealer stands.")
                        legal_points = [points for points in dealer.totals if points <= 21]
                        legal_points.sort()
                        dealer_points = legal_points[-1]
                        legal_points = [points for points in player1.totals if points <= 21]
                        legal_points.sort()
                        player1_points = legal_points[-1]
                        end = True
                else:
                    legal_points = [points for points in dealer.totals if points <= 21]
                    legal_points.sort()
                    if legal_points[-1] > 20:
                        print("\nDealer stands.")
                        dealer_points = legal_points[-1]
                        legal_points = [points for points in player1.totals if points <= 21]
                        legal_points.sort()
                        player1_points = legal_points[-1]
                        end = True
                    else:
                        print("\nDealer hits.")
                        dealer.add_to_hand(deck1.deal_card())







    play = checked_input("\nWould you like to play again? (Y/N): ", ["Y", "N"])
print("Goodbye!")
