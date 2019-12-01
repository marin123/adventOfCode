def get_data(path):
    with open('../data/input_1_1.txt', 'r') as f:
        data = f.readlines()
    return data

def get_total_mass(path):
    data = get_data(path)
    data_clean = [int(s.strip("\n")) for s in data]
    mass = [int(d / 3) - 2 for d in data_clean]
    total_mass = sum(mass)
    return total_mass


total_mass = get_total_mass("../data/input_1_1.txt")
print(total_mass)

