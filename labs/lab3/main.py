from playfair.playfair import PlayfairCipher


class PlayfairApp:
    def __init__(self):
        self.cipher = PlayfairCipher()

    def display_matrix(self):
        print("\nencryption matrix:")
        for row in self.cipher.matrix:
            print(" ".join(row))
        print()

    def run(self):
        print("=== playfair algorithm for the romanian language ===")
        print("alphabet: a-z with diacritics (ă, â, î, ș, ț)")
        print("allowed letters: a-z, a-z (30 letters, letter j removed)\n")

        while True:
            print("\n" + "=" * 50)
            operation = input(
                "choose operation (1-encrypt, 2-decrypt, 0-exit): "
            ).strip()

            if operation == "0":
                print("goodbye!")
                break

            if operation not in ["1", "2"]:
                print("invalid option!")
                continue

            key = input("enter key (minimum 7 characters): ").strip()

            if len(key) < 7:
                print("error: the key must contain at least 7 characters!")
                continue

            if not self.cipher.validate_input(key):
                print("error: the key contains invalid characters!")
                print("use only letters a-z, a-z with diacritics (ă, â, î, ș, ț)")
                continue

            self.cipher.create_matrix(key)
            self.display_matrix()

            if operation == "1":
                text = input("enter the message to encrypt: ").strip()

                if not self.cipher.validate_input(text):
                    print("error: the message contains invalid characters!")
                    print("use only letters a-z, a-z with diacritics (ă, â, î, ș, ț)")
                    continue

                prepared = self.cipher.prepare_text(text)
                print("\nprepared text (in pairs): ", end="")
                for i in range(0, len(prepared), 2):
                    if i + 1 < len(prepared):
                        print(f"{prepared[i]}{prepared[i + 1]} ", end="")
                print()

                result = self.cipher.encrypt(text)
                print(f"\nciphertext: {result}")

                formatted = " ".join(
                    [result[i : i + 2] for i in range(0, len(result), 2)]
                )
                print(f"ciphertext (formatted): {formatted}\n")

            else:
                text = input("enter the ciphertext to decrypt: ").strip()

                if not self.cipher.validate_input(text):
                    print("error: the ciphertext contains invalid characters!")
                    print("use only letters a-z, a-z with diacritics (ă, â, î, ș, ț)")
                    continue

                result = self.cipher.decrypt(text)
                print(f"\ndecrypted message: {result}")


def main():
    app = PlayfairApp()
    app.run()


if __name__ == "__main__":
    main()
