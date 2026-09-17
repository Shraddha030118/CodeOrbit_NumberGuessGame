import random

def play_game():
    number = random.randint(1, 100)
    attempts = 0

    print("\n==============================")
    print("     NUMBER GUESSING GAME")
    print("==============================")
    print("I have selected a number between 1 and 100.")
    print("Try to guess it!")

    while True:
        try:
            guess = int(input("\nEnter your guess: "))
            attempts += 1

            if guess < number:
                print("Too low! Try again.")

            elif guess > number:
                print("Too high! Try again.")

            else:
                print(f"🎉 Correct! The number was {number}.")
                print(f"You guessed it in {attempts} attempts.")
                break

        except ValueError:
            print("Please enter a valid number.")


def main():
    while True:
        play_game()

        choice = input("\nDo you want to play again? (yes/no): ").lower()

        if choice != "yes":
            print("\nThanks for playing!")
            break


if __name__ == "__main__":
    main()