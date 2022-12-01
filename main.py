import random
from art import logo, vs
from game_data import data
import os

def random_profile():
    return (random.choice(data))

def compare(user_pick, followers1, followers2):
    if followers1 > followers2:
        return user_pick == "a"
    else:
        return user_pick == "b"

def higher_lower():
    global score
    score = 0
    game_over = False
    profile1 = 0
    while not game_over:
        os.system('clear')
        print(logo)
        if profile1 == 0:
            profile1 = random_profile()
        profile2 = random_profile()
        if profile1 == profile2:
            profile2 = random_profile()
        if score == 0:
            print(f" Current score: {score}")
        else:
            print(f" You're right! Current score: {score}")
        print(f" Compare A: {profile1['name']}, a {profile1['description']}, from {profile1['country']}.")
        print(vs)
        print(f" Against B: {profile2['name']}, a {profile2['description']}, from {profile2['country']}.")
        user_pick = input(" Pick profile 'A' or profile 'B': ").lower()
        profile1_followers = profile1['follower_count']
        profile2_followers = profile2['follower_count']
        is_correct = compare(user_pick, profile1_followers, profile2_followers)
        if is_correct:
            score += 1
        else:
            game_over = True

higher_lower()
os.system('clear')
print(logo)
print(f" Wrong, Game Over. Final score: {score}")