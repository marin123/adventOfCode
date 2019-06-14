f=open("input_day_6.txt", "r")
# print(f.read())
coordinates=[]
grid = [[0] * 500 for i in range(500)]
index = 1
locations=[]
for line in f:
    x = line.split()[0][:-1]
    y = line.split()[1]
    coordinates.append([index, int(x), int(y)])
    locations.append(index)
    index += 1
total_size=0
for i in range(0, 500):
    for j in range(0, 500):
        total_distance=0
        for coordinate in coordinates:
            distance = abs(coordinate[1] - i) + abs(coordinate[2] - j)
            total_distance += distance
        if total_distance < 10000:
            grid[i][j]=1
            total_size += 1
print(total_size)


