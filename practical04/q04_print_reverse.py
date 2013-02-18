# Name: q04_print_reverse.py
# Author: Song Kai
# Description: Reverse the digits of an integer using recursion
# Created: 20130215
# Last Modified: 20130215

def check(str):
   if str.isdigit():
     return True
   else:
     print("Please enter a proper number!")
     return False

def reverse_int(n):
    if n<10:
        print(n)
    else:
        print(n%10,end="")
        reverse_int(n//10)
    return 0

n=input("Enter a number: ")
while not check(n):
    n=input("Enter a number: ")
    
reverse_int(int(n))
