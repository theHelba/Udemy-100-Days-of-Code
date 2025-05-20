import random
from Art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
dealer_cards = []

# Deals random card from cards list
def deal_card():
    card_dealt = random.choice(cards)
    return card_dealt

# Aces are 11s, this checks to see if the 11 needs to become a 1
def check_if_ace_in_hand():
    if 11 in user_cards:
        return True
    else:
        return False

def final_hands():
    dealer_cards.append(deal_card())
    dealer_current_score = sum(dealer_cards)
    user_current_score = sum(user_cards)
    print()
    print(f"    Your cards: {user_cards}, current score: {user_current_score}")
    print(f"    Dealer cards: {dealer_cards}, current score {dealer_current_score}")
    if user_current_score > dealer_current_score:
        print("---You've Won!!!---")
    else:
        print("---Sorry there bud, but the house always wins---")

# Starts by checking if we've gone over 21
def check_if_over():
    user_current_score = sum(user_cards)

    # We're over 21 but the game is not over because an ace is in hand, replaces 11 with 1
    if user_current_score > 21 and check_if_ace_in_hand() == True:
        for i in range(len(user_cards)):
            if user_cards[i] == 11:
                user_cards[i] = 1

        # Displays our hand/score and dealers cards, then ask if we'd like to hit
        user_current_score = sum(user_cards)
        print()
        print(f"    Your cards: {user_cards}, current score: {user_current_score}")
        print(f"    Dealer first card: {dealer_cards}")
        another_hit()

    # Game is over because we went over 21 without an ace
    elif sum(user_cards) > 21:
        dealer_cards.append(deal_card())
        dealer_final_score = sum(dealer_cards)
        print()
        print(f"    Your final hand: {user_cards}, final score: {user_current_score}")
        print(f"    Dealer final hand: {dealer_cards}, dealer final score: {dealer_final_score}")
        print("---You went over, You lose---")

    # Game is not over because were below 21 and didn't have an ace in hand
    else:
        print()
        print(f"    Your cards: {user_cards}, current score: {user_current_score}")
        print(f"    Dealer first card: {dealer_cards}")
        another_hit()

# function that lets us draw another card
def another_hit():
    print()
    another_card = input("Type 'y' to get another card, type 'n' to pass: ")
    if another_card.upper() == "Y":
        user_cards.append(deal_card())
        check_if_over()
    elif another_card.upper() == "N":
        final_hands()
    else:
        pass

# Starts fresh draw with user drawing 2 and dealer drawing 1
def first_deal():
    user_cards.append(deal_card())
    user_cards.append(deal_card())
    dealer_cards.append(deal_card())

def main():
    # Display game logo
    print(logo)

    while True:
        # Clear any old user/dealer cards
        user_cards.clear()
        dealer_cards.clear()

        # Ask if user wants to play
        print()
        play_y_n = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
        if play_y_n.upper() == "Y":
            # Deals cards to user/dealer
            first_deal()
            # Start hit/lose loop
            check_if_over()

        # User doesn't want to play, exit
        elif play_y_n.upper() == "N":
            print()
            print("---Have a great day---")
            break
        # User selects an option besides 'y' or 'n' restart loop
        else:
            pass

if __name__ == '__main__':
    main()

