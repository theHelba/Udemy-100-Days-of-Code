from art import logo

# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

# Finding max value in dictionary
#     my_dict = {'a': 10, 'b': 5, 'c': 12}
#     max_value = max(my_dict.values())
#     print(max_value)  # Output: 12

# Finding max key
#    my_dict = {'a': 10, 'b': 5, 'c': 12}
#    max_key = max(my_dict, key=my_dict.get)
#    print(max_key)  # Output: c

bidders = {}

def end_game():
    clear_screen()
    print(logo)
    print("Thanks for playing")

def clear_screen():
    print("\n" * 100)

def play_again():
    i = input("Go again? Type 'yes' or 'no'.\n")
    if i.lower() == "yes":
        bidders.clear()
        clear_screen()
        main()
    elif i.lower() == "no":
        end_game()
    else:
        play_again()

def end_results():
    highest_bid = max(bidders.values())
    highest_bidder = max(bidders, key=bidders.get)
    print(f"{highest_bidder} has won the bid with ${highest_bid}!\n")
    play_again()

def questions():
    name = input("What is your name?: ")
    bid = input("What's your bid?: ")
    # Add bidder info into dictionary
    bidders[name] = bid
    continue_or_end()

def continue_or_end():
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if other_bidders.lower() == "yes":
        clear_screen()
        questions()
    elif other_bidders.lower() == "no":
        end_results()
    else:
        continue_or_end()

def main():
    print(logo)
    print("Welcome to the secret auction program.")
    questions()

main()