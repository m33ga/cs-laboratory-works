from des.des_key_plus import DESKeyPlus


def main():
    while True:
        try:
            key = input("Enter DES key (8 characters): ")

            if len(key) != 8:
                print(
                    f"Error: Key must be exactly 8 characters. You entered {len(key)} characters."
                )
                print()
                continue

            print()
            des = DESKeyPlus(key)
            des.calculate_k_plus()
            break

        except KeyboardInterrupt:
            print("\n\nProgram terminated by user.")
            break
        except Exception as e:
            print(f"Error: {e}")
            print()


if __name__ == "__main__":
    main()
