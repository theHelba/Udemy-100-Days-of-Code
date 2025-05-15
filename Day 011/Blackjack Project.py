import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
dealer_cards = []

def deal_card():
    card_dealt = random.choice(cards)
    return card_dealt

def check_if_ace_in_hand():
    if 11 in user_cards:
        return True
    else:
        return False

def check_if_over():
    user_current_score = sum(user_cards)

    # Game is not over because an ace is in hand, replaces 11 with 1
    if user_current_score > 21 and check_if_ace_in_hand() == True:
        for i in range(len(user_cards)):
            if user_cards[i] == 11:
                user_cards[i] = 1

        user_current_score = sum(user_cards)
        print(f"    Your cards: {user_cards}, current score: {user_current_score}")
        print(f"    Dealer first card: {dealer_cards}")
        another_hit()

    # Game is over because we went over 21 without an ace
    elif sum(user_cards) > 21:
        dealer_cards.append(deal_card())
        dealer_final_score = sum(dealer_cards)
        print(f"    Your final hand: {user_cards}, final score: {user_current_score}")
        print(f"    Dealer final hand: {dealer_cards}, dealer final score: {dealer_final_score}")
        print("You went over. You lose.")

    # Game is not over because were below 21
    else:
        print(f"    Your cards: {user_cards}, current score: {user_current_score}")
        print(f"    Dealer first card: {dealer_cards}")
        another_hit()

def another_hit():
    another_card = input("Type 'y' to get another card, type 'n' to pass: ")
    if another_card.upper() == "Y":
        user_cards.append(deal_card())
        check_if_over()
    elif another_card.upper() == "N":
        print("test NO")
    else:
        pass

def first_deal():
    user_cards.append(deal_card())
    user_cards.append(deal_card())
    dealer_cards.append(deal_card())

def main():
    while True:
        user_cards.clear()
        dealer_cards.clear()

        play_y_n = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
        if play_y_n.upper() == "Y":
            first_deal()
            check_if_over()

        elif play_y_n.upper() == "N":
            print("you chose N")
            break
        else:
            pass

if __name__ == '__main__':
    main()

