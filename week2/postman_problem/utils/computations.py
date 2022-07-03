
def distance(point_1, point_2) -> float:
    """
    Вычисление расстояния между двумя точками
    """
    return ((point_2[0] - point_1[0]) ** 2
            + (point_2[1] - point_1[1]) ** 2) ** 0.5


def fill_table(points):
    """
    Заполнение словаря списками со значениями расстояний.
    В каждом списке по индексу х находится расстояние
    до точки с индексом х в исходном наборе.
    """
    table = {}
    for main in range(len(points)):
        table[main] = {}
        for sub in range(len(points)):
            table[main][sub] = distance(points[main][1], points[sub][1])
    return table


def whole_run(table, points):
    """
    Вычисление длины всего маршрута.
    Элементы кортежа points (индексы точек пути)
    используются в качестве ключей для словаря table
    """
    total = float()

    for i in range(len(points)-1):
        total += table[points[i]][points[i+1]]
    total += table[0][points[0]] + table[0][points[-1]]

    return total
