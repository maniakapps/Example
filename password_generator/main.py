# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from PasswordGenerator import PasswordGenerator


def generate_password():
    while True:
        mn = int(input("How many passwords would you like to generate: "))
        for _ in range(mn):
            print(PasswordGenerator("/Users/mapc/PycharmProjects/Book/password_generator/adjectives.txt", "/Users/mapc/PycharmProjects/Book/password_generator/nouns.txt","/Users/mapc/PycharmProjects/Book/password_generator/punctuation.txt"))
        mn = input("would you like to continue")
        if mn.lower().strip() == "no":
            print("Thanks for using our password generator")
            break


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    generate_password()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
