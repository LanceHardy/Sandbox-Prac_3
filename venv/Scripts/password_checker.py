
MIN_LENGTH = 5


def main():
    print("Enter password")
    password = input()
    while password < MIN_LENGTH:
        print("Enter valid password")
        password = input()
    print("*" * len(password))
    print("Password accepted")


main()

