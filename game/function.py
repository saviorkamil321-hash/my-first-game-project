def functions(your_choise, comp_choise):
    if your_choise == comp_choise:
        print("It's a tie!")
    elif your_choise == "rock":
        if comp_choise == "scissors":
            print("You win!")
        else:
            print("You lose!")
    elif your_choise == "paper": 
        if comp_choise == "rock":
            print("You win!")
        else:
            print("You lose!")
    elif your_choise == "scissors":
        if comp_choise == "paper":
            print("You win!")
        else:
            print("You lose!")
        