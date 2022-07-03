import sys
from itertools import permutations
from utils.computations import whole_run
from utils.computations import fill_table
import utils.parsing as parsing
import utils.output as output

"""
Проверяем аргумент программы,
считываем заданное в нем количество строк и
записываем названия и координаты в словарь lines.
"""
if len(sys.argv) == 1:
    line_num = 0
else:
    if sys.argv[1] == "help":
        parsing.error_exit(0)
    try:
        line_num = int(sys.argv[1])
    except:
        parsing.error_exit(1)
    if(line_num <= 0):
        parsing.error_exit(1)

lines = {}

for i in range(line_num):
    ret = parsing.get_coords(input())
    lines[i] = ret

"""
Два особых случая - аргумент 0,
на который программа демонстрирует пример работы,
и аргумент 1, для которого невозможны
вычисления по алгоритму.
"""
if line_num == 0:
    lines = parsing.default_lines
    line_num = 5
    print('\n Пример работы программы.\n'
            ' Чтобы узнать обо всех функциях,\n'
            ' Запустите программу с аргументом "help".\n')
    for i in range(len(lines)):
        print(f"{lines[i][0]} -"
            " ({x}, {y})".format(x=lines[i][1][0], y=lines[i][1][1]))

elif line_num == 1:
    print()
    output.print_format(lines[0][0], lines[0][1], 0.0, "")
    print(f"\n Кратчайшее возможное расстояние: {0.0}")
    exit()

table = fill_table(lines)

"""
Вычисляем длину каждой из пермутаций пути,
находим минимальную длину и выводим результат.
"""
combs = permutations(range(1,line_num), line_num - 1)
res = tuple()
min_run = float("inf")
for comb in combs:
    run = whole_run(table, comb)
    if run < min_run:
        min_run = run
        res = comb

output.print_results(lines, res, table)
print(f"\n Кратчайшее возможное расстояние: {min_run}")