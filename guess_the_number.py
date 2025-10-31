import random




def game():

    com = random.randint(1, 100)

    game_on = True
    guesses = 0
    lives = 0

    option = input("Choose Deficulty Level (EASY/HARD): ").lower()

    if option == "easy":
        lives = 10
        print("you have 10 lives to guess")
        
    elif option == "hard":
        lives = 5
        print("you have 5 lives to guess")

    else:
        print("Invalid Choice! Defaulting to EASY MODE")
        lives = 10


    while game_on:

        guesses += 1

        a = int(input("Guess The Number: "))

        if a > com:
            print("guess lower number")
            lives -= 1
           

        elif a < com:
            print("guess higher")
            lives -= 1

        elif a == com:
            print(f"Congrats you guess it right - {a}")
            print(f"You Guessed the number in {guesses} attempts")
            game_on = False

        print(f"Lives left: {lives}")

        if lives == 0:
            print("You're out of lives! Better luck next time.")
            print(f"The correct number was {com}.")
            game_on = False

while True:
    game()

    resume = input("Wanna Play Again (YES/NO): ").lower()
    
    if resume != "yes":
        print("Thanks For Playing! Come Again!")
        break


