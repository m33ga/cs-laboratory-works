from labs.lab1.main import main as lab1
from labs.lab3.main import main as lab3
from labs.lab4.main import main as lab4


def main():
    while True:
        print("Available Labs:")
        print("1. Caesar Cipher Console")
        print("3. Playfair Cipher Console")
        print("4. DES K+")
        print("0. Exit")
        try:
            choice = input("\nSelect a lab to run: ").strip()

            if choice == "1":
                lab1()
            elif choice == "3":
                lab3()
            elif choice == "4":
                lab4()
            elif choice == "0":
                break
            else:
                print("Invalid choice.")
        except Exception as e:
            print(f"Error running lab: {e}")


if __name__ == "__main__":
    main()
