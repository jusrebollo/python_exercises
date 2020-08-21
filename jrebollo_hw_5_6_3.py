"""
Justin Rebollo
    Class: CS 521 - Summer 2
    Date: 7/29/20
    Homework Problem 5_6_3
    Description of Problem (just a 1-2 line summary!):  Prompts the user for
    three numbers in one request.Divides the first number by the second number
    and add that result to the third number.  Prints output that shows in one line
    the formula applied and the result of the calculation.
"""

if __name__ == '__main__':

    # while loop until input is correct
    i = 1

    while i == 1:
        # try to get input
        try:
            num1, num2, num3 = (input("Enter 3 numbers separated by a space: ")
                                .split())
            num1 = float(num1)
            num2 = float(num2)
            num3 = float(num3)
            i = 0

        # excepts for common errors
        except ValueError:
            print("Value Error: Please enter three numbers!")
            i = 1
        except NameError:
            print("Name Error: Please enter three numbers as integers "
                  "or floats !")
            i = 1
        except TypeError:
            print("Type Error: Do not enter any letters!")
            i = 1

        # try to calculate formula
        try:
            first_operand = (num1 / num2)
            total = first_operand + num3
            print("Formula: ", "(", num1, "/", num2, ")", "+", num3,
                  "=", '{:,.2f}'.format(total))
        # excepts for common errors
        except ValueError:
            print("Value Error: Please enter three numbers!")
            i = 1
        except NameError:
            print("Name Error: Please enter three numbers as integers "
                  "or floats !")
            i = 1
        # catch zero division
        except ZeroDivisionError:
            print("Your second value cannot be a zero! No dividing by zeros.")
            i = 1
        # catch type error
        except TypeError:
            print("Type Error: Do not enter any letters!")
            i = 1
