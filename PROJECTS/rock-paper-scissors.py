import random

while True:
    choices = ["rock", "paper", "scissors"]
    bot = random.choice(choices)

    player = None

    while player not in choices:
        # if player answer is blank
        # if input doesn't contain anything in choices list
        # it keeps asking until you put in rock, paper or scissors
        player = input("Rock, paper or scissors?: ").lower()

    if player == bot:
        print("bot chooses: " + bot)
        print("You chose: " + player)
        print("Tie!")
    elif player == "rock":
        if bot == "paper":
            print("bot chooses: " + bot)
            print("You chose: " + player)
            print("You Loose!")
        if bot == "scissors":
            print("Computer chooses: " + bot)
            print("You chose: " + player)
            print("You win!")
    elif player == "scissors":
        if bot == "rock":
            print("bot chooses: " + bot)
            print("You chose: " + player)
            print("You Loose!")
        if bot == "paper":
            print("Computer chooses: " + bot)
            print("You chose: " + player)
            print("You win!")
    elif player == "paper":
        if bot == "scissors":
            print("bot chooses: " + bot)
            print("You chose: " + player)
            print("You Loose!")
        if bot == "rock":
            print("Computer chooses: " + bot)
            print("You chose: " + player)
            print("You win!")

    play_again = input("Play again? (yes)/(no)").lower()
    if play_again != "yes":
        break
    # in while, because we added a feature, if you want to continue or not
print("Bye.")
