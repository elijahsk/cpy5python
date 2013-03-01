# Name: q06_sum_digits.py
# Author: Song Kai
# Description: Compute the sum of the digits of an integer
# Created: 20130215
# Last Modified: 20130215

# check whether the string can be converted into a number
def check(str):
   if str.isdigit():
     return True
   else:
     print("Please enter a proper number!")
     return False

# add up the sum of the digits using recursion
def sum_digits(n):
    if n<10:return n
    return n%10+sum_digits(n//10)

# input the value of n
n=input("Enter a number: ")
while not check(n):
    n=input("Enter a number: ")

# print
print("Sum of the digits of %s is: "%n,sum_digits(int(n)))
