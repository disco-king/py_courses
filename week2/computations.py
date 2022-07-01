

def distance(point_1, point_2) -> float:
    return ((point_2[0] - point_1[0]) ** 2
            + (point_2[1] - point_1[1]) ** 2) ** 0.5


def whole_run(base, points):
    total = float()

    for i in range(len(points)-1):
        total += distance(points[i], points[i+1])
    # print(f" distance without base {total}")
    total += distance(base, points[0]) + distance(base, points[-1])
    return total

