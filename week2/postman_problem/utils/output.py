from .computations import distance


def print_results(lines, res, base):
    '''
    Вывод результатов работы программы в цикле.
    Условия в начале и конце тела цикла обрабатывают
    особые случаи: начало и конец пути.
    В обоих из них участвует "почтовое отделение",
    которое не включено в общий набор точек.
    '''
    print()
    dst = 0.0
    ending = "->"

    for i in range(-1, len(res)+1):
        if i == -1 or i == len(res):
            location = lines[base]
            coordinates = base
        else:
            location = lines[res[i]]
            coordinates = res[i]

        print_format(location, coordinates, dst, ending)

        if i == -1:
            dst = distance(base, res[0])
        elif i == len(res)-1:
            ending = ""
            dst += distance(res[i], base)
        elif i < len(res):
            dst += distance(res[i], res[i+1])


def print_format(location, coordinates, dst, ending):
    """
    Форматированный вывод названия, координат
    и пройденного расстояния для данной точки пути.
    Оффсет для названия зависит от того,
    имеет ли оно длину больше нуля.
    """
    offset = 30 if len(location) else 0

    print(f" {location.ljust(offset)}", end=" ")
    print(str(coordinates).ljust(15), end=" ")
    print(f"пройдено {dst} {ending}")

"""
Набор точек для тестового запуска.
"""
default_points = [(0,4), (10,7), (5,-2)]
default_lines = {
    default_points[0]: "ул. Зощенко, д. 5",
    default_points[1]: "Бухарестская пл., д. 70 к. 3",
    default_points[2]: "с. Васильково, д.18"
    }