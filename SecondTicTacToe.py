import sys
import os
import random

list_num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
won_list = [[list_num[0], list_num[1], list_num[2]], [list_num[3], list_num[4], list_num[5]],
            [list_num[6], list_num[7], list_num[8]], [list_num[0], list_num[3], list_num[6]],
            [list_num[1], list_num[4], list_num[7]], [list_num[2], list_num[5], list_num[8]],
            [list_num[0], list_num[4], list_num[8]], [list_num[2], list_num[4], list_num[6]]]
stone = 'X'
number_of_rounds = 0
choose_stone = 1
playerx = 0
playero = 0
tie = 0
aimove = 0
center = None
side = None
corner = None
game_transition = None
best_of_something = None

def nine_round(number_of_rounds, stone, game_transition):
    number_of_rounds += 1
    if number_of_rounds > 9:
        global tie
        tie += 1
        os.system('clear')
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

def best_of_game(best_of_something, game_transition):
    if best_of_something in ['e', 'E']:
        print('Endless game')
        best_of_something = '10000'
    if best_of_something in ['3', '5', '7']:
        print('Best of '+best_of_something+'!')
    if playero <= (int(best_of_something)-tie-playerx)/2 and playerx <= (int(best_of_something)-tie-playero)/2:
        return
    elif playero+playerx+tie == int(best_of_something):
        print('It is a tie! N - Back to menu, Q - Quit game')
    elif playero > (int(best_of_something)-tie-playerx)/2:
        print('Player O won! N - Back to menu, Q - Quit game')
    elif playerx > (int(best_of_something)-tie-playero)/2:
        print('Player X won! N - Back to menu, Q - Quit game')
    restart_game(stone, game_transition)

def game_mode(stone, game_transition):
    game_transition = input("Please choose game mode(1, 2): ")
    number_of_rounds = 0
    y = 0
    while y !=1:
        if game_transition == '1':
            one_player_mode(stone, number_of_rounds, aimove, list_num, game_transition)
            y = 1
        if game_transition == "2":
            global best_of_something
            best_of_something = input('Game mode: Best of 3/5/7 or E - endless: ')
            while True:
                if best_of_something in ['3', '5', '7', 'e', 'E']:
                    break
                else:
                    best_of_something = input('Please choose 3, 5, 7 or E: ')
            if best_of_something in ['e', 'E']:
                best_of_something = '10000'
            stone = choose_stone()
            two_player_mode(stone, number_of_rounds, list_num, game_transition, best_of_something)
            y = 1
        else:
            game_transition = input("Please choose 1 or 2: ")
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

def player_turn(stone, game_transition, number_of_rounds, best_of_something):
    loop_break = True
    while loop_break:
        best_of_game(best_of_something, game_transition)
        os.system('clear')
        print_score()
        print(stone+' is next!')
        create_board()
        number_of_rounds = nine_round(number_of_rounds, stone, game_transition)
        try:
            while True:
                step = int(input('Choose a place 1-9: '))
                if step in list_num:
                    place = int(step)-1
                    if list_num[place] != 'X' or list_num[place] != 'O':
                        print('Pick a free number')
                        break
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

def two_player_mode(stone, number_of_rounds, list_num, game_transition, best_of_something):
    loop_break = True
    print(number_of_rounds)
    while loop_break:
        os.system('clear')
        loop_break = player_turn(stone, game_transition, number_of_rounds, best_of_something)

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


def one_player_mode(stone, number_of_rounds, aimove, list_num, game_transition):
    while True:
        easy_hard = input('E - Easy mode, H - Hard mode: ')
        if easy_hard in ['e', 'h', 'E', 'H']:
            break
    while True:
        loop_break = True
        os.system('clear')
        print_score()
        create_board()
        if stone == 'X':
            number_of_rounds = nine_round(number_of_rounds, stone, game_transition)
            one_player_turn(stone, game_transition, number_of_rounds)
            won_check(loop_break, stone, game_transition)
            stone = change_player(stone)
        if easy_hard in ['e', 'E']:
            number_of_rounds = nine_round(number_of_rounds, stone, game_transition)
            while True:
                x = random.choice(list_num)
                if x not in ['X', 'O']:
                    list_num[int(x)-1] = stone
                    break
            won_check(loop_break, stone, game_transition)
            stone = change_player(stone)
        else:
            number_of_rounds = nine_round(number_of_rounds, stone, game_transition)
            aimove = AI_move(aimove)
            list_num[aimove] = stone
            won_check(loop_break, stone, game_transition)
            stone = change_player(stone)

def win_move(x, y, z):
    try:
        if 'O' == x and 'O' == y:
            return z-1
        elif 'O' == x and 'O' == z:
            return y-1
        elif 'O' == y and 'O' == z:
            return x-1
        else:
            return '*'
    except (ValueError, TypeError):
        return '*'
def def_move(x, y, z):
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
    won_list = [[list_num[0], list_num[1], list_num[2]], [list_num[3], list_num[4], list_num[5]],
    [list_num[6], list_num[7], list_num[8]], [list_num[0], list_num[3], list_num[6]],
    [list_num[1], list_num[4], list_num[7]], [list_num[2], list_num[5], list_num[8]],
    [list_num[0], list_num[4], list_num[8]], [list_num[2], list_num[4], list_num[6]]]

    while loop_break == True:
        for i in range(len(won_list)):
            x = win_move(won_list[i][0], won_list[i][1], won_list[i][2])
            print(x)
            if x != '*':
                return x

        for a in range(len(won_list)):
            x = def_move(won_list[a][0], won_list[a][1], won_list[a][2])
            print(x)
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
    if stone == 'X':
        global playerx
        playerx += 1
    elif stone == 'O':
        global playero
        playero += 1
    restart_game(stone, game_transition)

def restart_game(stone, game_transition):
    while True:
        rematch = input('Rematch? Y - Rematch, N - Back to menu, Q - Quit: ')
        if rematch == 'Y' or rematch == 'y':
            os.system('clear')
            global list_num
            list_num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            number_of_rounds = 0
            if game_transition == '2':
                stone = change_player(stone)
                two_player_mode(stone, number_of_rounds, list_num, game_transition, best_of_something)
            else:
                stone = change_player(stone)
                one_player_mode(stone, number_of_rounds, aimove, list_num, game_transition)
            return list_num
            break
        elif rematch == 'N' or rematch == 'n':
            os.system('clear')
            #global list_num
            list_num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            global playerx
            playerx = 0
            global playero
            playero = 0
            global tie
            tie = 0
            game_transition = None
            main()
            break
        elif rematch == 'q' or rematch == 'Q':
            sys.exit()
        else:
            print('Choose Y, N or Q!')
    return

def main():
    try:
        game_mode(stone, game_transition)
    except KeyboardInterrupt:
        pass
main()
