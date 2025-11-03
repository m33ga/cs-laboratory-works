class DESKeyPlus:
    PC1 = [
        57,
        49,
        41,
        33,
        25,
        17,
        9,
        1,
        58,
        50,
        42,
        34,
        26,
        18,
        10,
        2,
        59,
        51,
        43,
        35,
        27,
        19,
        11,
        3,
        60,
        52,
        44,
        36,
        63,
        55,
        47,
        39,
        31,
        23,
        15,
        7,
        62,
        54,
        46,
        38,
        30,
        22,
        14,
        6,
        61,
        53,
        45,
        37,
        29,
        21,
        13,
        5,
        28,
        20,
        12,
        4,
    ]

    def __init__(self, key):
        if len(key) != 8:
            raise ValueError("Key must be exactly 8 characters")
        self.key = key
        self.key_bits = self._string_to_bits(key)

    def _string_to_bits(self, s):
        return [int(bit) for char in s for bit in f"{ord(char):08b}"]

    def _permute(self, bits, table):
        return [bits[i - 1] for i in table]

    def _format_bits(self, bits, group_size=8):
        result = ""
        for i in range(0, len(bits), group_size):
            if i > 0:
                result += " "
            result += "".join(str(b) for b in bits[i : i + group_size])
        return result

    def _print_table(self, name, table, cols):
        print(f"\n{name} table")
        for i in range(0, len(table), cols):
            row = table[i : i + cols]
            print(row)

    def calculate_k_plus(self):
        print(f"64 bit key in binary: {self._format_bits(self.key_bits, 8)}")

        self._print_table("apply permuted choice 1", self.PC1, 7)

        k_plus = self._permute(self.key_bits, self.PC1)

        print(f"\nK+ : {self._format_bits(k_plus, 7)}")

        return k_plus
