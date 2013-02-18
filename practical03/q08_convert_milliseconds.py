# Name: q08_convert_milliseconds.py
# Author: Song Kai
# Description: Convert milliseconds to hours,minutes and seconds
# Created: 20130215
# Last Modified: 20130215

def check(str):
   if str.isdigit():
     return True
   else:
     print("Please enter a proper number!")
     return False

def convert_ms(n):
    string=""
    string+=str(n//3600000)
    n%=3600000
    string+=":"+str(n//60000)
    n%=60000
    string+=":"+str(n//1000)
    return string

n=input("Enter the time in milliseconds: ")
while not check(n):
    n=input("Enter the time in milliseconds: ")
    
print(convert_ms(int(n)))
