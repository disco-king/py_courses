import sys
from itertools import permutations
from utils.computations import whole_run
from utils.computations import distance
from utils.computations import fill_table
import utils.parsing as parsing
import utils.output as output

"""
Проверяем аргумент программы,
считываем заданное в нем количество строк,
записываем строки в lines для вывода
и в points для вычисления расстояний. 
"""
if len(sys.argv) != 2:
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

"""
Два особых случая - аргумент 0,
на который программа демонстрирует пример работы,
и аргумент 1, для которого невозможны
вычисления по алгоритму.
"""
if line_num == 0:
    lines = output.default_lines
    points = output.default_points
    for key in points:
        print(f"{lines[key]} -"
            " ({x}, {y})".format(x=key[0], y=key[1]))

elif line_num == 1:
    print()
    output.print_format(lines[points[0]], points[0], 0.0, "")
    print(f"\n Кратчайшее возможное расстояние: {0.0}")
    exit()

table = fill_table(points)

"""
Вычисляем длину каждой из пермутаций пути,
находим минимальную длину и выводим результат.
"""
combs = permutations(points[1:], len(points) - 1)
res = tuple()
min_run = float("inf")
for comb in combs:
    run = whole_run(points[0], comb, min_run)
    if run < min_run:
        min_run = run
        res = comb

output.print_results(lines, res, points[0])
print(f"\n Кратчайшее возможное расстояние: {min_run}")