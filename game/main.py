import random
from function import functions

def play_game():
    print("Welcome to the game!")
    your_choise = input("enter your choice (rock, paper, scissors): ")
    comp_choise = random.choice(["rock", "paper", "scissors"])
    print(f"Computer chose: {comp_choise}")
    print(f"you chose: {your_choise}")
    functions(your_choise, comp_choise)
play_game()
    