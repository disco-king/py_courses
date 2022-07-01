from itertools import permutations
from computations import whole_run, distance
import parsing
import sys

# points = [(1,1), (4,1), (1,5)]
# points = [(1,1), (2,2), (3,3), (4,4)]
# points = [(1,1), (2,2), (3,3), (4,4), (5,5)]
# points = [(0,2), (2,5), (5,2), (6,6)]
# points = [(0,2), (2,5), (5,2), (6,6), (8,3)]

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
for i in combs:
    run = whole_run(points[0], i)
    if run < min_run:
        min_run = run
        res = i

print(f"\n {lines[points[0]]} {points[0]} пройдено 0.0 ->")
dst = distance(points[0], res[0])

for i in range(len(res)-1):
    print(f" {lines[res[i]]} {res[i]} пройдено {dst} ->")
    dst += distance(res[i], res[i+1])

i += 1
print(f" {lines[res[i]]} {res[i]} пройдено {dst} ->")
print(f" {lines[points[0]]} {points[0]}"
        f" пройдено {dst + distance(res[i], points[0])}")
print(f"\n Кратчайшее возможное расстояние: {min_run}")