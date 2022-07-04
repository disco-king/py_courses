from random import randint as rand
import logic
from logic import check_point


def borders(field, i, j):
    pass #check if field[i][j] has any neighbors


def ai_move(field, fig):
    moves = []
    best = [0,0]
    buff = [0,0]
    dic = {}
    for i in range(logic.size):
        for j in range(logic.size):
            if field[i][j] != '0':
                continue
            field[i][j] = fig
            buff[0] = check_point(field, i, j)
            field[i][j] = '0'
            if buff[0] < best[0]:
                continue
            field[i][j] = 'X' if fig == 'Y' else 'Y'
            buff[1] = check_point(field, i, j)
            field[i][j] = '0'
            if buff[0] > best[0]:
                best = buff.copy()
                moves = [(i,j)]
            elif buff[0] == best[0]:
                if buff[1] > best[1]:
                    best = buff.copy()
                    moves = [(i,j)]
                elif buff[1] == best[1]:
                    moves.append((i,j))
            dic[(i,j)] = buff.copy()
    crds = moves[rand(0, len(moves)-1)]
    field[crds[0]][crds[1]] = fig
    return crds
