import random

def main():
    """Start a number guessing game between 1 - 100."""
    print("Guess the number!")

    x = random.randint(1,100)
    guess = None

    while x != guess:
        guess = int(input("Pick a number between 1 to 100: "))

        if x == guess:
            print("You genius!")
        if x > guess:
            print("Try a bigger number.")
        else:
            print("Try a smaller number.")

main()