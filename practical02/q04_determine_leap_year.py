# Name: q04_determine_leap_year.py
# Author: Song Kai
# Description: Enter a year and determine whether it is a leap year
# Created: 20130201
# Last Modified: 20130201

# check number function
def check(str):
    if str.isdigit():
        return True
    else:
        print("Please enter a proper number!")
        return False
# input year
year=input("Enter year: ")
# check using function check(str)
while (not check(year)):
    year=input("Enter year: ")
year=int(year)

# check whether the year is a leap year
if (year%400==0 or (year%100!=0 and year%4==0)):
    print("Leap")
else:
    print("Non-Leap")
