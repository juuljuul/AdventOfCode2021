import numpy as np

player_1_position = 7
player_2_position = 9
dice_rolled = 0
player_1_score = 0
player_2_score = 0
dice = 0
turn_player_1 = True

while player_1_score < 1000 and player_2_score < 1000:
    # choose player
    if dice_rolled % 6 < 3: #player 1 turn
        dice = (dice % 100) + 1
        player_1_position = (player_1_position -1 + dice) % 10 + 1
        dice = (dice % 100) + 1
        player_1_position = (player_1_position -1 + dice) % 10 + 1
        dice = (dice % 100) + 1
        dice_rolled += 3
        player_1_position = (player_1_position -1 + dice) % 10 + 1
        player_1_score += player_1_position        
    else: #player 2 turn
        dice = (dice % 100) + 1
        player_2_position = (player_2_position -1 + dice) % 10 + 1
        dice = (dice % 100) + 1
        player_2_position = (player_2_position -1 + dice) % 10 + 1
        dice = (dice % 100) + 1
        dice_rolled += 3
        player_2_position = (player_2_position -1 + dice) % 10 + 1
        player_2_score += player_2_position        

if player_1_score < player_2_score:
    loosing_player_score = player_1_score
else:
    loosing_player_score = player_2_score

print("result: ", loosing_player_score * dice_rolled)