from caesar.caesar_cipher import CaesarCipher


def main():
    cipher = CaesarCipher()

    while True:
        print("\n--- Caesar Cipher ---")
        print("1. Encrypt message")
        print("2. Decrypt message")
        print("0. Exit")

        choice = input("Choose an option (1-3): ").strip()

        if choice == "0":
            print("Goodbye!")
            break
        elif choice in ["1", "2"]:
            operation = "encrypt" if choice == "1" else "decrypt"

            try:
                message = input(f"Enter message to {operation}: ").strip()

                print("\nChoose key type:")
                print("1. Simple key (offset only)")
                print("2. Complex key (offset + key string)")

                key_choice = input("Choose key type (1-2): ").strip()

                if key_choice == "1":
                    offset = int(input("Enter offset (integer): ").strip())
                    result = (
                        cipher.encrypt(message, offset)
                        if operation == "encrypt"
                        else cipher.decrypt(message, offset)
                    )
                    print(f"Result: {result}")

                elif key_choice == "2":
                    offset = int(input("Enter offset (integer): ").strip())
                    key_string = input(
                        "Enter key string (minimum 7 characters): "
                    ).strip()
                    result = (
                        cipher.encrypt(message, offset, key_string)
                        if operation == "encrypt"
                        else cipher.decrypt(message, offset, key_string)
                    )
                    print(f"Result: {result}")

                else:
                    print("Error: Invalid key type choice")

            except ValueError as e:
                print(f"Error: {e}")
            except Exception as e:
                print(f"Error: Invalid input format {e}")
        else:
            print("Error: Invalid option choice")


if __name__ == "__main__":
    main()
