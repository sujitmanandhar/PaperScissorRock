import random

while True:
    choices = ['paper','scissor','rock']

    computer = random.choice(choices)

    player = None

    while player not in choices:
        player = input('rock,paper or scissors?').lower()

    if player == computer :
        print("Computer:",computer)
        print("Player:",player)
        print('It is a Tie')

    elif player == "rock":
        if computer == "paper":
            print("Computer:",computer)
            print("Player:",player)
            print('You lost')

        if computer == "scissor":
            print("Computer:",computer)
            print("Player:",player)
            print('You won')

    elif player == "scissor":
        if computer == "paper":
            print("Computer:",computer)
            print("Player:",player)
            print('You won')

        if computer == "rock":
            print("Computer:",computer)
            print("Player:",player)
            print('You lost')

    elif player == "paper":
        if computer == "rock":
            print("Computer:",computer)
            print("Player:",player)
            print('You won')

        if computer == "scissor":
            print("Computer:",computer)
            print("Player:",player)
            print('You lost')

    play_again = input('Play again? (yes/No):').lower()

    if play_again != 'yes':
        break

print('Good Bye! Thank you for playing!')
