dirs = ((0,1), (1,1), (1,0), (1,-1))
size = 10
win_num = 5


def check_nul(lst, i, j, direction, fig):
    y = i + direction[0]
    x = j + direction[1]
    if (x >= 0 and x < size and y >= 0 and y < size
            and lst[y][x] in ('0', fig)):
        return check_nul(lst, y, x, direction, fig) + 1
    return 1

def check_seq(lst, i, j, direction):
    y = i + direction[0]
    x = j + direction[1]
    result = [1, 0]
    if x >= 0 and x < size and y >= 0 and y < size:
        if lst[i][j] == lst[y][x]:
            ret = check_seq(lst, y, x, direction)
            result[0] += ret[0]
            result[1] += ret[1]
        elif lst[y][x] == '0':
            result[1] += check_nul(lst, y, x, direction, lst[i][j])
    return result

def check_win(lst):
    for i in range(size):
        for j in range(size):
            if lst[i][j] == '0':
                continue
            for dir in dirs:
                res = check_seq(lst, i, j, dir)
                if res[0] == win_num:
                    return lst[i][j]
    return None

def reverse(dir):
    return (dir[0] * -1, dir[1] * -1)

def check_point(lst, i, j):
    value = 4
    if lst[i][j] == '0':
        return None
    # lst[i][j] = fig
    for dir in dirs:
        res_dir = check_seq(lst, i, j, dir)
        res_rev = check_seq(lst, i, j, reverse(dir))
        res_dir[0] += res_rev[0] - 1
        res_dir[1] += res_rev[1]
        if res_dir[0] + res_dir[1] >= win_num:
            res_dir[0] = 5 - res_dir[0]
            value = min(value, res_dir[0])
    # lst[i][j] = '0'
    return value
