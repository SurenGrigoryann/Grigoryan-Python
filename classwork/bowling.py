strike_once = 0
score = 0
bowling_balls = 0
strike_twice = 0
# making variables which we are going to use soon


while True:
    bowling_balls += 1
    set_one = input('your first bowling score > ')
    if set_one == '10':
        if strike_once == 1:
            score = score + 20    
        else:
            score += 10
            strike_once = 1
        print('Wow strike!')
        strike = 1
        print(f'Your score is {score}')
        pass
    else:

        set_two = input('your second bowling score > ')
        if strike_twice != 0 or strike_once != 0:
            score += (int(set_one) + int(set_two))*2
            strike_twice = 0
        else:
            score += (int(set_one) + int(set_two))
        if int(set_two) + int(set_one) >= 10:
            print('Wow strike!')
            strike_twice = 1
        
    print(f'Your score is {score}')

    if bowling_balls == 10:
        break
        