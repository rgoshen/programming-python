swaps = input()
ball_location = 1

for swap_type in swaps:
    if swap_type.upper() == 'A' and ball_location == 1:
        ball_location = 2
    elif swap_type.upper() == 'A' and ball_location == 2:
        ball_location = 1
    elif swap_type.upper() == 'B' and ball_location == 2:
        ball_location = 3
    elif swap_type.upper() == 'B' and ball_location == 3:
        ball_location = 2
    elif swap_type.upper() == 'C' and ball_location == 3:
        ball_location = 1
    elif swap_type.upper() == 'C' and ball_location == 1:
        ball_location = 3

print(ball_location)
