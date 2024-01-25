import random

def get_Playerchoice():
    choices_names = {"r": "rock", "p": "paper", "s": "scissors"}
    Playerchoice = input("Rock(r), Paper(p), or Scissors(s): ").lower()
    
    while Playerchoice not in choices_names:
        print("Invalid choice")
        Playerchoice = input("Choose rock(r), paper(p), or scissors(s): ").lower()
    
    return Playerchoice

def get_PC_choice():
    choices = list("rsp")
    return random.choice(choices)

def determine_winner(Playerchoice, PC_choice):
    choices_names = {"r": "rock", "p": "paper", "s": "scissors"}
    Playerchoice_name = choices_names[Playerchoice]
    PC_Choice_name = choices_names[PC_choice]

    if Playerchoice == PC_choice:
        return "It's a tie!"
    elif (
        (Playerchoice == "r" and PC_choice == "s") or
        (Playerchoice == "s" and PC_choice == "p") or
        (Playerchoice == "p" and PC_choice == "r")
    ):
        return f"You win! {Playerchoice_name} beats {PC_Choice_name}."
    else:
        return f"You lost! {PC_Choice_name} beats {Playerchoice_name}."

def play_game():
    User_score = 0
    PC_score = 0
    choices_names = {"r": "rock", "p": "paper", "s": "scissors"}  

    while True:
        Playerchoice = get_Playerchoice()
        PC_choice = get_PC_choice()

        print(f"\nYour choice was: {choices_names[Playerchoice]}")
        print(f"Computer chose: {choices_names[PC_choice]}")

        res = determine_winner(Playerchoice, PC_choice)
        print(res)

        if "You win" in res:
            User_score += 1
        elif "You lost" in res:
            PC_score += 1

        print(f"Scores - You: {User_score} | PC: {PC_score}")

        play_again = input("\nWanna play again? (y/n): ").lower()
        if play_again != "y":
            print("Thanks for playing")
            break

if __name__ == "__main__":
    play_game()
