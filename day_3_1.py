def get_coordinates(input_line):
    x_0 = input_line.split()[2].split(",")[0]
    y_0 = input_line.split()[2].split(",")[1]
    y_0 = y_0[:-1]
    return int(x_0), int(y_0)


def get_dimensions(input_line):
    x = input_line.split()[3].split("x")[0]
    y = input_line.split()[3].split("x")[1]
    return int(x), int(y)


def cover_fabric(fabric, x_0, y_0, x, y):
    for i in range(x_0, x_0 + x):
        for j in range(y_0, y_0 + y):
            fabric[i][j] += 1
    return fabric


fabric = [[0] * 1000 for i in range(1000)]
f = open("input_day_3.txt", "r")
for line in f:
    x_0, y_0 = get_coordinates(line)
    x, y = get_dimensions(line)
    fabric = cover_fabric(fabric, x_0, y_0, x, y)
count_domain=0
for i in range(0, 1000):
    for j in range(0, 1000):
        if fabric[i][j] >= 2:
            count_domain += 1
print(count_domain)

# test_input = f.readline()
# test_split = test_input.split(' ')
# coordinates = test_split[2].split(",")[1]
# print(get_coordinates(test_input))
# print(get_dimensions(test_input))
# x_0, y_0 = get_coordinates(test_input)
# x, y = get_dimensions(test_input)
# fabric = cover_fabric(fabric, x_0, y_0, x, y)
# print(fabric[906][738])