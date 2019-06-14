f=open("input_day_6.txt", "r")
# print(f.read())
coordinates=[]
grid = [[-1] * 500 for i in range(500)]
index = 1
for line in f:
  x = line.split()[0][:-1]
  y = line.split()[1]
  coordinates.append([index, int(x), int(y)])
  index += 1
#coordinates=[[1,1, 1],[2,1, 6],[3,8, 3],[4,3, 4],[5,5, 5],[6,8, 9]]
#alt_infinite_coordinates=set()
for i in range(0, 500):
    for j in range(0, 500):
        closest_point = -1
        #no_closest_points = 0
        min_distance=10000
        for coordinate in coordinates:
            distance = abs(coordinate[1] - i) + abs(coordinate[2] - j)
            if distance < min_distance:
                min_distance = distance
                #no_closest_points = 1
                closest_point = coordinate[0]
                #alt_infinite_coordinates.add(coordinate[0])
                #print(min_distance)
                #print(closest_point)
            else:
                if distance == min_distance:
                    #no_closest_points += 1
                    #alt_infinite_coordinates.add(coordinates[0])
                    closest_point = -1
        #print(closest_point)
        grid[i][j] = closest_point
#print(grid)
x_infinity = []
x_0_infinity = []
y_0_infinity=[]
y_infinity = []
for i in range(0, 500):
    x_0_infinity.append(grid[i][0])
    y_0_infinity.append(grid[0][i])
    x_infinity.append(grid[i][499])
    y_infinity.append(grid[499][i])
x_infinity=set(x_infinity)
y_infinity=set(y_infinity)
x_0_infinity=set(x_0_infinity)
y_0_infinity=set(y_0_infinity)
print(x_infinity, y_infinity)
infinite_points = x_infinity | y_infinity |x_0_infinity| y_0_infinity
print(infinite_points)
max_size=0
size=0
int_coordinates=[]
for i in range(0, len(coordinates)):
    int_coordinates.append(coordinates[i][0])
#int_coordinates=coordinates[:]
print(int_coordinates)
#sizes=[]
for location in int_coordinates:
    size = 0
    if location not in infinite_points:
        for i in range(0,500):
            for j in range(0, 500):
                if grid[i][j] == location:
                    size += 1
                    #print(size, location)
                    #if location == 5:
    if size > max_size:
        max_size = size
        print(location)
print(max_size)
#print(grid[:15][:15])
            #print(distance)

