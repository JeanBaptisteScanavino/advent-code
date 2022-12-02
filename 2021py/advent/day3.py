from utils.utils import *


def read_input_file():
    return InputReader.read_file("day_3.txt")


def exec_1(file):
    gamma = Diagnostic.get_gamma_bits(file)
    epsilon = Diagnostic.get_epsilon_bits(gamma)
    return ClassicCalc.get_decimal_from_bin(gamma) * ClassicCalc.get_decimal_from_bin(
        epsilon
    )


def exec_2(file):
    oxy = Diagnostic.get_oxygen_bits(file)
    co2 = Diagnostic.get_CO2_bits(file)
    return ClassicCalc.get_decimal_from_bin(oxy[0]) * ClassicCalc.get_decimal_from_bin(
        co2[0]
    )


file = read_input_file()
result_1 = exec_1(file)
print("exo_1:", result_1)
result_2 = exec_2(file)
print("exo_1:", result_2)
