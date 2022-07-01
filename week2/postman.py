from itertools import permutations as func
from computations import whole_run

points = [(1,1), (4,1), (1,5)]
# points = [(1,1), (2,2), (3,3), (4,4)]
# points = [(1,1), (2,2), (3,3), (4,4), (5,5)]
# points = [(0,2), (2,5), (5,2), (6,6), (8,3)]

combs = func(points[1:], len(points) - 1)
min = 1000.0
for i in combs:
    run = whole_run(points[0], i)
    print(f"run distance for {i} is {run}")
    if run < min:
        min = run

print('\n\n', "minimal:", min)