from art import logo, vs
from game_data import data
import random

def format_data(account):
    """Takes the account data and returns a printable format."""
    account_name = account["character"]
    account_descr = account["actor"]
    account_country = account["movie"]
    return f"{account_name}, played by {account_descr}, in the film {account_country}"

def check_answer(user_guess, a_followers, b_followers):
    """Take a user's guess amd the follower counts and returns if they got it right."""
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"


print(logo)
score = 0
game_should_continue = True
# generate a random account from the game data
account_b = random.choice(data)

# Make the game repeatable
while game_should_continue:
    # Make account at position B become the next account A
    account_a = account_b
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")

    # ask user to guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # clear the screen
    print("\n" * 20)
    print(logo)
    # Check if user is correct.
    # - Get the follower count of each account.
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    #  - Check against user input
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # Give user feedback on their guess.
    # Score keeping.
    if is_correct:
        score += 1
        print(f"You're right! Current score {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        game_should_continue = False
        