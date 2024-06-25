from flag_class import *

if __name__ == "__main__":
    """
    a program that prints the Israeli flag to the console using asterisks ("*") to represent each
    pixel. The program should take the width and height and the kind option of the flag as input and output the flag with
    appropriate proportions.
    """
    while True:
        try:
            width = int(input("Enter the width of the flag: "))
            height = int(input("Enter the height of the flag: "))
            option = (input("Enter letter O for star of david flag or Z for david TZION star of david flag: "))
            if isinstance(option, str) and option.isalpha():
                flag_obj = Flag(width, height, option)
                print(flag_obj)
        except BaseException as b:
            print(b) 