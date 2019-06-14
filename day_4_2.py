f = open("all_output.txt", "r")
minutes = [ [0]*60 for i in range(3542)]
# print(minutes)
for line in f:
    # print(line)
    line = line.split(",")

    guard=int(line[0])
    start_min = int(line[1])
    end_min = int(line[2])
    for i in range(start_min, end_min):
        minutes[guard][i]+=1
max_overall=0
pos_guard=0
for i in range(0, 3542):
    max_guard=max(minutes[i])
    if max_guard > max_overall:
        pos_guard = i
        max_overall = max_guard
print(pos_guard, max_overall)

print(minutes[1733])

