from deck import Deck
from hand import Hand
from game_constants import card_back, yes_or_no, max_score, points_to_stand


def checked_input(message, valid_options):
    while True:
        user_input = input(message).upper()
        if user_input not in valid_options:
            print("You must choose a valid option")
            continue
        else:
            return user_input


def first_deal():
    for i in range(2):
        player.add_to_hand(deck.deal_card())
    for i in range(2):
        dealer.add_to_hand(deck.deal_card())


def show_hands(is_dealer_turn):
    dealer_hand = dealer.all_cards()
    one_card_face_down = card_back + dealer_hand[dealer_hand.find(" "):]
    print("\nYour cards:")
    print(player.all_cards())
    print("Dealer's cards:")
    print(one_card_face_down) if not is_dealer_turn and dealer.points != max_score else print(dealer_hand)


def player_win_or_lose(game_end):
    if (dealer.points > max_score) or (game_end and dealer.points < player.points) or\
            (player.points == max_score != dealer.points):
        return "YOU WIN!!!"
    if (player.points > max_score) or (game_end and dealer.points > player.points) or\
            (dealer.points == max_score != player.points):
        return "You lose!!!"
    if (game_end and player.points == dealer.points) or (dealer.points == max_score == player.points):
        return "PUSH!!! No winner!!!"
    return ""


def check_reason():
    if (player.points == max_score) or (dealer.points == max_score):
        return "21!!! "
    if (player.points > max_score) or (dealer.points > max_score):
        return "BUST!!! "
    return ""


def check_for_winners(game_end, is_dealer_turn):
    final_score = f"\nThe dealer has {dealer.points} points and you have {player.points} points.\n"
    result = player_win_or_lose(game_end)
    reason = check_reason()
    winner = result != ""
    show_hands(winner or is_dealer_turn)
    return winner, final_score + reason + result


def players_turn():
    request = checked_input("\nH - Hit\nS - Stand\nWhat would you like to do? ", ["H", "S"])
    if request == "H":
        print("\nYou hit.")
        player.add_to_hand(deck.deal_card())
        return False
    else:
        print("\nYou stand.")
        return True


def hand_without_aces():
    if dealer.points < player.points:
        print("\nDealer hits.")
        dealer.add_to_hand(deck.deal_card())
        return False
    else:
        print("\nDealer stands.")
        return True


def hand_with_aces():
    if dealer.points <= points_to_stand and dealer.points < player.points:
        print("\nDealer hits.")
        dealer.add_to_hand(deck.deal_card())
        return False
    else:
        print("\nDealer stands.")
        return True


def dealers_turn():
    dealer.sum_hand()
    player.sum_hand()
    has_aces = dealer.soft != dealer.hard
    return hand_with_aces() if has_aces else hand_without_aces()


print("Welcome to Blackjack!\n")
play = checked_input("Ready to play? (Y/N): ", yes_or_no)
deck = Deck()

while play == "Y":
    player = Hand()
    dealer = Hand()
    deck.shuffle_cards()
    first_deal()

    found_a_winner = False
    is_dealers_turn = False
    is_end_of_game = False
    while not found_a_winner:
        player.sum_hand()
        dealer.sum_hand()
        found_a_winner, winner_message = check_for_winners(is_end_of_game, is_dealers_turn)

        if found_a_winner:
            print(winner_message)
        else:
            if not is_dealers_turn:
                is_dealers_turn = players_turn()
            else:
                is_end_of_game = dealers_turn()

    play = checked_input("\nWould you like to play again? (Y/N): ", yes_or_no)
print("Goodbye!")
