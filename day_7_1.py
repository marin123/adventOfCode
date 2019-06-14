f = open("input_day_7.txt", "r")
file_input = []
file_input_0 = []
file_input_1 = []
alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
for line in f:
    input_line = line.split()
    file_input.append((input_line[1], input_line[7]))
    file_input_1.append(input_line[7])
print(file_input)
finished_steps = []
candidate_steps = []
for element in alphabet:
    if element not in file_input_1:
        candidate_steps.append(element)
print(candidate_steps)
dict_instr = {}
for line in file_input:
    if line[1] in dict_instr:
        dict_instr[line[1]].append(line[0])
    else:
        dict_instr[line[1]] = [line[0]]
print(dict_instr)
while len(finished_steps) < 27:
    print(finished_steps, candidate_steps)
    candidate_steps.sort()
    finished_steps.append(candidate_steps[0])
    candidate_steps.pop(0)
    for key in dict_instr:
        if set(dict_instr[key]) < set(finished_steps) and key not in finished_steps and key not in candidate_steps:
            candidate_steps.append(key)
print(finished_steps)







