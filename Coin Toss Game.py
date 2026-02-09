import random # imports `random` library

coin_sides = random.choice(["heads", "tails"]) # choices in coin toss game

player_choice = input("heads or tails?: ") # player choice

if player_choice == "heads": 
    print("coin flipped and you got: ", coin_sides)  # if player choice is `heads` computer prints random choice
if player_choice == "tails":
    print("coin flipped and you got: ", coin_sides) # if player choice is ´tails´ computer prints random choice
