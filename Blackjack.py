from deck import Deck
from hand import Hand


def checked_input(message, valid_options):
    while True:
        user_input = input(message).upper()
        if user_input not in valid_options:
            print("You must choose a valid option")
            continue
        else:
            return user_input


def show_hands():
    print("\nYour cards:")
    print(player.hand_string())
    print("Dealer's cards:")
    if not dealer_turn and dealer.points != 21:
        dealer_hand = dealer.hand_string()
        print("\u2630" + dealer_hand[dealer_hand.find(" "):])
    else:
        print(dealer.hand_string())


def check_for_winners():
    winner = True
    final_score = ""
    message = ""
    if player.points == 21:
        if dealer.points == 21:
            message = "\nPUSH!!! No winner!!!"
        else:
            message = "\n21!!! YOU WIN!!!"
    elif player.points > 21:
        message = "\nBUST!!! You lose!!!"
    elif dealer.points == 21:
        message = "\nThe dealer has 21!!! You lose!!!"
    elif dealer.points > 21:
        message = "\nThe dealer busted!!! YOU WIN!!!"
    elif end:
        final_score = "\nThe dealer has {0} points and you have {1} points.".format(dealer.points, player.points)
        if dealer.points > player.points:
            message = "You lose!!!"
        elif dealer.points < player.points:
            message = "YOU WIN!!!"
        else:
            message = "PUSH!!! No winner!!!"
    else:
        winner = False
    return winner, final_score + message


print("Welcome to Blackjack!\n")
play = checked_input("Ready to play? (Y/N): ", ["Y", "N"])

deck = Deck()

while play == "Y":
    deck.shuffle_deck()
    player = Hand()
    dealer = Hand()

    # FIRST DEAL
    for i in range(2):
        player.add_to_hand(deck.deal_card())
    for i in range(2):
        dealer.add_to_hand(deck.deal_card())

    found_a_winner = False
    dealer_turn = False
    end = False
    while not found_a_winner:
        player.sum_hand()
        dealer.sum_hand()

        show_hands()

        found_a_winner, winner_message = check_for_winners()

        if found_a_winner:
            print(winner_message)
        else:
            if not dealer_turn:  # PLAYER'S TURN
                request = checked_input("\nH - Hit\nS - Stand\nWhat would you like to do? ", ["H", "S"])
                if request == "H":
                    print("\nYou hit.")
                    player.add_to_hand(deck.deal_card())
                else:
                    print("\nYou stand.")
                    dealer_turn = True
            else:  # DEALER'S TURN
                dealer.sum_hand()
                player.sum_hand()
                if dealer.soft == dealer.hard:  # NO ACES IN HAND
                    if dealer.points < player.points:
                        print("\nDealer hits.")
                        dealer.add_to_hand(deck.deal_card())
                    else:
                        print("\nDealer stands.")
                        end = True
                else:  # ACES IN HAND
                    if dealer.points <= 17 and dealer.points < player.points:
                        print("\nDealer hits.")
                        dealer.add_to_hand(deck.deal_card())
                    else:
                        print("\nDealer stands.")
                        end = True

    play = checked_input("\nWould you like to play again? (Y/N): ", ["Y", "N"])
print("Goodbye!")
