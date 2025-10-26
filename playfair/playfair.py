class PlayfairCipher:
    def __init__(self):
        self.alphabet = "AĂÂBCDEFGHIÎKLMNOPQRSȘTȚUVWXYZ"
        self.matrix = []
        self.rows = 6
        self.cols = 5

    def validate_input(self, text):
        for char in text.upper():
            if char not in self.alphabet and char != " ":
                return False
        return True

    def create_matrix(self, key):
        key = key.upper().replace(" ", "")
        seen = set()
        key_unique = []

        for char in key:
            if char not in seen and char in self.alphabet:
                seen.add(char)
                key_unique.append(char)

        for char in self.alphabet:
            if char not in seen:
                key_unique.append(char)

        self.matrix = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                idx = i * self.cols + j
                if idx < len(key_unique):
                    row.append(key_unique[idx])
            if row:
                self.matrix.append(row)

    def find_position(self, char):
        for i, row in enumerate(self.matrix):
            if char in row:
                return i, row.index(char)
        return None, None

    def prepare_text(self, text):
        text = text.upper().replace(" ", "")
        prepared = []
        i = 0

        while i < len(text):
            char1 = text[i]

            if i + 1 < len(text):
                char2 = text[i + 1]
                if char1 == char2:
                    prepared.append(char1)
                    if char1 not in ["X", "Z", "Q"]:
                        prepared.append("X")
                    elif char1 == "X":
                        prepared.append("Z")
                    elif char1 == "Z":
                        prepared.append("Q")
                    else:
                        prepared.append("X")
                    i += 1
                else:
                    prepared.append(char1)
                    prepared.append(char2)
                    i += 2
            else:
                prepared.append(char1)
                prepared.append("X")
                i += 1

        return "".join(prepared)

    def encrypt_pair(self, char1, char2):
        row1, col1 = self.find_position(char1)
        row2, col2 = self.find_position(char2)

        if row1 is None or row2 is None:
            return char1 + char2

        if row1 == row2:
            new_col1 = (col1 + 1) % len(self.matrix[row1])
            new_col2 = (col2 + 1) % len(self.matrix[row2])
            return self.matrix[row1][new_col1] + self.matrix[row2][new_col2]
        elif col1 == col2:
            new_row1 = (row1 + 1) % len(self.matrix)
            new_row2 = (row2 + 1) % len(self.matrix)
            return self.matrix[new_row1][col1] + self.matrix[new_row2][col2]
        else:
            return self.matrix[row1][col2] + self.matrix[row2][col1]

    def decrypt_pair(self, char1, char2):
        row1, col1 = self.find_position(char1)
        row2, col2 = self.find_position(char2)

        if row1 is None or row2 is None:
            return char1 + char2

        if row1 == row2:
            new_col1 = (col1 - 1) % len(self.matrix[row1])
            new_col2 = (col2 - 1) % len(self.matrix[row2])
            return self.matrix[row1][new_col1] + self.matrix[row2][new_col2]
        elif col1 == col2:
            new_row1 = (row1 - 1) % len(self.matrix)
            new_row2 = (row2 - 1) % len(self.matrix)
            return self.matrix[new_row1][col1] + self.matrix[new_row2][col2]
        else:
            return self.matrix[row1][col2] + self.matrix[row2][col1]

    def encrypt(self, text):
        prepared = self.prepare_text(text)
        result = []

        for i in range(0, len(prepared), 2):
            if i + 1 < len(prepared):
                result.append(self.encrypt_pair(prepared[i], prepared[i + 1]))

        return "".join(result)

    def decrypt(self, text):
        text = text.upper().replace(" ", "")
        result = []

        for i in range(0, len(text), 2):
            if i + 1 < len(text):
                result.append(self.decrypt_pair(text[i], text[i + 1]))

        return "".join(result)
