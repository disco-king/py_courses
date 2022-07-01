

def get_coords(string):
    string = string.lstrip(" 123456789.")
    
    if "–" in string:
        delim = "–"
    elif "-" in string:
        delim = "-"
    else:
        return ["", get_nums(string)]

    halves = string.split(delim)

    if len(halves) != 2:
        error_exit(1)

    halves[0] = halves[0].strip()
    halves[1] = get_nums(halves[1])
    return halves


def get_nums(string):
    string = string.strip()

    if string.startswith("(") and string.endswith(")"):
        string = string[1:-1]
    else:
        error_exit(1)

    try:
        ret = tuple([float(i.strip()) for i in string.split(",")])
    except:
        error_exit(1)

    if len(ret) != 2:
        error_exit(1)
    return ret


def error_exit(code):
    if(code == 1):
        print("Wrong input string")
    exit()


string = input()
result = get_coords(string)
if result[0]:
    print(f"numbers for {result[0]}: {result[1]}")
else:
    print(f"coords: {result[1]}")