class CaesarCipher:
    def __init__(self):
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def _create_cipher_alphabet(self, offset, key_string=""):
        offset = offset % 26

        unique_key_chars = []
        seen = set()
        for char in key_string.upper():
            if char in self.alphabet and char not in seen:
                unique_key_chars.append(char)
                seen.add(char)

        remaining_chars = [char for char in self.alphabet if char not in seen]

        cipher_alphabet = "".join(unique_key_chars) + "".join(remaining_chars)
        shifted_alphabet = cipher_alphabet[offset:] + cipher_alphabet[:offset]
        print(f"Alphabet used: {shifted_alphabet}")
        return shifted_alphabet

    def encrypt(self, message, offset, key_string=""):
        if key_string:
            if len(key_string) < 7:
                raise ValueError("Key string must be at least 7 characters long")

        for char in message:
            if not (char.isalpha() or char.isspace()):
                raise ValueError("Message can only contain English letters and spaces")

        cipher_alphabet = self._create_cipher_alphabet(offset, key_string)
        result = []

        for char in message:
            if char.isalpha():
                char_upper = char.upper()
                pos = self.alphabet.index(char_upper)
                encrypted_char = cipher_alphabet[pos]
                result.append(encrypted_char)

        return "".join(result)

    def decrypt(self, message, offset, key_string=""):
        if key_string:
            if len(key_string) < 7:
                raise ValueError("Key string must be at least 7 characters long")

        for char in message:
            if not char.isalpha():
                raise ValueError("Encrypted message can only contain English letters")

        cipher_alphabet = self._create_cipher_alphabet(offset, key_string)
        result = []

        for char in message:
            if char.isalpha():
                char_upper = char.upper()
                pos = cipher_alphabet.index(char_upper)
                decrypted_char = self.alphabet[pos]
                result.append(decrypted_char)

        return "".join(result)
