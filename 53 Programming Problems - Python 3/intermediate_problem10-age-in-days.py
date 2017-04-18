# Age in Days

# Write a program that's capable of giving the age of a person in days, based
# on the the day of birth informed.
# In order to solve this problem you need to know that:
# - September, November, April and June have exact 30 days, all the rest have 31
# days, except February that has 28, except in bissext years, when it has 29
# days.
# - Every even year, divisible by 4 is a bissext year (1992 = 4*468, therefore
# 1992 is a bissext year. 1990 isn't)
# - The rule above is not valid for the last year of a Century, it must be also
# divisible by 400 to be a bissext year, thus 1700, 1900 and 2100 are not
# bissexts, but 2000 is.
#
# ** You aren't allowed to use a function that returns the number of days!!! **
#
# The program input is a valid integer per line, being day, month and year of
# birth, respectively.
# The output will be a single line with the number of days that the person has
# lived.
from datetime import datetime
import math

# Get birth date from user input
day_of_birth = 0
while day_of_birth < 1 or day_of_birth > 31:
    day_of_birth = input("Day: ")
month_of_birth = 0
while month_of_birth < 1 or month_of_birth > 12:
    month_of_birth = input("Month: ")
year_of_birth = 0
while year_of_birth < 1:
    year_of_birth = input("Year: ")

# Get current date
current_day = datetime.now().date().day
current_month = datetime.now().date().month
current_year = datetime.now().date().year

# Initialize variable that'll store the total days lived
total_days = 0

# Calculate difference between years
if current_year - year_of_birth > 1:
    total_days += (current_year - year_of_birth - 1) * 365
    if year_of_birth % 4 == 0:
        if year_of_birth % 100 == 0:
            if year_of_birth % 400 == 0:
                if current_year - year_of_birth % 5 == 0:
                    total_days += math.ceil((current_year - year_of_birth) / 4)
                else:
                    total_days += math.floor((current_year - year_of_birth) / 4)
        else:
            if current_year - year_of_birth % 5 == 0:
                total_days += math.ceil((current_year - year_of_birth) / 4)
            else:
                total_days += math.floor((current_year - year_of_birth) / 4)
month_31_days = [1, 3, 5, 7, 8, 10, 12]
# Calculate difference between months
if current_month - month_of_birth < 0:
    total_days += (((current_month - month_of_birth) % 12) - 1) * 30
    if current_month > 2:  # remove 2 days from Feb
        total_days -= 2
    # Adding days from 31-days months
    _31_day_months_last_year = month_31_days.index(
        min(month_31_days, key=lambda x: abs(x-month_of_birth)))
    _31_day_months_current_year = month_31_days.index(
        min(month_31_days, key=lambda x: abs(x-current_month)))
    total_days += ((6 - _31_day_months_current_year) +
                   (6 - _31_day_months_last_year))
elif current_month - month_of_birth > 0:
    if current_year > year_of_birth:
        total_days += 363  # 365 days of a year - 2 days removed from Feb
    total_days += (current_month - month_of_birth - 1) * 30
    if month_of_birth == 1:
        total_days -= 2
    # Adding days from 31-days months
    _31_day_months_last_year = month_31_days.index(
        min(month_31_days, key=lambda x: abs(x-month_of_birth)))
    _31_day_months_current_year = month_31_days.index(
        min(month_31_days, key=lambda x: abs(x-current_month)))
    total_days += (_31_day_months_current_year - _31_day_months_last_year)

# Calculate difference between days
if current_month - month_of_birth != 0:
    total_days += 30 - day_of_birth
    total_days += current_day
else:
    total_days += current_day - day_of_birth

if total_days > 1:
    print "%d days" % total_days
else:
    print "%d day" % total_days
