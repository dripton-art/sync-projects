import random # So we can pick a secret number.

play = "yes"

while play == "yes":
    secret_number = random.randint(1, 11) 

    print("Guess a number between 1 and 11")
    guess = int(input("enter any number: "))

    match guess:
        case _ if guess == secret_number:
            print("\n Congratulations, you guessed!")
        case _ if guess > secret_number:
            print("\n Oops, your guess is a bit high. Try again!")
        case _ if guess < secret_number:
            print("\n Nope, your guess is a bit low. Give it another shot!")

    # Ask if the user wants to play again.
    play = input("\n Do you want to play again? (yes or no): ").lower()

    if play == "yes":
        print("\n Starting a new game...\n")
    else:
        print("\n ***Thank you for playing***\n")
