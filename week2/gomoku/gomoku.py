from logic import check_win
from logic import check_point
from ai import ai_move
import os

alpha = 'ABCDEFGHIJ'

def get_index(letter):
    for num, val in enumerate(alpha):
        if val == letter.upper():
            return num
    return -1

def print_field(lst):
    print('\t', end = '')

    for letter in alpha:
        print(letter, end='   ')
    print('\n')

    for i in range(len(lst)):
        print(i, end = '\t')
        for j in range(len(lst[i])):
            print(lst[i][j] if lst[i][j] != '0' else '-', end='   ')
        print('\n')

size = 10
win_num = 5

def field_init():
    lst = [['0' for p in range(size)] for i in range(size)]
    return(lst)

figs = "XY"

def make_move(field, turn, i=-1, j=-1):
    if turn and field[i][j] != '0':
        return None
    ret = [i, j]
    if turn:
        field[i][j] = figs[int(turn)]
    else:
        ret = ai_move(field, figs[int(turn)])
    
    res = check_win(field)
    if res:
        # ret[2] = True
        print(field[res[0]][res[1]], ' loses!')
    return ret
