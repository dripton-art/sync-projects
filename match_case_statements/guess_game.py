import random # So we can pick a secret number.

play = "yes"

while play == "yes":
    secret_number = random.randint(1, 11)
    guess = None # Just to start the loop.
    
print("Guess a number between 1 and 11")
guess = int(input("enter any number: "))

match guess:
  case _ if guess == secret_number:
    print("Congratulations, you guessed!")
  case _ if guess > secret_number:
    print("Oops, your guess is a bit high. Try again!")
  case _ if guess < secret_number:
    print("Nope, your guess is a bit low. Give it another shot!")

# Ask if the user wants to play again.
play = input("Do you want to play again? (yes or no): ").lower()

if play == "yes":
    print("Lets play again!")
else:
    print("Thank you for playing!")
