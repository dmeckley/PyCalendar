def printMonth(year, month):
    # Display calendar heading including month, year,
    # heading divider, and days of week:
    printMonthTitle(year, month)
    # Display calendar body including dates
    # for the months days of the week:
    printMonthBody(year, month)

def printMonthTitle(year, month):
    # days Dictionary for printing days of the week:
    days = {
        1: 'SUN',
        2: 'MON',
        3: 'TUE',
        4: 'WED',
        5: 'THUR',
        6: 'FRI',
        7: 'SAT'
    }
    # Display month and year heading:
    for iterator in range(14):
        print(' ', end= '')
    print(getMonthName(month), year, sep=' ')
    # Display divider line heading:
    for iterator in range(38):
        print('-', end='')
    print()
    # Display days of week heading:
    iterator = 1
    for iterator in days:
        print(' ', days[iterator], end='')
    print()

def printMonthBody(year, month):
    # Get start day of the week for the first date in the month:
    startDay = getStartDay(year, month)
    # Get the number of days in the month:
    numberOfDaysInMonth = getNumberOfDaysInMonth(year, month)
    # Display spacing prior to days of week dates:
    iterator = 0
    for iterator in range(0, startDay):
        print('    ', end=' ')
    # Display days of week dates on calendar:
    for iterator in range(1, numberOfDaysInMonth + 1):
        print(format(iterator, '4d'), end=' ')
        if (iterator + startDay) % 7 == 0:
            print()

def getMonthName(month):
    # months Dictionary for returning the month:
    months = {
        1: 'January',
        2: 'February',
        3: 'March',
        4: 'April',
        5: 'May',
        6: 'June',
        7:  'July',
        8: 'August',
        9: 'September',
        10: 'October',
        11: 'November',
        12: 'December'
    }
    # Return appropriate month:
    if month == 1:
        return(months[1])
    elif month == 2:
        return(months[2])
    elif month == 3:
        return(months[3])
    elif month == 4:
        return(months[4])
    elif month == 5:
        return(months[5])
    elif month == 6:
        return(months[6])
    elif month == 7:
        return(months[7])
    elif month == 8:
        return(months[8])
    elif month == 9:
        return(months[9])
    elif month == 10:
        return(months[10])
    elif month == 11:
        return(months[11])
    else:
        return(months[12])

def getStartDay(year, month):
    # Get the start date for month/1/year:
    START_DAY_FOR_JAN_1_2018 = 3
    # Get total number of days from 1/1/1800 to month/1/year:
    totalNumberOfDays = getTotalNumberOfDays(year, month)
    # Return the start day for month/1/year:
    return(totalNumberOfDays + START_DAY_FOR_JAN_1_2018) % 7

def getTotalNumberOfDays(year, month):
    # Get the total number of days since January 1st, 1800:
    total = 0
    # Get the total days from 1800 to 1/1/year
    for i in range(1800, year):
        # Assign total to 366 days if leap year:
        if isLeapYear(i):
           total += 366
        # Otherwise, assign total 365 days if not leap year:
        else:
            total += 365
    # Add days from Jan to the month prior to the calendar month:
    for i in range(1, month):
        total += getNumberOfDaysInMonth(year, i)
    # Return total number of days:
    return total

def getNumberOfDaysInMonth(year, month):
    # Get the number of days in a month:

    # If Jan, Mar, May, Jul, Aug, Oct, Dec then return 31 days:
    if (month == 1 or month == 3 or month == 5 or month == 7 or 
    month == 8 or month == 10 or month == 12):
        return(31)
    # If Apr, Jun, Sep, Nov then return 30 days: 
    if month == 4 or month == 6 or month == 9 or month == 11:
        return(30)
    # If Feb, then return 29 if leap year and 28 if not leap year:
    if month == 2:
        return(29 if isLeapYear(year) else 28)
    # Return 0 for any other input besides 1 --> 12:
    return(0)

def isLeapYear(year):
    # Boolean function to determine if year is a leap year:
    return(year % 400 == 0 or (year % 4 == 0 and year % 100 != 0))

def main():
    year = eval(input('Enter the full year (e.g., 2001): '))
    # year = 2010
    month = eval(input('Enter month as a number between 1 and 12: '))
    # month = 3
    printMonth(year, month)
    print()

if __name__ == "__main__":
    main()
