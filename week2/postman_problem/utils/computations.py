
def distance(point_1, point_2) -> float:
    """
    Функция вычисляет расстояние между двумя точками
    """
    return ((point_2[0] - point_1[0]) ** 2
            + (point_2[1] - point_1[1]) ** 2) ** 0.5


def fill_table(points):
    table = {}
    for main in range(len(points)):
        table[main] = {}
        for sub in range(len(points)):
            table[main][sub] = distance(points[main][1], points[sub][1])
    return table


def whole_run(table, points):
    """
    Функция вычисляет длину всего маршрута
    """
    total = float()

    for i in range(len(points)-1):
        total += table[i][i+1]
    total += table[0][points[0]] + table[0][points[-1]]

    return total

