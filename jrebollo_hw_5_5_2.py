"""
Justin Rebollo
    Class: CS 521 - Summer 2
    Date: 7/29/20
    Homework Problem 5_5_2
    Description of Problem (just a 1-2 line summary!):Write a python program
    that does the following:takes as input from the user a date and time
    (24-hour clock) as "MM/DD/YYYY HH:mm:SS"If the input string is returned
    from the function as valid, use input string to print following:
    DD/MM/YYYY HR:MIN:SEC MM/YYYY Whether the time is “AM” or “PM”

"""


def is_validate_datetime(time):
    """Takes a string argumentvalidates that the string
    has all the elements to be a valid date and time"""

    date_time = []
    date_time = str(time)

    # check if the inputted value is valid
    if len(date_time) != 19:
        print("Error: Not in the correct format!")
        return False
    elif date_time.isupper() or date_time.islower():
        print("Error: Not a valid date and time, no alphabetical input!")
        return False
    else:
        new_list = date_time.split(' ')

    # create date
    date_list = new_list[:1]
    # create time
    time_list = new_list[1:]
    # create date and time string
    date_str = str(date_list)
    time_str = str(time_list)

    # checks if correct format for date and time
    if ":" in date_str:
        print("Error: You must use a slash in date")
        return False
    if "/" in time_str:
        print("Error: You must use a colon in time")
        return False

    # uses splices of time_str to check if the supplied time is proper
    if time_str[2:4] > '24':
        print("Invalid: Only 24 hours in a day")
        return False
    if time_str[5:7] > '59':
        print("Invalid: Minutes must be under 60")
        return False
    if time_str[8:10] > '59':
        print("Invalid: Seconds must be under 60")
        return False

    # uses splices of date_str to check if the supplied date is proper
    if date_str[2:4] > '12':
        print("Invalid: Month must be under 12")
        return False
    if date_str[5:7] > '31':
        print("Invalid: There must be between 28 and 31 days in a month!")
        return False
    if date_str[5:7] < '01':
        print("Invalid: There must be between 1 and 31 days in a month!")
        return False
    if date_str[8:12] < '1000':
        print("Invalid: The year must be after 999!")
        return False
    if date_str[8:12] > '9999':
        print("Invalid: The year must be less than 10,000!")

    # if user's time is proper return true to trigger print in requested format
    else:
        return True


if __name__ == '__main__':

    # take in date/time and push to function
    try:
        supplied_time = input(str("Please enter a date and time in this "
                                  "format (with a space after the date): "
                                  "MM/DD/YYYY HH:mm:SS "))
        print(is_validate_datetime(supplied_time))
    except UnboundLocalError:
        print("You did not enter a valid time!")

    # if function returns true print out the date/time in requested format
    try:
        if (is_validate_datetime(supplied_time)):
            date_times = []
            date_times = str(supplied_time)
            new_list = date_times.split(' ')
            date_list = new_list[:1]
            # create time
            time_list = new_list[1:]
            date_str = str(date_list)
            time_str = str(time_list)

            # print as requested
            print("DD/MM/YYYY is ", date_str[5:7], "/", date_str[2:4], "/",
                  date_str[8:12])
            print("HR:MIN:SEC is ", time_str[2:4], ":", time_str[5:7], ":",
                  time_str[8:10])
            print("MM/YYYY is ", date_str[2:4], "/",  date_str[8:12])

            # checks and prints AM or PM, account for 24 hour clock
            if time_str[2:4] < '12':
                print("The time is AM")
            elif time_str[2:4] == '24':
                print("The time is AM")
            else:
                print("The time is PM")
    # catch error
    except ValueError:
        print("Something went wrong. Please try again!")
