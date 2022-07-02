
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
            val = distance(points[main], points[sub])
            table[main][sub] = val
    return table


def whole_run(table, points):
    """
    Функция вычисляет длину всего маршрута
    """
    total = float()

    for i in range(len(points)-1):
        total += table[i][i+1]
        # if total > minn:
        #     return total
    total += table[0][points[0]] + table[0][points[-1]]

    return total

