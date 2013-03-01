# Name: q04_print_reverse.py
# Author: Song Kai
# Description: Reverse the digits of an integer using recursion
# Created: 20130215
# Last Modified: 20130215

# check whether the string can be converted into a number
def check(str):
   if str.isdigit():
     return True
   else:
     print("Please enter a proper number!")
     return False

# reverse the digits using recursion and print
def reverse_int(n):
    if n<10:
        print(n)
    else:
        print(n%10,end="")
        reverse_int(n//10)
    return 0

# input
n=input("Enter a number: ")
while not check(n):
    n=input("Enter a number: ")

# recursion
reverse_int(int(n))
