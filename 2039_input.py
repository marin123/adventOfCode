f = open("2039_input.txt", "r")
minutes = [0]*60
for line in f:
    line = line.split(" ")
    print(line)
    start_min = int(line[1])
    end_min = int(line[2])
    for i in range(start_min, end_min):
        minutes[i]+=1
print(minutes)
