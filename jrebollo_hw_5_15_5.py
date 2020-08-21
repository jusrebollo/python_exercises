"""
Justin Rebollo
    Class: CS 521 - Summer 2
    Date: 7/29/20
    Homework Problem 5_15_5
    Description of Problem (just a 1-2 line summary!): Calculate compound
    interest from user input of principal, int_rate and years. Also do so
    recursively.
 
"""


def calc_compound_interest(principal, int_rate, years):
    """This function takes three variables principal, int_rate, and years and
    returns a total based on the compound interest formula"""

    total = principal * (pow((1 + int_rate), years))

    return total


def calc_compound_interest_recursive(principal, int_rate, years):
    """ This function takes three variables principal, int_rate, and years and
     returns a calculated total  recursively"""

    if years == 0:
        return principal
        print(years)
    else:
        return calc_compound_interest_recursive(principal * (1 + int_rate),
                                                int_rate, years - 1)


if __name__ == '__main__':

    # while loop until correct input
    i = 1
    while i == 1:
        # try to take input
        try:
            print(
                "When prompted below, enter your principal, interest rate, "
                "and time length in years:")
            principal = int(input("What is the principal? "))
            int_rate = float(
                input("What is the interest rate? (as a decimal, no %) "))
            years = int(input("How many years? "))
            i = 0
        # catch errors
        except ValueError:
            print(
                "Value Error: Please enter an integer for principal and "
                "years, and a float interest rate!")
            i = 1
        except NameError:
            print(
                "Name Error: Please enter an integer for principal and years, "
                "and a float interest rate!")
            i = 1
        # try to print values
        try:
            print('-' * 10)
            print("Total Value from formula: ",
                  ("{:0,.2f}".format(calc_compound_interest
                                     (principal, int_rate, years))))
            print("Total Value calculated recursively: ")
            print(("{:0,.2f}".format(calc_compound_interest_recursive
                                     (principal, int_rate, years))))

            recursive_round = round(calc_compound_interest_recursive
                                    (principal, int_rate, years), 4)
            normal_round = round(
                calc_compound_interest(principal, int_rate, years), 4)
            print('-' * 10)
            # check if equal to four decimal places
            if recursive_round == normal_round:
                print("Values are equal to four decimal places!")
            else:
                print("Values are not equal to four decimal places!")
        # catch errors
        except ValueError:
            print(
                "Value Error: Please enter an integer for principal and years, "
                "and a float interest rate!")
            i = 1
        except NameError:
            print(
                "Name Error: Please enter an integer for principal and years, "
                "and a float interest rate!")
            i = 1
