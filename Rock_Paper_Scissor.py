import random

def get_computer_choice():
    choices = ['rock', 'paper', 'scissor']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'tie'
    elif (user_choice == 'rock' and computer_choice == 'scissor') or \
         (user_choice == 'scissor' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return 'user'
    else:
        return 'computer'

def print_results(user_choice, computer_choice, result):
    print(f"\nUser chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    
    if result == 'tie':
        print("It's a tie!")
    elif result == 'user':
        print("You win!")
    else:
        print("Computer wins!")

def play_game():
    user_score = 0
    computer_score = 0

    while True:
        print("\nChoose rock, paper, or scissor:")
        user_choice = input().lower()

        if user_choice not in ['rock', 'paper', 'scissor']:
            print("Invalid choice. Please choose rock, paper, or scissor.")
            continue

        computer_choice = get_computer_choice()
        result = determine_winner(user_choice, computer_choice)

        print_results(user_choice, computer_choice, result)

        if result == 'user':
            user_score += 1
        elif result == 'computer':
            computer_score += 1

        print(f"\nScore - You: {user_score} | Computer: {computer_score}")

        print("\nDo you want to play again? (yes or no)")
        play_again = input().lower()
        if play_again != 'yes':
            break

    print("\nThank you for playing!")
    print(f"Final Score - You: {user_score} | Computer: {computer_score}")

if __name__ == "__main__":
    play_game()
