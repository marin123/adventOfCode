import itertools
def get_data(path):
    with open(path, 'r') as f:
        data = f.readlines()
    return data


def sum_elements(pos1, pos2, pos, data_list):
    data_list[pos] = data_list[pos1] + data_list[pos2]
    return data_list


def multiply_elements(el1, el2, pos, data_list):
    data_list[pos] = data_list[el1] * data_list[el2]
    return data_list


def program_out(noun, verb, data_list_o):
    i = 0
    data_list = [a for a in data_list_o]
    data_list[1] = noun
    data_list[2] = verb
    while i < len(data_list_o):
        program = data_list[i:i+4]
        if program[0] == 1:
            data_list = sum_elements(program[1], program[2], program[3], data_list)
        elif program[0] == 2:
            data_list = multiply_elements(program[1], program[2], program[3], data_list)
        if data_list[i+4] == 99:
            return data_list[0]
            break
        i += 4
    return data_list[0]


data_list_0 = [int(a) for a in get_data("../data/input_2.txt")[0].split(",")]
#data_list_0 = [1,1,1,4,99,5,6,0,99]

for pair in itertools.product(range(0, 100), repeat=2):
    if program_out(pair[0], pair[1], data_list_0) == 19690720:
        print(pair[0], pair[1])


