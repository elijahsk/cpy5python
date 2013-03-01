# Name: q01_sum_series1.py
# Author: Song Kai
# Description: Compute the series using recursion
# Created: 20130215
# Last Modified: 20130215

# check whether the string can be converted into a number
def check(str):
   if str.isdigit():
     return True
   else:
     print("Please enter a proper number!")
     return False

# calculate the sum using recursion
def sum_series1(n):
    if n==1:return 1
    return sum_series1(n-1)+float(1)/float(n)

# input a number
n=input("Enter a number: ")
while not check(n):
    n=input("Enter a number: ")

# print
print("m[%s] is: "%n,sum_series1(float(n)))
