player_1 = input('rock (R), paper (P), or scissors (S)? ')
player_2 = input('rock (R), paper (P), or scissors (S)? ')

if player_1.lower() == player_2.lower():
    print('draw!')

elif (player_1.lower() == 'r' and player_2.lower()== 's') or (player_1.lower() == 's' and player_2.lower() == 'p') or (player_1.lower() == 'r' and player_2.lower() == 'p'):
    print('player1 won!')

elif (player_2.lower() == 'r' and player_1.lower()== 's') or (player_2.lower() == 's' and player_1.lower() == 'p') or (player_2.lower() == 'r' and player_1.lower() == 'p'):
    print('player1 won!')