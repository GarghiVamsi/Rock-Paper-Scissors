#Rock Paper Scissors Game in Python. 
import random

#Makes the code run in a loop until cancelled
while True:
    print('Make your choise:')
    #input my choice
    choice = input()
    choice = choice.lower() 

    #prints my choice
    print("My choice is", choice)

    #The difference in choices for the game
    choices = ['rock', 'paper', 'scissors']

    #Randomly chooses between rock, paper, scissors
    computer_choice = choices[random.randint(0, len(choices)-1)]

    #prints the computer choice
    print("comp choice is", computer_choice)

    while choice == choice:
        if computer_choice == choice:
            print ("tie")
        elif choice == "rock":
            if computer_choice == "paper":
                print ("You Lose!", computer_choice, "beats", choice)
            else:
                print("You win!", choice, "beats", computer_choice)
        elif choice == "paper":
            if computer_choice == "scissors":
                print ("You Lose!", computer_choice, "beats", choice)
            else:
                print("You win!", choice, "beats", computer_choice)
        elif choice == "scissors":
            if computer_choice == "rock":
                print ("You Lose!", computer_choice, "beats", choice)
            else:
                print("You win!", choice, "beats", computer_choice)
        elif computer_choice != choice:
            print("This input is invalid, please try again! Maybe check your spelling")
        break