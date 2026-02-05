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
    """Take a user's guess and the follower counts and returns if they got it right."""
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"

print("\n" * 20)
print(logo)
print("She doesn’t even go here!")
print("\n" * 2)

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

    print("Who has more followers??")
    print(f"A: {format_data(account_a)}.")
    print(vs)
    print(f"B: {format_data(account_b)}.")
    

    # ask user to guess
    guess = input("Type 'A' or 'B': ").lower()

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
        print(f"That is so fetch!\nCurrent score {score}")
        print("\n")
    else:
        print("\n" * 4)
        print(f"Gretchen, stop trying to make fetch happen! It’s not going to happen!\nSorry, wrong choice. Final score: {score}\nYou can’t sit with us!")
        print("\n" * 4)
        game_should_continue = False
        