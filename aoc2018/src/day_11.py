
def get_power_level(x, y, grid_ser_no):
    rack_id = x + 10
    #print(rack_id)
    power_level = rack_id * y
    #print(power_level)
    power_level += grid_ser_no
    power_level *= rack_id
    power_level_str = str(power_level)
    #print(power_level_str)
    hundreds=int(power_level_str[-3])
    #print()
    power_level_out= hundreds - 5
    return power_level_out

size = 300
grid_serial = 6042
power_cell_grid=[[0 for i in range(size)] for j in range(size)]

print(power_cell_grid)
for i in range(size):
    for j in range(size):
        power_cell_grid[i][j] = get_power_level(i, j, grid_serial)
print(power_cell_grid)
max_power_sum=0
power_sum=0
max_size=0
size_square=1
max_location=[0,0]
for size_square in range (1, size):
    for i in range(size-size_square + 1):
        for j in range(size-size_square + 1):
            for k in range(size_square):
                for l in range(size_square):
                    power_sum += power_cell_grid[i+k][j+l]
            if power_sum > max_power_sum:
                max_power_sum = power_sum
                max_location = [i, j]
                max_size=size_square
            power_sum=0
    print(max_size, max_location)
print(max_power_sum, max_location, max_size)

