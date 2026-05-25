import random

print("===== Rock Paper Scissors Game =====")

choices = ["rock", "paper", "scissors"]

# Scores
user_score = 0
computer_score = 0

while True:
    user = input("\nEnter rock, paper, or scissors: ").lower()

    if user not in choices:
        print("Invalid choice! Try again.")
        continue

    computer = random.choice(choices)

    print(f"\nYou chose: {user}")
    print(f"Computer chose: {computer}")

    # Game Logic
    if user == computer:
        print("It's a Tie!")

    elif (
        (user == "rock" and computer == "scissors") or
        (user == "paper" and computer == "rock") or
        (user == "scissors" and computer == "paper")
    ):
        print("You Win!")
        user_score += 1

    else:
        print("Computer Wins!")
        computer_score += 1

    # Display Scores
    print("\n----- Score Board -----")
    print(f"Your Score     : {user_score}")
    print(f"Computer Score : {computer_score}")

    # Play Again
    again = input("\nDo you want to play again? (yes/no): ").lower()

    if again != "yes":
        print("\n===== Final Scores =====")
        print(f"Your Final Score     : {user_score}")
        print(f"Computer Final Score : {computer_score}")

        if user_score > computer_score:
            print("You are the overall winner!")

        elif computer_score > user_score:
            print("Computer is the overall winner!")

        else:
            print("The game ended in a tie!")

        print("\nThanks for playing!")
        break