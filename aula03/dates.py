

def isLeapYear(year):
    return year%400 == 0 or year%4==0 and year%100!=0


def monthDays(year, month):
    MONTHDAYS = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
        # This tuple contains the days in each month (on a common year).
        # For example: MONTHDAYS[3] is the number of days in March.
    days = MONTHDAYS[month]
    if month==2:
        if isLeapYear(year)==True:
            days=29
    return days



def nextDay(year, month, day):
    if isLeapYear(year)==True and month==2 and day==29:
        month+=1
        day=1
    elif isLeapYear(year)==False and month==2 and day==28:
        month+=1
        day=1
    elif (month==1 or month==3 or month==5 or month==5 or month==7 or month==8 or month==10) and day==31:
        month+=1
        day=1
    elif (month==4 or month==6 or month==9 or month==11) and day==30:
        month+=1
        day=1
    elif month==12 and day==31:
        year+=1
        month=1
        day=1
    else:
        day+=1
    
    return year, month, day


# This is the main function
def main():
    print("Was", 2017, "a leap year?", isLeapYear(2017))    # False?
    print("Was", 2016, "a leap year?", isLeapYear(2016))    # True?
    print("Was", 2000, "a leap year?", isLeapYear(2000))    # True?
    print("Was", 1900, "a leap year?", isLeapYear(1900))    # False?
    
    print("January 2017 had", monthDays(2017, 1), "days")   # 31?
    print("February 2017 had", monthDays(2017, 2), "days")  # 28?
    print("February 2016 had", monthDays(2016, 2), "days")  # 29?
    print("February 2000 had", monthDays(2000, 2), "days")  # 29?
    print("February 1900 had", monthDays(1900, 2), "days")  # 28?
    
    y, m, d = nextDay(2017, 1, 30)
    print(y, m, d)    # 2017 1 31 ?
    y, m, d = nextDay(2017, 1, 31)
    print(y, m, d)    # 2017 2 1 ?
    y, m, d = nextDay(2017, 2, 28)
    print(y, m, d)    # 2017 3 1 ?
    y, m, d = nextDay(2017, 2, 28)
    print(y, m, d)    # 2016 3 1 ?
    y, m, d = nextDay(2017, 12, 31)
    print(y, m, d)    # 2018 1 1 ?

# call the main function
if __name__ == "__main__":
    main()

