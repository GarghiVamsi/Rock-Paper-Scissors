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

    while choice == 'rock':
        if computer_choice == 'paper':
            print ("you lose!")
        elif computer_choice == 'scissors':
            print ("You Win!")
        elif computer_choice == 'rock':
            print ("its a tie")
        break
    while choice == 'paper':
        if computer_choice == 'scissors':
            print ("you lose!")
        elif computer_choice == 'rock':
            print ("You Win!")
        elif computer_choice == 'paper':
            print ("its a tie")
        break
    while choice == 'scissors':
        if computer_choice == 'rock':
            print ("you lose!")
        elif computer_choice == 'paper':
            print ("You Win!")
        elif computer_choice == 'scissors':
            print ("its a tie")
        break

    print( "This is the break point for the code so we can see when it loops and when it doesnt.")
