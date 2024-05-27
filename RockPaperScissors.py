def choices(choice1, choice2,player1,player2):
    if choice1 == 'rock' and choice2 == 'rock':
        print("Draw!")
    elif choice1 == 'rock' and choice2 == 'paper':
        print(f"{player2} wins!")
    elif choice1 == 'rock' and choice2 == 'scissors':
        print(f"{player1} wins!")
    elif choice1 == 'paper'  and choice2 == 'rock':
        print(f"{player1} wins!")
    elif choice1 == 'paper' and choice2 == 'paper':
        print("Draw!")
    elif choice1 == 'paper' and choice2 == 'scissors':
        print(f"{player2} wins!")
    elif choice1 == 'scissors' and choice2 == 'rock':
        print(f"{player2} wins!")
    elif choice1 == 'scissors' and choice2 == 'paper':
        print(f"{player1} wins!")
    elif choice1 == 'scissors' and choice2 == 'scissors':
        print("Draw!")
    else:
        print("Invalid options")
def pvp():
    player1=input("Player 1 enter your name: ")
    player2=input("Player 2 enter your name: ")
    if player1 != "":
        print(f"{player1} it's your turn")
        choice1 = input("Rock Paper Scissors: ").lower()
    if player2 != "":
        print(f"{player2} it's your turn")
        choice2 = input("Rock Paper Scissors: ").lower()
    choices(choice1, choice2, player1, player2)

def cvp():
    import random
    game_options = ['Rock', 'Paper', 'Scissors']
    player=input("Enter your name: ")
    if player != "":
        print(f"{player} it's your turn")
        choice1 = input("Rock Paper Scissors: ").lower()
    print("Computer's turn")
    choice2 = random.choice(game_options).lower()
    print(f"Computer chose {choice2}")
    choices(choice1, choice2, player1=player, player2="Computer")
    
if __name__ == '__main__':
    option=input("Do you want to start the game?(Y/N)").lower()
    while option == 'y':
        play = input("Computer Vs Player or Player Vs Player(CVP/PVP)").upper()
        print("---Welcome to the game---")

        if play == 'CVP':
            cvp()
        elif play == 'PVP':
            pvp()
        else:
            print("Invalid option.")
        option=input("Do you wish to continue? To continue press y, To quit press any other key: ").lower()