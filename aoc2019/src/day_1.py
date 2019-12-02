def get_data(path):
    with open(path, 'r') as f:
        data = f.readlines()
    return data


def get_total_mass(path):
    data = get_data(path)
    data_clean = [int(s.strip("\n")) for s in data]
    mass = [int(d / 3) - 2 for d in data_clean]
    total_mass = sum(mass)
    return total_mass


def recursive_fuel(mass):
    total_fuel = 0
    rest_of_mass = mass
    while rest_of_mass > 8:
        added_fuel = int(rest_of_mass / 3) - 2
        total_fuel += added_fuel
        rest_of_mass = added_fuel
    return total_fuel

def get_total_fuel_mass(path):
    data = get_data(path)
    data_clean = [int(s.strip("\n")) for s in data]
    mass = [recursive_fuel(d) for d in data_clean]
    total_mass = sum(mass)
    return total_mass

mass_of_fuel_1 = get_total_mass("../data/input_1_1.txt")
mass_of_fuel_2 = get_total_fuel_mass("../data/input_1_1.txt")
print(f"Total mass for part 1 is {mass_of_fuel_1} \n"
      f"and the total mass for part 2 is {mass_of_fuel_2}")

