import sys
import os
import random

#global list_num
list_num = [1, 2, 3, 4, 5, 6, 7, 8, 9]

won_list = [[list_num[0], list_num[1], list_num[2]], [list_num[3], list_num[4], list_num[5]],
            [list_num[6], list_num[7], list_num[8]], [list_num[0], list_num[3], list_num[6]],
            [list_num[1], list_num[4], list_num[7]], [list_num[2], list_num[5], list_num[8]],
            [list_num[0], list_num[4], list_num[8]], [list_num[2], list_num[4], list_num[6]]]
#num_players = None
stone = 'X'
#loop_break = True
number_of_rounds = 0
choose_stone = 1
playerx = 0
playero = 0
tie = 0
c = 0
aimove = 0
list_active = [1, 2, 3, 4, 5, 6, 7, 8, 9]
center = None
side = None
corner = None
game_transition = None

def nine_round(number_of_rounds, stone):
    number_of_rounds += 1
    if number_of_rounds > 9:
        global tie
        tie += 1
        print('It is a tie!')
        stone = change_player(stone)
        create_board()
        restart_game(stone, game_transition)
    return number_of_rounds

def change_player(stone):
    if stone == 'X':
        stone = 'O'
    else:
        stone = 'X'
    return stone

def choose_stone():
    start = input("Please choose the starter player(0 = O, 1 = X): ")
    while True:
        if start == '1':
            stone = 'X'
            break
        elif start == '0':
            stone = 'O'
            break
        else:
            start = input("Please choose 1 or 0!: ")
    return stone

def game_mode(stone, game_transition):
    num_players = input("Please choose game mode(1, 2): ")
    y = 0
    print(num_players)
    while y !=1:
        if num_players == '1':
            game_transition = num_players
            one_player_mode(stone, number_of_rounds, aimove, list_num, game_transition)
            y = 1
        if num_players == "2":
            stone = choose_stone()
            game_transition = num_players
            two_player_mode(stone, number_of_rounds, list_num, game_transition)
            y =1
        else:
            num_players = input("Please choose 1 or 2: ")
            y = 2
    return

def print_score():
    print("Player X: "+str(playerx), end =' ')
    print("Tie: "+str(tie), end =' ')
    print("Player O: "+str(playero))

def create_board():
    x = 0
    print('  ' + str(list_num[0]) + ' | ' + str(list_num[1]) + ' | ' + str(list_num[2]) + '  ')
    print('-------------')
    print('  ' + str(list_num[3]) + ' | ' + str(list_num[4]) + ' | ' + str(list_num[5]) + '  ')
    print('-------------')
    print('  ' + str(list_num[6]) + ' | ' + str(list_num[7]) + ' | ' + str(list_num[8]) + '  ')

def player_turn(stone, game_transition, number_of_rounds):
    loop_break = True
    while loop_break:
        os.system('clear')
        print_score()
        create_board()
        number_of_rounds = nine_round(number_of_rounds, stone)
        try:
            step = int(input('Choose a place 1-9: '))
            if step in list_num:
                place = int(step)-1
                if list_num[place] == 'X' or list_num[place] == 'O':
                    print('Pick a free number')
                else:
                    list_num[place] = stone
                    loop_break = won_check(loop_break, stone, game_transition)
                    stone = change_player(stone)
        except (ValueError, TypeError, IndexError):
            print("Please enter a valid number")
    return loop_break

def won_check(loop_break, stone, game_transition):
    loop_break = True
    won_list = [[list_num[0], list_num[1], list_num[2]], [list_num[3], list_num[4], list_num[5]],
        [list_num[6], list_num[7], list_num[8]], [list_num[0], list_num[3], list_num[6]],
        [list_num[1], list_num[4], list_num[7]], [list_num[2], list_num[5], list_num[8]],
        [list_num[0], list_num[4], list_num[8]], [list_num[2], list_num[4], list_num[6]]]

    for i in range(len(won_list)):
            if won_list[i][0] == won_list[i][1] and won_list[i][0] == won_list[i][2]:
                won(stone, game_transition)
                loop_break = False
    return loop_break

def two_player_mode(stone, number_of_rounds, list_num, game_transition):
    loop_break = True
    while loop_break:
        #os.system('clear')
        loop_break = player_turn(stone, game_transition, number_of_rounds)

def one_player_turn(stone, game_transition, number_of_rounds):
    while True:
        try:
            step = int(input('Choose a place 1-9: '))
            if step in list_num:
                place = int(step)-1
                if list_num[place] == 'X' or list_num[place] == 'O':
                    print('Pick a free number')
                else:
                    list_num[place] = stone
                    break
        except (ValueError, TypeError, IndexError):
            print("Please enter a valid number")


def one_player_mode(stone, number_of_rounds, aimove, list_num, num_players):
    stone2 = stone
    while True:
        loop_break = True
        #os.system('clear')
        print_score()
        create_board()
        if stone == stone2:
            number_of_rounds = nine_round(number_of_rounds, stone)
            one_player_turn(stone, game_transition, number_of_rounds)
            won_check(loop_break, stone, game_transition)
            stone = change_player(stone)
        number_of_rounds = nine_round(number_of_rounds, stone)
        aimove = AI_move(aimove)
        list_num[aimove] = stone
        won_check(loop_break, stone, game_transition)
        stone = change_player(stone)

def win_move(x, y, z):
    try:
        if stone == x and stone == y:
            return z-1
        elif stone == x and stone == z:
            return y-1
        elif stone == y and stone == z:
            return x-1
        else:
            return '*'
    except (ValueError, TypeError):
        return '*' # AI
def def_move(x, y, z):
    if stone == 'O':
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
        return x
def AI_move(x):
    loop_break = True

    while loop_break == True:
        for i in range(len(won_list)):
            """
            won_list = [[list_num[0], list_num[1], list_num[2]], [list_num[3], list_num[4], list_num[5]],
            [list_num[6], list_num[7], list_num[8]], [list_num[0], list_num[3], list_num[6]],
            [list_num[1], list_num[4], list_num[7]], [list_num[2], list_num[5], list_num[8]],
            [list_num[0], list_num[4], list_num[8]], [list_num[2], list_num[4], list_num[6]]]
            """

            x = win_move(won_list[i][0], won_list[i][1], won_list[i][2])
            if x != '*':
                return x
        for a in range(len(won_list)):
            """
            won_list = [[list_num[0], list_num[1], list_num[2]], [list_num[3], list_num[4], list_num[5]],
            [list_num[6], list_num[7], list_num[8]], [list_num[0], list_num[3], list_num[6]],
            [list_num[1], list_num[4], list_num[7]], [list_num[2], list_num[5], list_num[8]],
            [list_num[0], list_num[4], list_num[8]], [list_num[2], list_num[4], list_num[6]]]
            """

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
                    return x
        loop_break = won_check(loop_break, stone, game_transition)
def won(stone, game_transition):
    os.system("clear")
    print('Player '+stone+' won!')
    create_board()
    print(stone)
    if stone == 'X':
        global playerx
        playerx += 1
    elif stone == 'O':
        global playero
        playero += 1
    restart_game(stone, game_transition)

def restart_game(stone, game_transition):
    print(game_transition)
    while True:
        rematch = input('Rematch? Y - Rematch, N - Back to menu, Q - Quit: ')
        if rematch == 'Y' or rematch=='y':
            #os.system('clear')
            global list_num
            list_num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            if game_transition == '2':
                stone = change_player(stone)
                two_player_mode(stone, number_of_rounds, list_num, game_transition)
            else:
                #stone = change_player(stone)
                one_player_mode(stone, number_of_rounds, aimove, list_num, game_transition)
            return list_num
            break
        elif rematch == 'N' or rematch == 'n':
            #os.system('clear')
            #global list_num
            list_num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            global playerx
            playerx = 0
            global playero
            playero = 0
            game_transition = None
            main()
            break
        elif rematch == 'q' or rematch == 'Q':
            sys.exit()
        else:
            print('Choose Y, N or Q!')
    return

def main():

    game_mode(stone, game_transition)

main()
