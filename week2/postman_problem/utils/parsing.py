
def get_coords(string):
    """
    Точка входа в часть программы, отвечающую за парсинг.
    Функция принимает входную строку и возвращает список
    из опционального адреса и кортежа с координатами точки.
    """
    if len(string) == 0:
        error_exit(1)

    string = string.lstrip(" 123456789.")
    
    if string.startswith("("):
        return ["", get_nums(string)]
    if " – " in string:
        delim = " – "
    elif " - " in string:
        delim = " - "
    else:
        error_exit(2)

    halves = string.split(delim, 1)

    halves[0] = halves[0].strip()
    halves[1] = get_nums(halves[1])
    return halves


def get_nums(string):
    """
    Функция принимает на вход строку,
    содержащую координаты точки, и возвращает
    кортеж с координатами в дробных числах.
    """
    string = string.strip()

    if string.startswith("(") and string.endswith(")"):
        string = string[1:-1]
    else:
        error_exit(2)

    try:
        ret = tuple([float(i.strip()) for i in string.split(",")])
    except:
        error_exit(3)

    if len(ret) != 2:
        error_exit(3)
    return ret


def error_exit(code):
    """
    Вывод сообщения об ошибке и завершение программы
    """
    print()
    if code == 0:
        print("\n Для вычисления кратчайшего расстояния\n"
        " введите целое число в качестве аргумента,\n"
        " а затем введите координаты точек пути\n"
        " в отдельных строках в виде:\n"
        " [адрес] - (x, у)\n"
        " либо просто (х, у), например:\n\n"
        " $> python3 postman.py 3\n"
        " ул. Зощенко, д. 5 - (0, 4)\n"
        " Бухарестская пл., д. 70 к. 3 - (10, 7)\n"
        " с. Васильково, д.18 - (-5, 2)\n")
        exit()

    print(" Ошибка:", end="")
    if code == 1:
        print(" Неправильное количество точек пути")
    elif code == 2:
        print(" Неправильный формат точки пути")
    elif code == 3:
        print(" Неправильная координата точки пути")

    print("\n Запустите программу с аргументом \"help\""
            " для получения подробных инструкций.")
    exit()


"""
Набор точек для тестового запуска.
"""
default_lines = {
    0: ['Почтовое отделение', (0, 2)],
    1: ['Ул. Грибоедова, 104/25', (2, 5)],
    2: ['Ул. Бейкер стрит, 221б', (5, 2)],
    3: ['Ул. Большая Садовая, 302-бис', (6, 6)],
    4: ['Вечнозелёная Аллея, 742', (8, 3)]
    }


if __name__ == "__main__":
    """
    Скрипт для тестирования
    функций парсинга в отдельности
    """
    string = input()
    result = get_coords(string)
    if result[0]:
        print(f"coords for {result[0]}: {result[1]}")
    else:
        print(f"coords: {result[1]}")
