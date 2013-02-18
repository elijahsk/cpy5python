# Name: q06_sum_digits.py
# Author: Song Kai
# Description: Compute the sum of the digits of an integer
# Created: 20130215
# Last Modified: 20130215

def check(str):
   if str.isdigit():
     return True
   else:
     print("Please enter a proper number!")
     return False

def sum_digits(n):
    if n<10:return n
    return n%10+sum_digits(n//10)

n=input("Enter a number: ")
while not check(n):
    n=input("Enter a number: ")
    
print("Sum of the digits of %s is: "%n,sum_digits(int(n)))
