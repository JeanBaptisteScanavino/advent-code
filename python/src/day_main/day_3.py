from utils.utils import make_int, read_file

day = 3
input_path = f"/input/input_day_{day}.txt"


def get_bits(bits):
    return [bit for bit in bits]


def most_bit(input):
    count_zero = 0
    for element in input:
        if element == "0":
            count_zero += 1
    if count_zero > len(input) / 2:
        return "0"
    return "1"


def most_bit_with_count(input):
    count_zero = 0
    for element in input:
        if element == "0":
            count_zero += 1
    if count_zero > len(input) / 2:
        return {"most": "0", "count": count_zero}
    return {"most": "1", "count": len(input) - count_zero}


def inverse_table(input):
    inverse = []
    for bit in input:
        if bit == "0":
            inverse.append("1")
        else:
            inverse.append("0")
    return inverse


def find_power(array_of_data):
    gamma_rate_table = []
    for x in range(0, len(array_of_data[0])):
        gamma_rate_table.append(most_bit([data[x] for data in array_of_data]))
    epsilon_rate_table = inverse_table(gamma_rate_table)
    gamma_rate = int(("").join(gamma_rate_table), 2)
    epsilon_rate = int(("").join(epsilon_rate_table), 2)
    return gamma_rate * epsilon_rate


def find_oxygen(array_of_data):
    i = 0
    while len(array_of_data) > 1:
        most_and_count = most_bit_with_count([data[i] for data in array_of_data])
        array_of_data = [
            byte for byte in array_of_data if byte[i] == most_and_count["most"]
        ]
        if len(array_of_data) == 1:
            break
        array_of_data = array_of_data[0 : most_and_count["count"]]
        i += 1
    return int(("").join(array_of_data[0]), 2)


def find_C02(array_of_data):
    i = 0
    while len(array_of_data) > 1:
        most_and_count = most_bit_with_count([data[i] for data in array_of_data])
        array_of_data = [
            byte for byte in array_of_data if byte[i] != most_and_count["most"]
        ]
        if len(array_of_data) == 1:
            break
        array_of_data = array_of_data[0 : most_and_count["count"]]
        i += 1
    return int(("").join(array_of_data[0]), 2)


def find_life_support(array_of_data):
    return find_oxygen(array_of_data) * find_C02(array_of_data)


def main(input_file):
    input_data = read_file(input_file)
    array_of_data = [get_bits(data) for data in input_data]
    power = find_power(array_of_data)
    life = find_life_support(array_of_data)
    return {"power": power, "life": life}


print(main(input_path))
