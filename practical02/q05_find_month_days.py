# Name: q05_find_month_days.py
# Author: Song Kai
# Description: Enter the month and year,display the number of days in that month
# Created: 20130201
# Last Modified: 20130201

months=["January","February","March","April","May","June","July","August","September","October","November","December"]

def check(str):
    if str.isdigit():
        return True
    else:
        print("Please enter a proper number!")
        return False


year=input("Enter year: ")
while (not check(year)):
    year=input("Enter year: ")
year=int(year)

while True:
    month=input("Enter month: ")
    indica=True
    if (month.isdigit()):
        if (int(month)<1 or int(month)>12):
            print("Month value must be between 1 and 12!!!")
            indica=False
    if (check(month) and indica): break
    
month=int(month)
if (month==1 or month==3 or  month==5 or month==7 or month==8 or month==10 or month==12):days=31
if (month==4 or month==6 or month==9 or month==11):days=30
if (month==2):
	if ((year%400==0) or (year%4==0 and (not year%100==0))):days=29
	else:days=28

print(months[month-1],year,"has",days,"days")

    
