import sys
import os
import random

#global list_num
list_num = [1, 2, 3, 4, 5, 6, 7, 8, 9]

won_list = [[list_num[0], list_num[1], list_num[2]], [list_num[3], list_num[4], list_num[5]],
            [list_num[6], list_num[7], list_num[8]], [list_num[0], list_num[3], list_num[6]],
            [list_num[1], list_num[4], list_num[7]], [list_num[2], list_num[5], list_num[8]],
            [list_num[0], list_num[4], list_num[8]], [list_num[2], list_num[4], list_num[6]]]
stone = None
loop_break = True
player = 'X'
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

def nine_round(number_of_rounds, stone):
    number_of_rounds += 1
    if number_of_rounds == 9:
        global tie
        tie +=1
        restart(stone)
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

def game_mode(stone):
    num_players = input("Please choose game mode(1, 2): ")
    while True:
        if num_players == '1':
            one_player_mode(stone, number_of_rounds, aimove, list_num)
            break
        if num_players == "2":
            two_player_mode(stone, number_of_rounds, list_num)
            break
        else:
            num_players = input("Please choose 1 or 2: ")

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

def player_turn(stone):
    loop_break = True
    while loop_break == True:
        try:
            step = int(input('Choose a place 1-9: '))
            place = int(step)-1
            if list_num[place] == 'X' or list_num[place] == 'O':
                print('Pick a free number')
            else:
                list_num[place] = stone
                loop_break = won_check(loop_break, stone)
                break
        except (ValueError, TypeError, IndexError):
            print("Please enter a valid number")
    return

def won_check(loop_break, stone):
    won_list = [[list_num[0], list_num[1], list_num[2]], [list_num[3], list_num[4], list_num[5]],
        [list_num[6], list_num[7], list_num[8]], [list_num[0], list_num[3], list_num[6]],
        [list_num[1], list_num[4], list_num[7]], [list_num[2], list_num[5], list_num[8]],
        [list_num[0], list_num[4], list_num[8]], [list_num[2], list_num[4], list_num[6]]]

    for i in range(len(won_list)):
            if won_list[i][0] == won_list[i][1] and won_list[i][0] == won_list[i][2]:
                won(stone)
                loop_break = False
    return loop_break

def two_player_mode(stone, number_of_rounds, list_num):
    #global list_num
    #list_num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    while True:
        #os.system('clear')
        print_score()
        create_board()
        player_turn(stone)
        stone = change_player(stone)
        number_of_rounds = nine_round(number_of_rounds, stone)

def one_player_mode(stone, number_of_rounds, aimove, list_num):
    while True:
        #os.system('clear')
        print_score()
        create_board()
        player_turn(stone)
        won_check()
        stone = change_player(stone)
        number_of_rounds = nine_round(number_of_rounds)
        aimove = AI_move(aimove)
        list_num[aimove] = stone
        """
        won_list = [[list_num[0], list_num[1], list_num[2]], [list_num[3], list_num[4], list_num[5]],
            [list_num[6], list_num[7], list_num[8]], [list_num[0], list_num[3], list_num[6]],
            [list_num[1], list_num[4], list_num[7]], [list_num[2], list_num[5], list_num[8]],
            [list_num[0], list_num[4], list_num[8]], [list_num[2], list_num[4], list_num[6]]]
            """
        for i in range(len(won_list)):
            x = won(won_list[i][0], won_list[i][1], won_list[i][2])
            if x == '?':
                break

        nine_round(number_of_rounds)
        stone = change_player(stone)

def won(stone):
    os.system("clear")
    print('Player '+stone+' won!')
    create_board()
    if stone == 'X':
        global playerx
        playerx += 1
        restart(stone)
    elif stone == 'O':
        global playero
        playero += 1
        restart(stone)

def restart(stone):
    while True:
        rematch = input ('Rematch? Y - Rematch, N - Back to menu, Q - Quit: ')
        if rematch == 'Y' or rematch=='y':
            #os.system('clear')
            global list_num
            list_num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            stone = change_player(stone)
            two_player_mode(stone, number_of_rounds, list_num)
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
            main()
            break
        elif rematch == 'q' or rematch == 'Q':
            sys.exit()
        else:
            print('Choose Y, N or Q!')
    return

def main():
    stone = choose_stone()
    game_mode(stone)

main()
