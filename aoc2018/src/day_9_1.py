def place_marble(marble_circle_status, marble_no, current_position, player_playing, score_input):
    if marble_no == 1 or marble_no == 2:
        new_position = 1
        marble_circle_status.insert(new_position, marble_no)
    else:
        if marble_no % 23 != 0:
            new_position = (current_position + 2) % (len(marble_circle))
            marble_circle_status.insert(new_position, marble_no)
        else:
            score[player_playing] += marble_no
            marble_to_remove = (current_position - 7) % len(marble_circle)
            score_input[player_playing] += marble_circle[marble_to_remove]
            #marble_circle_status.remove(marble_to_remove)
            del marble_circle_status[marble_to_remove]
            new_position = marble_to_remove
    return marble_circle_status, new_position, score_input


max_marble = 7178700
no_players = 463
score = [0]*no_players
current_player = 0
marble_circle = [0]
current_marble_no = 1
new_position = 0
for i in range(0, max_marble+1):
    marble_circle, new_position, score = place_marble(marble_circle, current_marble_no, new_position, current_player, score)
    # print(marble_circle, score, new_position)
    current_player += 1
    current_player = current_player % no_players
    current_marble_no += 1
    if current_marble_no % 10000 == 0:
        print(current_marble_no)
print(max(score))


