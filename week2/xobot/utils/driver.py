from .logic import check_win
from .logic import check_tie
from .ai import ai_move

size = 10
win_num = 5
figs = "XY"


def field_init():
    lst = [['0' for p in range(size)] for i in range(size)]
    return(lst)


def make_move(field, turn, i=-1, j=-1):
    """
    В зависимости от значения turn, ход делает
    либо человек (поступившие координаты),
    либо компьютер. Затем выполняется проверка
    на победу или ничью (когда все поля заняты).
    """
    if turn and field[i][j] != '0':
        return None

    if turn:
        ret = [i, j]
        field[i][j] = figs[int(turn)]
    else:
        ret = list(ai_move(field, figs[int(turn)]))

    ret.append(False)
    res = check_win(field)

    if res:
        ret[2] = True
        ret.append(res)
    elif check_tie(field):
        ret[2] = True
        ret.append(None)
    return ret
