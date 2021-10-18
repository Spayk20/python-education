"""
Calculator
You chose one of 4 operations( + _ * / ), input 2 numbers and receive answer
"""
import decimal
import time
import typing


class Calculator:
    """Class calculate sum +, subtract -, multiply *, divide /"""
    def __init__(self, a: str, b: str) -> None:
        """Class constructor"""
        self.num_1 = a
        self.num_2 = b

    def add(self) -> typing.Union[int, decimal.Decimal]:
        """Calculate sum of 2 numbers"""
        return self.num_1 + self.num_2

    def subtract(self) -> typing.Union[int, decimal.Decimal]:
        """Calculate sub of 2 numbers"""
        return self.num_1 - self.num_2

    def multiply(self) -> typing.Union[int, decimal.Decimal]:
        """Calculate mul of 2 numbers"""
        return self.num_1 * self.num_2

    def divide(self) -> typing.Union[int, decimal.Decimal, None]:
        """Calculate div of 2 numbers"""
        try:
            return self.num_1 / self.num_2
        except decimal.DivisionByZero:
            print("Your answer is undefined")
        return None


def str_to_float_int(string: str) -> typing.Union[int, decimal.Decimal, None]:
    """Func convert string to decimal or int"""
    # try to convert str to decimal
    try:
        return decimal.Decimal(string)
    except decimal.InvalidOperation:
        # if no try to convert to int
        try:
            return int(string)
        # except return None
        except ValueError:
            pass
    return None


if __name__ == "__main__":
    while True:
        # just display menu and ask user input method
        print("      MENU\n 1: Add\t 2: Sub\n 3: Mul\t 4: Dev\n 0: Exit")
        # catch exception if user input not number and exit
        try:
            menu_choice = int(input("Select operation: "))
        except ValueError:
            print("Only numbers aloud. Bye")
            break

        # first check whether user want to exit
        if menu_choice == 0:
            break

        # take 2 numbers
        user_input1 = input("Enter first number: ")
        user_input2 = input("Enter second number: ")

        # check is input numbers are int, decimal or no
        user_input1 = str_to_float_int(user_input1)
        user_input2 = str_to_float_int(user_input2)

        # if user input not numbers - exit
        if (user_input1 or user_input2) is None:
            print("Only digits and dot aloud. Bye")
            break

        # create a calculator object
        obj = Calculator(user_input1, user_input2)

        if menu_choice == 1:
            print("Result ", obj.add())
        elif menu_choice == 2:
            print("Result ", obj.subtract())
        elif menu_choice == 3:
            print("Result ", obj.multiply())
        elif menu_choice == 4:
            print("Result ", obj.divide())
        else:
            print("Invalid Operation")
        time.sleep(2)
