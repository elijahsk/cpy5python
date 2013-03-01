# Name: q08_convert_milliseconds.py
# Author: Song Kai
# Description: Convert milliseconds to hours,minutes and seconds
# Created: 20130215
# Last Modified: 20130215

# check whether the string can be converted into a number
def check(str):
   if str.isdigit():
     return True
   else:
     print("Please enter a proper number!")
     return False
# the convert process
def convert_ms(n):
    string=""
    # calculate the number of hours
    string+=str(n//3600000)
    n%=3600000
    # calculate the number of minutes
    string+=":"+str(n//60000)
    n%=60000
    # calculate the number of seconds
    string+=":"+str(n//1000)
    return string

# input the time
n=input("Enter the time in milliseconds: ")
while not check(n):
    n=input("Enter the time in milliseconds: ")

# print
print(convert_ms(int(n)))
