import art
import random
import game_data

# set game standards
score = 0
continue_game = True

# import data and randomly choose accounts to compare
data_list = game_data.data
acct_a = random.choice(data_list)
acct_b = random.choice(data_list)
if acct_a == acct_b:
    acct_b = random.choice(data_list)

# access account info from dictionary
def user_data(acct):
    acct_name = acct["name"]
    acct_desc = acct["description"]
    acct_location = acct["country"]
    return(f"{acct_name}, {acct_desc}, from {acct_location}.")

# function to compare follower count, returns higher result
def compare_followers(a_followers, b_followers, guess):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

print(art.logo)

# while game continues, it will keep receiving guesses and updating score
while continue_game:
    acct_a = acct_b
    acct_b = random.choice(data_list)

    print(f"Compare A: {user_data(acct_a)}")

    print(art.vs)

    print(f"Against B: {user_data(acct_b)}")

    # received guesses
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # access follower count and retrieves result from function
    a_followers = acct_a["follower_count"]
    b_followers = acct_b["follower_count"]
    result = compare_followers(a_followers, b_followers, guess)

    # checks result to determine if game continues or ends
    if result:
        score += 1
        print(f"You're right! Current score: {score}.")
    else:
        continue_game = False
        print(f"That's wrong. Your final score is {score}.")
