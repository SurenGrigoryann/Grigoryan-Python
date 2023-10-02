round1_1 = round1_2 = round2_1 = round2_2 = round3_1 = round3_2 = round4_1 = round4_2 = round5_1 = round5_2 = round6_1 = round6_2 = round7_1 = round7_2 = round8_1 = round8_2 = round9_1 = round9_2 = 0
round10_1 = round10_2 = round10_3 = 0
list_of_last_round = [round10_1,round10_2,round10_3]

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
score = [0,0,0,0,0,0,0,0,0]
score10 = 0
rounds = 0
strike_one_shot = 0
strike_two_shots = 0
hdcp_score = 0
time_to_stop = False

def show1(rounds,strike_one_shot,strike_two_shots):
    round1_1 = int(input('your first shot > '))
    if round1_1 == 10:
        print('Wow Strike from first shot!')
        last_three_score[0] = '1'
        list_of_rounds_score[rounds - 1][0] = ''
        list_of_rounds_score[rounds - 10][1] = 'X'

    else:
        round1_2 = int(input('your second shot > '))
        if round1_1 + round1_2 == 10:
            list_of_rounds_score[rounds - 1][0] = round1_1
            list_of_rounds_score[rounds - 1][1] = '/'
            last_three_score[0] = '0.5'

        else:
            list_of_rounds_score[rounds - 1][0] = round1_1
            list_of_rounds_score[rounds - 1][1] = round1_2
            score[rounds-1] = round1_1 + round1_2
        # end if
    # end if
    if strike_one_shot == 1:
        last_three_score[0] = '1'
    # end if

# end function show1

  
def show2():
    if rounds != 10:
        strike_one_shot = 0
        strike_two_shots = 0
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
            # end if
        # end if
        if strike_one_shot == 1:
            if last_three_score[0] == '1':
                if last_three_score[1] == '1':
                    
                    score[rounds-3] = score[rounds-4] + 30
                else:
                    last_three_score[1] = '1'
                # end if 
            elif last_three_score[0] == '0.5':
                score[rounds-2] = score[rounds-3] + 20
                last_three_score[0] = '1'
            else:
                last_three_score[0] = '1'
            # end if
        elif strike_two_shots == 1:
            if last_three_score[0] == '1':
                if last_three_score[1] == '1':
                    score[rounds - 3] = score[rounds-4] + 20 + round1_1
                    score[rounds - 2] = score[rounds - 3] + 20
                    last_three_score[0] = '0.5'
                else:
                    score[rounds-2] = score[rounds-3] + 20
                    last_three_score[0] = '0.5'
                # end if 
            elif last_three_score[0] == '0.5':
                score[rounds - 2] = score[rounds - 3] + 10 + round1_1
            else:
                last_three_score[0] = '0.5'
            # end if 
            list_of_rounds_score[rounds - 1][0] = round1_1
            list_of_rounds_score[rounds - 1][1] = round1_2
        else:
            list_of_rounds_score[rounds - 1][0] = round1_1
            list_of_rounds_score[rounds - 1][1] = round1_2
            if last_three_score[0] == '1':
                if last_three_score[1] == '1':
                    score[rounds-3] = score[rounds-4] + 20 + round1_1
                    score[rounds-2] = score[rounds-3] + 10 + round1_1 + round1_2
                    last_three_score[0] = '0'
                    last_three_score[1] = '0'
                else:
                    score[rounds-2] = score[rounds - 3] + 10 + round1_1 + round1_2
                    print()
                    print(score[rounds-2])
                # end if
                last_three_score[0] = '0'
            elif last_three_score[0] == '0.5':
                score[rounds-2] = score[rounds - 3] + 10 + round1_1
                last_three_score[0] = '0'
            # end if
            score[rounds-1] = score[rounds-2] + round1_1 + round1_2
        # end if
        strike_one_shot = 0
        strike_two_shots = 0       
    else:
        round10_1 = int(input('your first shot > '))
    #if strike_one_shot == 1:

        if round10_1 == 10:
            list_of_last_round[0] = 'X'
            round10_2 = int(input('your second shot > '))
            round10_3 = int(input('your third shot > '))
            if round10_2 == 10:
                list_of_last_round[1] = 'X'
                if round10_3 == 10:
                    list_of_last_round[2] = 'X'
                else:
                    list_of_last_round[2] = round10_3
                # end if

            elif round10_3 == 10:
                list_of_last_round[2] = 'X'
                list_of_last_round[1] = round10_2
            else:
                list_of_last_round[1] = round10_2
                list_of_last_round[2] = round10_3
            # end if
        else:
            round10_2 = int(input('your second shot > '))
            if round10_1 + round10_2 == 10:
                list_of_last_round[0] = round10_1
                list_of_last_round[1] = '/'
                strike_two_shots = 1
            else:
                list_of_last_round[0] = round10_1
                list_of_last_round[1] = round10_2
                list_of_last_round[2] = round10_3
        time_to_stop = True
            # end if
        # end if
        score10 = score[rounds-10] + round10_1 + round10_2 + round10_3

# end function show2
 






while time_to_stop == False:
    rounds += 1
    print(f'\t\trounds\t\t\t  |', end = '')
    print(f'Hdcp Score\t|', end = '')
    print(f'Max Possible|')
    for i in range(9): 
        if i != 0:
            print(f'   {list_of_rounds[i]}',end='')
        else:
            print(f' {list_of_rounds[i]}',end='')
        # end if
    # end for
    print('    10 ', end = '')
    for i in range(len(score)):
        if int(score[i]) != 0:
            hdcp_score = score[i]
        # end if
        i += 1
    # end for
    print(f' |\t{hdcp_score}\t|\t     |')
    for i in range(69):
        print('-', end = '')
    # end for
    print('|')
    for i in range(9):
        print(list_of_rounds_score[i][0], list_of_rounds_score[i][1], end = '')
        print('|', end = '')
    # end for
    print(list_of_last_round[0],list_of_last_round[1], list_of_last_round[2], '|')
    print('')
    for i in range(69):
        print('-', end = '')
    # end for
    print('|')
    for i in range(9):
        print(score[i], end = '')
        print('  |', end = '')
    # end for
    print(score10,'    |')
    #if rounds == 10:
     #   show3()
      #  break
    if rounds == 1:
        show1(rounds,strike_one_shot,strike_two_shots)
    else:
        show2()
    # end if
    
    
# Line 113
# Need to write the round 10 of three shotys possible