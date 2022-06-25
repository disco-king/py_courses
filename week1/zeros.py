from math import log, floor

def zeros(n):
    if n == 0:
        return 0
    ret = 0
    for i in range(1, floor(log(n, 5)) + 1):
        ret += floor(n / 5 ** i)
    return ret

# for num in (0, 6, 30, 1000):
#     print(num, "! has ", zeros(num), " trailing zeros", sep="")

# assert zeros(0) == 0
# assert zeros(6) == 1
# assert zeros(30) == 7