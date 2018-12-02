def differences_between_strings(string_1, string_2):
    differences = 0
    for i in range(0, len(string_2)-1):
        if string_1[i] != string_2[i]:
            differences += 1
        i += 1
    return differences


f = open("input_day_2.txt", "r")
file_list = []
for line in f:
    file_list.append(line)
for line_1 in file_list:
    for line_2 in file_list:
        if differences_between_strings(line_1, line_2) == 1:
            print(line_1, line_2)
        # print(line_1,line_2, len(line_1), len(line_2), differences_between_strings(line_1,line_2))
