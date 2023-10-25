def main():
    option = -1
    password = ""
    new_pass = ""
    while option != 3:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print()
        option = int(input("Please enter an option: "))

        if option == 1:
            password = int(input("Please enter you password to encode: "))
            print("Your password has been encoded and stored!")
        elif option == 2:
            new_pass = encode(password)
            print(f'The encoded password is {new_pass}, and the original password is {decode(new_pass)}.')
        elif option == 3:
            break

def encode(passw):
    return passw + 33333333

def decode(pass_new):
    return pass_new - 33333333

main()
