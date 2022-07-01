from itertools import permutations
from computations import whole_run, distance
import parsing
import sys

if len(sys.argv) == 1:
    parsing.error_exit(0)

try:
    line_num = int(sys.argv[1])
except:
    parsing.error_exit(1)

lines = {}
points = []

for i in range(line_num):
    ret = parsing.get_coords(input())
    lines[ret[1]] = ret[0]
    points.append(ret[1])

combs = permutations(points[1:], len(points) - 1)
res = next(combs)
min_run = whole_run(points[0], res)
for comb in combs:
    run = whole_run(points[0], comb)
    if run < min_run:
        min_run = run
        res = comb

print()
dst = 0.0
ending = "->"

for i in range(-1, len(res)+1):
    if i == -1 or i == len(res):
        location = lines[points[0]]
        coordinates = points[0]
    else:
        location = lines[res[i]]
        coordinates = res[i]

    print(f" {location.ljust(30)}", end=" ")
    print(str(coordinates).ljust(15), end=" ")
    print(f"пройдено {dst} {ending}")

    if i == -1:
        dst = distance(points[0], res[0])
    elif i == len(res)-1:
        ending = ""
        dst += distance(res[i], points[0])
    elif i < len(res):
        dst += distance(res[i], res[i+1])

print(f"\n Кратчайшее возможное расстояние: {min_run}")