from logic import check_win
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
        print(letter, end=' ')
    print('\n')

    for i in range(len(lst)):
        print(i, end = '\t')
        for j in range(len(lst[i])):
            print(lst[i][j], end=' ')
        print()


size = 10
win_num = 5

lst = [['0' for p in range(size)] for i in range(size)]

print_field(lst)
figs = "XY"
turn = False

while(True):
    move = input()

    move.replace(" ", "")
    if len(move) != 2 or move.isalpha() or move.isdigit():
        continue

    num = move[0] if move[0].isdigit() else move[1]
    let = move[0] if move[0].isalpha() else move[1]
    
    lst[int(num)][get_index(let)] = figs[turn]
    print_field(lst)
    
    res = check_win(lst)
    if res:
        print(res, ' wins!')
        break
    
    turn = not turn
