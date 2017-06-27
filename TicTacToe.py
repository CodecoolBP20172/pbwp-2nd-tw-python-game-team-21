import sys
import os
import random
#global list_num
list_num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#global a
player = 'X'
#global nine_round
nine_round = 0
valaszt = 1
#global player1
playerx = 0
#global player2
playero = 0
#global tie
tie = 0
c = 0
#global list_active
list_active = [1, 2, 3, 4, 5, 6, 7, 8, 9]
center = None
side = None
corner = None
aimove = ''
def end_game(a):
    os.system("clear")
    print('It is a tie')
    create_board('It is a tie')
    global tie
    tie+=1
    while True:
        rematch = input ('Rematch? Y - Rematch, N - Back to menu, Q - Quit')
        if rematch == 'Y' or rematch=='y':
            global nine_round
            nine_round = 0
            global list_num
            list_num = [1,2,3,4,5,6,7,8,9]
            global list_active
            list_active = [1,2,3,4,5,6,7,8,9]
            if a == 'X':
                a = 'O'
            else:
                a = 'X'
            os.system('clear')
            print('New game')
            create_board ("New Game")
            break
        elif rematch == 'N' or rematch == 'n':
            os.execl(sys.executable, sys.executable, *sys.argv)
        elif rematch == 'q' or rematch == 'Q':
            sys.exit()
        else:
            print('Choose Y, N or Q!')
    return a, list_num # Tie
def change_player(a):
    if a == 'X':
        a = 'O'
    else:
        a = 'X'
    return a # stone change
def won(x, y, z,):
    if x == z and x == y:
        os.system("clear")
        global a
        print('Player '+a+' won!')
        create_board('Player won!')
        if a == 'X':
            global playerx
            playerx += 1
        elif a == 'O':
            global playero
            playero += 1
        while True:
            rematch = input ('Rematch? Y - Rematch, N - Back to menu, Q - Quit: ')
            if rematch == 'Y' or rematch=='y':
                os.system('clear')
                global nine_round
                nine_round = -1
                global list_num
                list_num = [1,2,3,4,5,6,7,8,9]
                global list_active
                list_active = [1,2,3,4,5,6,7,8,9]
                #if a == 'X':
                 #   a = 'O'
                #else:
                 #   a = 'X'
                #print('New game')
                #create_board ("New Game")
                return '?'
            elif rematch == 'N' or rematch == 'n':
                os.execl(sys.executable, sys.executable, *sys.argv)
            elif rematch == 'q' or rematch == 'Q':
                sys.exit()
            else:
                print('Choose Y, N or Q!')
    return '!'
def create_board(x):
    x = 0
    print('  ' + str(list_num[0]) + ' | ' + str(list_num[1]) + ' | ' + str(list_num[2]) + '  ')
    print('-------------')
    print('  ' + str(list_num[3]) + ' | ' + str(list_num[4]) + ' | ' + str(list_num[5]) + '  ')
    print('-------------')
    print('  ' + str(list_num[6]) + ' | ' + str(list_num[7]) + ' | ' + str(list_num[8]) + '  ')
def player_turn(a):
    b = 0
    while b == 0:
        try:
            step = int(input('Choose a place 1-9: '))
            list_active.remove(step)
            place = int(step)-1
            if list_num[place] == 'X' or list_num[place] =='O':
                print('Pick a free number')
            else:
                list_num[place] = a
                won_list = [[list_num[0], list_num[1], list_num[2]], [list_num[3], list_num[4], list_num[5]],
                    [list_num[6], list_num[7], list_num[8]], [list_num[0], list_num[3], list_num[6]],
                    [list_num[1], list_num[4], list_num[7]], [list_num[2], list_num[5], list_num[8]],
                    [list_num[0], list_num[4], list_num[8]], [list_num[2], list_num[4], list_num[6]]]
                for i in range(len(won_list)):
                    won(won_list[i][0], won_list[i][1], won_list[i][2])
                b += 1
        except (ValueError, TypeError, IndexError):
            print ("Please enter a valid number")
    return #player move against AI
def win_move(x, y, z):
    try:
        if a == x and a == y:
            return z-1
        elif a == x and a == z:
            return y-1
        elif a == y and a == z:
            return x-1
        else:
            return '*'
    except (ValueError, TypeError):
        return '*' # AI
def def_move(x, y, z):
    if a == 'O':
        try:
            if 'X' == x and 'X' == y:
                return z-1
            elif 'X' == x and 'X' == z:
                return y-1
            elif 'X' == y and 'X' == z:
                return x-1
            else:
                return '/'
        except (ValueError, TypeError):
            return '/'
    else:
        try:
            if 'O' == x and 'O' == y:
                return z-1
            elif 'O' == x and 'O' == z:
                return y-1
            elif 'O' == y and 'O' == z:
                return x-1
            else:
                return '/'
        except (ValueError, TypeError):
            return '/' # AI
def corner_move(x):
    corner_list = [0, 2, 6, 8]
    for i in range(len(corner_list)):
        corner_list = [0, 2, 6, 8]
        x = random.choice(corner_list)
        corner_list.remove(x)
        if list_num[x] == 'X' or list_num[x] =='O':
            continue
        else:
            return x
    return '' # AI
def side_move(x):
    side_list = [1, 3, 7, 5]
    for i in range(len(side_list)):
        side_list = [1, 3, 7, 5]
        x = random.choice(side_list)
        side_list.remove(x)
        if list_num[x] == 'X' or list_num[x] =='O':
            continue
        else:
            return x
    return '' # AI
def center_move(x):
    if list_num[4] == 'X' or list_num[4] == 'O':
        return ''
    else:
        x = 4
        return x # AI
def AI_move(x):
    won_list = [[list_num[0], list_num[1], list_num[2]], [list_num[3], list_num[4], list_num[5]],
            [list_num[6], list_num[7], list_num[8]], [list_num[0], list_num[3], list_num[6]],
            [list_num[1], list_num[4], list_num[7]], [list_num[2], list_num[5], list_num[8]],
            [list_num[0], list_num[4], list_num[8]], [list_num[2], list_num[4], list_num[6]]]
    for i in range(len(won_list)):
        won_list = [[list_num[0], list_num[1], list_num[2]], [list_num[3], list_num[4], list_num[5]],
        [list_num[6], list_num[7], list_num[8]], [list_num[0], list_num[3], list_num[6]],
        [list_num[1], list_num[4], list_num[7]], [list_num[2], list_num[5], list_num[8]],
        [list_num[0], list_num[4], list_num[8]], [list_num[2], list_num[4], list_num[6]]]
        x = win_move(won_list[i][0], won_list[i][1], won_list[i][2])
        if x != '*':
            return x
    for a in range(len(won_list)):
        won_list = [[list_num[0], list_num[1], list_num[2]], [list_num[3], list_num[4], list_num[5]],
        [list_num[6], list_num[7], list_num[8]], [list_num[0], list_num[3], list_num[6]],
        [list_num[1], list_num[4], list_num[7]], [list_num[2], list_num[5], list_num[8]],
        [list_num[0], list_num[4], list_num[8]], [list_num[2], list_num[4], list_num[6]]]
        x = def_move(won_list[a][0], won_list[a][1], won_list[a][2])
        if x != '/':
            return x
    x = center_move(x)
    if x != '':
        return x
    else:
        x = corner_move(x)
        if x != '':
            return x
        else:
            x = side_move(x)
            if x != '':
                return x # AI move against player

                
while valaszt == 1: # choose stone
    valaszt = 1
    start = input("Please choose the starter player(0 = O, 1 = X): ")
    if start == '1':
        a = 'X'
        valaszt = 0
    elif start == '0':
        a = 'O'
        valaszt = 0
    else:
        print("Please choose 1 or 0!") #kezdő ikon választása
while True: # game
    try:
        num_players = int(input("Please choose game mode(1, 2): "))
        if num_players == 1: # egy játékos program
            while True: #nine_round <= len(list_num):
                os.system('clear')
                print("Player X: "+str(playerx), end =' ')
                print("Tie: "+str(tie), end =' ')
                print("Player O: "+str(playero))
                create_board('')
                player_turn(a)
                nine_round += 1
                a=change_player(a)
                if nine_round == len(list_num):
                    end_game(a)
                aimove = AI_move(aimove)
                list_num[aimove] = a
                won_list = [[list_num[0], list_num[1], list_num[2]], [list_num[3], list_num[4], list_num[5]],
                    [list_num[6], list_num[7], list_num[8]], [list_num[0], list_num[3], list_num[6]],
                    [list_num[1], list_num[4], list_num[7]], [list_num[2], list_num[5], list_num[8]],
                    [list_num[0], list_num[4], list_num[8]], [list_num[2], list_num[4], list_num[6]]]
                for i in range(len(won_list)):
                    x = won(won_list[i][0], won_list[i][1], won_list[i][2])
                    if x == '?':
                        break
                nine_round += 1
                if nine_round == len(list_num):
                    end_game(a)
                a=change_player(a)
        elif num_players ==2: #2 játékos program
            #print("2playermod")
            while True: # nine_round <= len(list_num):
                os.system("clear")
                print("Player X: "+str(playerx), end =' ')
                print("Tie: "+str(tie), end =' ')
                print("Player O: "+str(playero))
                create_board('')
                if nine_round <= len(list_num):
                    print(a+" is next!")
                while c == 0:
                    try:
                        step = int(input('Choose a place 1-9: '))
                        place = int(step)-1 #
                        if list_num[place] == 'X' or list_num[place] =='O':
                            print('Pick a free number')
                        else:
                            c += 1
                    except (ValueError, TypeError, IndexError):
                        print ("Please enter a valid number")            
                c = 0
                list_num[place] = a
                won_list = [[list_num[0], list_num[1], list_num[2]], [list_num[3], list_num[4], list_num[5]],
                            [list_num[6], list_num[7], list_num[8]], [list_num[0], list_num[3], list_num[6]],
                            [list_num[1], list_num[4], list_num[7]], [list_num[2], list_num[5], list_num[8]],
                            [list_num[0], list_num[4], list_num[8]], [list_num[2], list_num[4], list_num[6]]]
                for i in range(len(won_list)):
                    x = won(won_list[i][0], won_list[i][1], won_list[i][2])
                    if x == '?':
                        break
                nine_round += 1
                a = change_player(a)
                if nine_round >= len(list_num):
                    end_game(a)
        elif num_players not in [1,2]:
            print("Pick number 1 or number 2!")
    except(TypeError, ValueError):
        print("Pick number 1 or number 2!")