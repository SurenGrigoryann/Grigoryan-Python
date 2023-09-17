round1_1 = round1_2 = round2_1 = round2_2 = round3_1 = round3_2 = round4_1 = round4_2 = round5_1 = round5_2 = round6_1 = round6_2 = round7_1 = round7_2 = round8_1 = round8_2 = round9_1 = round9_2 = 0

list_of_rounds = ['1','2','3','4','5','6','7','8','9','10']
list_of_rounds_score = [[round1_1,round1_2],
                        [round2_1,round2_2],
                        [round3_1,round3_2],
                        [round4_1,round4_2],
                        [round5_1,round5_2],
                        [round6_1,round6_2],
                        [round7_1,round7_2],
                        [round8_1,round8_2],
                        [round9_1,round9_2]]
last_three_score = ['0','0','0']
score = ['0','0','0','0','0','0','0','0','0']
rounds = 0
strike_one_shot = 0
strike_two_shots = 0

def show1(rounds,strike_one_shot,strike_two_shots):
    round1_1 = int(input('your first shot > '))
    if round1_1 == 10:
        strike_one_shot += 1
        print('Wow Strike from first shot!')
        list_of_rounds_score[rounds - 1][0] = ''
        list_of_rounds_score[rounds - 10][1] = 'X'
    else:
        round1_2 = int(input('your second shot > '))
        if round1_1 + round1_2 == 10:
            print('Strike with two shots!')
            round1_2 = '/'
            strike_two_shots += 1
    if strike_one_shot == 1:
        last_three_score[0] = 10
    
        
def show2(rounds,strike_one_shot,strike_two_shots):
    round1_1 = int(input('your first shot > '))
    if round1_1 == 10:
        strike_one_shot += 1
        print('Wow Strike from first shot!')
        list_of_rounds_score[rounds - 1][0] = ''
        list_of_rounds_score[rounds -1][1] = 'X'
    else:
        round1_2 = int(input('your second shot > '))
        if round1_1 + round1_2 == 10:
            print('Strike with two shots!')
            round1_2 = '/'
            strike_two_shots += 1
    if strike_one_shot == 1:
        last_three_score[0] = 10
    elif strike_one_shot == 2:
        last_three_score[0] = 20
        last_three_score[1] = 10
    elif strike_one_shot == 3:
        last_three_score[0] = 30
        last_three_score[1] = 20
        last_three_score[2] = 10
        score[rounds - 2] = last_three_score[0]
        print(score[rounds-2])
        





while True:
    rounds += 1
    print(f'\t\trounds\t\t   |', end = '')
    print(f'Hdcp Score\t|', end = '')
    print(f'Max Possible|')
    for i in range(9):
        if i != 0:
            print(f'   {list_of_rounds[i]}',end='')
        else:
            print(f' {list_of_rounds[i]}',end='')
    print(f' |\t\t|\t     |')
    for i in range(61):
        print('-', end = '')
    print('|')
    for i in range(9):
        print(list_of_rounds_score[i][0], list_of_rounds_score[i][1], end = '')
        print('|', end = '')
    print('')
    for i in range(61):
        print('-', end = '')
    print('|')
    for i in range(9):
        print(score[i], end = '')
        print('  |', end = '')

    if rounds == 1:
        show1(rounds,strike_one_shot,strike_two_shots)
    else:
        show2(rounds,strike_one_shot,strike_two_shots)

        
    if rounds == 9:
        break
    