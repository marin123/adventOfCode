f = open("input.txt", "r")
output = 0
for line in f:
    output += int(line)
print(output)
