from random import randint as rand
from .logic import check_point
from .logic import size


def ai_move(field, fig):
    """
    Каждое пустое поле на доске оценивается
    по длине линии, которую образуют фигуры,
    если ход будет на этом поле.
    Чем меньше длина линии, тем выше ценность
    хода. Если у нескольких ходов для компьютера
    одинаковая ценность, выбирается тот ход,
    который был бы наиболее ценен для человека.
    Если и ценность для человека совпадает,
    выбор производится случайным образом. 
    """
    moves = []
    best = [-1,-1]
    buff = [0,0]
    dic = {}
    for i in range(size):
        for j in range(size):
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
