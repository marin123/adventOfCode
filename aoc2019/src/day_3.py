def get_data(path):
    with open(path, 'r') as f:
        data = f.readlines()
    return data


def get_set(inst, start):
    direction = inst[0]
    step = int(inst[1:])
    if direction == "R":
        points = [(start[0] + i, start[1]) for i in range(1, step + 1)]
    if direction == "L":
        points = [(start[0] - i, start[1]) for i in range(1, step + 1)]
    if direction == "U":
        points = [(start[0], start[1] + i) for i in range(1, step + 1)]
    if direction == "D":
        points = [(start[0], start[1] - i) for i in range(1, step + 1)]
    return points


def get_points(line):
    points = [(0, 0)]
    for a in line:
        point = get_set(a, points[-1])
        points.extend(point)
    return points


def intersection(lst1, lst2):
    temp = set(lst2)
    lst3 = [value for value in lst1 if value in temp]
    return lst3


data = get_data("../data/input_3.txt")

line_1 = data[0].split(",")
line_2 = data[1].split(",")
points_1 = get_points(line_1)
points_2 = get_points(line_2)
intersections = intersection(points_1, points_2)
inter_wo_zero = intersections[1:]
min_distance = min([abs(a[0]) + abs(a[1]) for a in inter_wo_zero])
find_min_steps= min([int(points_1.index(el)) + int(points_2.index(el)) for el in inter_wo_zero])
print(find_min_steps)
print(min_distance)
