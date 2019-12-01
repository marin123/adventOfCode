f = open("input_day_12.txt", "r")
extra_space_size = 100000
plants = list()
new_plants = list()
first_line = f.readline().split(":")[1][1:-1]
input_size = len(first_line)
f.readline()  # skip empty line
rules = list()
for line in f:
    rule = line.split("=>")
    rule_left = rule[0][:-1]
    rule_right = rule[1][1:][0]
    rules.append((rule_left, rule_right))
for i in range(0, 2*extra_space_size + input_size):
    if i < extra_space_size or i >extra_space_size + len(first_line)-1:
        plants.append(".")
    else:
        #print(i)
        plants.append(first_line[i - extra_space_size])
print(rules)
generations = 250000000000
for j in range(0, generations):
    if j%1000000000 == 0:
        print(j)
    for i in range(0, extra_space_size - 2):
        new_plants.append(".")
    rule_match = 0
    for i in range(extra_space_size - 2, 2*extra_space_size + input_size -2):
        sub_plants = plants[i-2:i+3]
        string_plants = ''.join(str(e) for e in sub_plants)
        for single_rule in rules:
            # print(string_plants, single_rule)
            if string_plants == single_rule[0]:
                # print("match")
                new_plants.append(single_rule[1])
                rule_match = 1
                break
        if rule_match == 0:
            new_plants.append(plants[i])
        else:
            rule_match = 0
    for i in range(0, 2):
        new_plants.append(".")

    plants = new_plants
    sum_pots = 0
    starting_pot = -extra_space_size
    count_pots = 0
    for plant in plants:
        if plant == "#":
            #print(starting_pot)
            count_pots += 1
            sum_pots += starting_pot
        starting_pot += 1
    print(j, sum_pots - j*80, len(plants), count_pots)
    new_plants = list()
print(plants)
print(new_plants)
sum_pots = 0
starting_pot = -extra_space_size
for plant in plants:
    if plant == "#":
        sum_pots += starting_pot
    starting_pot += 1
print(sum_pots,starting_pot)
    # print(array)
# print(first_line)
# print(plants)
# print(rules)
