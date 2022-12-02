from .CalcInArray import CalcInArray


class Diagnostic:
    def get_gamma_bit(bits):
        lenght = len(bits)
        z = bits.count("0")
        if z > lenght / 2:
            return "0"
        return "1"

    def get_epsilon_bits(gamma):
        epsilon = []
        for b in gamma:
            if b == "0":
                epsilon.append("1")
            else:
                epsilon.append("0")
        return "".join(epsilon)

    def get_gamma_bits(seq):
        gamma = []
        for i in range(len(seq[0])):
            to_send = []
            for s in seq:
                to_send.append(s[i])
            gamma.append(Diagnostic.get_gamma_bit(to_send))
        return "".join(gamma)

    def get_oxy__bit(bits, defaut):
        lenght = len(bits)
        z = bits.count("0")
        if z == lenght / 2:
            return defaut
        if z > lenght / 2:
            return "0"
        return "1"

    def get_co2__bit(bits, defaut):
        lenght = len(bits)
        z = bits.count("0")
        if z == lenght / 2:
            return defaut
        if z < lenght / 2:
            return "0"
        return "1"

    def get_oxygen_bits(seq):
        oxy = []
        new_seq = seq
        for i in range(len(seq[0]) + 1):
            if len(new_seq) > 1:
                bit_seq = [s[i] for s in new_seq]
                bit_to_test = Diagnostic.get_oxy__bit(bit_seq, "1")
                new_seq = CalcInArray.kept_bits_with_x_in_position_y(
                    new_seq, bit_to_test, i
                )
        return new_seq

    def get_CO2_bits(seq):
        co2 = []
        new_seq = seq
        for i in range(len(seq[0])):
            if len(new_seq) > 1:
                bit_seq = [s[i] for s in new_seq]
                bit_to_test = Diagnostic.get_co2__bit(bit_seq, "0")
                new_seq = CalcInArray.kept_bits_with_x_in_position_y(
                    new_seq, bit_to_test, i
                )
        return new_seq
