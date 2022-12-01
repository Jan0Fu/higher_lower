import random
from art import logo, vs
from game_data import data
import os

def random_profile():
    return (random.choice(data))

def higher_lower():
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
            print(f"Current score: {score}")
        print(f"You're right! Current score: {score}")
        print(f" Compare A: {profile1}")
        print(vs)
        print(f" Against B: {profile2}")
        user_pick = input("Pick profile 'A' or profile 'B': ").lower()
        if user_pick == 'a' and profile1['follower_count'] > profile2['follower_count']:
            score += 1
            profile1 = profile2
        elif user_pick == 'a' and profile2['follower_count'] > profile1['follower_count']:
            game_over = True
        elif user_pick == 'b' and profile2['follower_count'] > profile1['follower_count']:
            score += 1
            profile1 = profile2
        elif user_pick == 'b' and profile2['follower_count'] < profile1['follower_count']:
            game_over = True
        game_over = True
        
higher_lower()
print("Wrong, Game Over.") #Final score: {score}")