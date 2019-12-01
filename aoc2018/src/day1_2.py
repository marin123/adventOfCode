f = open("input.txt", "r")
output = 0
list_of_outputs = set()
file = []
for line in f:
    file.append(int(line))
# print(file)
line_of_file = 0
length_of_file = len(file)
while True:
    output += file[line_of_file]
    if line_of_file == length_of_file - 1:
        line_of_file = 0
    else:
        line_of_file += 1
    if output not in list_of_outputs:
        list_of_outputs.add(output)
        # print(output)
    else:
        break
print(output)
