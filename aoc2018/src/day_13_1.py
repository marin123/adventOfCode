f = open("test_input_day_13.txt", "r")
tracks = list()
changes = list()
carts = list()
for index_line, line in enumerate(f):
    tracks.append(list(line)[0:-1])
    if ">" in list(line):
        carts.append([list(line).index(">"), index_line, l])
    if "<" in list(line):
        carts.append([list(line).index("<"), index_line, l])
    if "^" in list(line):
        carts.append([list(line).index("^"), index_line, l])
    if "v" in list(line):
        carts.append([list(line).index("v"), index_line, l])
        #print("found the cart")
    # print(line, tracks)
new_tracks = tracks
print(carts)
for index_x, field_x in enumerate(tracks):
    for index_y, field_y in enumerate(tracks):
        current_field = tracks[index_x][index_y]
        if current_field == ">":
            next_field = tracks[index_x+1][index_y]
            if next_field == "-":
                new_tracks[index_x][index_y] = "-"
                new_tracks[index_x+1][index_y] = ">"
            if next_field == "\\":
                new_tracks[index_x][index_y] = "-"
                new_tracks[index_x + 1][index_y] = "v"



# find the carts
