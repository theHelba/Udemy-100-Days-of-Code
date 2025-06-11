import random

def generate_number():
    number = random.randint(1,100)
    return number

RANDOM_NUMBER = generate_number()

def choose_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    return difficulty

def guess_number():
    number_guessed = input("Guess a number: ")
    if int(number_guessed) == RANDOM_NUMBER:
        return True
    elif int(number_guessed) > RANDOM_NUMBER:
        return "too high"
    elif int(number_guessed) < RANDOM_NUMBER:
        return "too low"
    else:
        pass

def main():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    difficulty = choose_difficulty()
    if difficulty.lower() == "easy":
        attempts = 10
        print(f"You chose easy, {attempts} guesses available.")
        while attempts > 0:
            correct_guess = guess_number()
            if correct_guess is True:
                print("Correct guess, you win!!!")
                attempts = 0
            elif correct_guess == "too high":
                attempts -= 1
                print(f"Too high, {attempts} guesses left")
            elif correct_guess == "too low":
                attempts -= 1
                print(f"Too low, {attempts} guesses left")
            else:
                attempts -= 1
                print(f"Try again, {attempts} guesses left")

    elif difficulty.lower() == "hard":
        attempts = 5
        print(f"You chose hard, {attempts} guesses available.")
        while attempts > 0:
            correct_guess = guess_number()
            if correct_guess is True:
                print("Correct guess, you win!!!")
                attempts = 0
            elif correct_guess == "too high":
                attempts -= 1
                print(f"Too high, {attempts} guesses left")
            elif correct_guess == "too low":
                attempts -= 1
                print(f"Too low, {attempts} guesses left")
            else:
                attempts -= 1
                print(f"Try again, {attempts} guesses left")
    else:
        main()

if __name__ == '__main__':
    main()
