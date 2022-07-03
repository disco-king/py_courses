from .computations import distance


def print_results(lines, res, table):
    '''
    Вывод результатов работы программы в цикле.
    Условия в начале и конце тела цикла обрабатывают
    особые случаи: начало и конец пути.
    В обоих из них участвует "почтовое отделение",
    которое не включено в пермутацию набора точек.
    '''
    print(f"\n Итоговая последовательность: 0 ", end="")
    for r in res:
        print(r, end=" ")
    print(0, "\n")

    dst = 0.0
    ending = "->"

    for i in range(-1, len(res)+1):
        if i == -1 or i == len(res):
            location = lines[0][0]
            coordinates = lines[0][1]
        else:
            location = lines[res[i]][0]
            coordinates = lines[res[i]][1]

        print_format(location, coordinates, dst, ending)

        if i == -1:
            dst = table[0][res[0]]
        elif i == len(res)-1:
            ending = ""
            dst += table[0][res[i]]
        elif i < len(res):
            dst += table[res[i]][res[i+1]]


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
