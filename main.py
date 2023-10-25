'''
    Author: jfonsing
    Date: 10/25/2023
    Project: Lab 6: Git
    Description: A lab demonstrating the purpose and usefullness of version control
    Collaborators: Henry Perlstein, Jenna Fonsing
'''

# defines main function
def main():
    option = -1
    password = ""
    new_pass = 0
    decoded_pass = 0

    while option != 3:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print()
        option = int(input("Please enter an option: "))

        if option == 1:
            password = input("Please enter you password to encode: ")
            new_pass = encode(int(password))
            print("Your password has been encoded and stored!")
        elif option == 2:
            decoded_pass = decode(new_pass)
            print(f'The encoded password is {new_pass}, and the original password is {password}.')
        elif option == 3:
            break

# defines encode function
# accepts a number and returns an encoded password
def encode(passw):
    return passw + 33333333

# defines decode function
# accepts a number and returns a decoded password
def decode(pass_new):
    decoded_val = pass_new - 33333333
    return decoded_val

main()
