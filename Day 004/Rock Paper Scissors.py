import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice_list = [rock, paper, scissors]

player_choice = input("\nWhat do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: ")
print(f"\nYou chose: {choice_list[int(player_choice)]}")

opp_random_number = random.randint(0, 2)
print(f"Opponent chose: {choice_list[opp_random_number]}")
print()

# Rock choices
if int(player_choice) == 0 and opp_random_number == 0:
    print("Tie!")
elif int(player_choice) == 0 and opp_random_number == 1:
    print("You Lose!")
elif int(player_choice) == 0 and opp_random_number == 2:
    print("You Win!")

# Paper choices
elif int(player_choice) == 1 and opp_random_number == 0:
    print("You Win!")
elif int(player_choice) == 1 and opp_random_number == 1:
    print("Tie!")
elif int(player_choice) == 1 and opp_random_number == 2:
    print("You Lose!")

# Scissor choices
elif int(player_choice) == 2 and opp_random_number == 0:
    print("You Lose!")
elif int(player_choice) == 2 and opp_random_number == 1:
    print("You Win!")
elif int(player_choice) == 2 and opp_random_number == 2:
    print("Tie!")

print()
