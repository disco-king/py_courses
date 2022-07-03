dirs = ((0,1), (1,1), (1,0), (1,-1))
size = 10
win_num = 5


def check_seq(lst, i, j, direction):
    y = i + direction[0]
    x = j + direction[1]
    if (x >= 0 and x < size and y >= 0 and y < size
            and lst[i][j] == lst[y][x]):
        result = check_seq(lst, y, x, direction) + 1
        return result
    else:
        return 1


def check_win(lst):
    for i in range(size):
        for j in range(size):
            if lst[i][j] == '0':
                continue
            for dir in dirs:
                res = check_seq(lst, i, j, dir)
                if res == win_num:
                    return lst[i][j]
    return None

def reverse(dir):
    return (dir[0] * -1, dir[1] * -1)

def check_point(lst, i, j):
    value = 4
    for i in range(size):
        for j in range(size):
            if lst[i][j] == '0':
                return None
            for dir in dirs:
                res_ai = check_seq(lst, i, j, dir, lst[i][j])
                dir = reverse(dir)
                res_rev = check_seq(lst, i+dir[0], j+dir[1], dir, '0')
                res_ai[0] += res_rev[0]
                res_ai[1] += res_rev[1]
                if res_ai[0] + res_ai[1] >= win_num:
                    res_ai[0] = 5 - res_ai[0]
                    value = min(value, res_ai[0])
    return value
