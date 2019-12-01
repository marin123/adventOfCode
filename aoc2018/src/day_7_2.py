f = open("input_day_7.txt", "r")
#workers = [0, 0]
workers = [0,0,0,0,0]
base_time = 61
file_input = []
file_input_0 = []
file_input_1 = []
alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
#alphabet = ["A", "B", "C", "D", "E", "F"]
time=0
for line in f:
    input_line = line.split()
    file_input.append((input_line[1], input_line[7]))
    file_input_1.append(input_line[7])
print(file_input)
finished_steps = []
progress_steps = ['', '', '', '', '']
#progress_steps = ['', '']
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
while len(finished_steps) < 26:
    for i in range(0, len(workers)):
        if workers[i] == 0:
            if progress_steps[i] != '':
                finished_steps.append(progress_steps[i])
                progress_steps[i] = ''
            for key in dict_instr:
                if set(dict_instr[key]) <= set(finished_steps) and key not in finished_steps and key not in candidate_steps and key not in progress_steps:
                    candidate_steps.append(key)
            # print(progress_steps, i, len(candidate_steps))
            #print(1,candidate_steps, progress_steps, finished_steps, workers)
            candidate_steps.sort()
            if len(candidate_steps) > 0:
                # print("test")
                progress_steps[i] = candidate_steps[0]
                workers[i] = base_time + alphabet.index(candidate_steps[0])
                candidate_steps.pop(0)
            #print(2,candidate_steps, progress_steps, finished_steps, workers)

    time += 1
    workers[:] = [x - 1 if x > 0 else 0 for x in workers]
    print(candidate_steps, progress_steps, finished_steps, workers, time)

print(finished_steps, time)
