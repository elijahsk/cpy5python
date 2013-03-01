# Name: q02_sum_series2.py
# Author: Song Kai
# Description: Compute the series using recursion
# Created: 20130215
# Last Modified: 20130215

# check whether the string  an be converted into a number
def check(str):
   if str.isdigit():
     return True
   else:
     print("Please enter a proper number!")
     return False

# calculate the sum using recursion
def sum_series2(n):
    if n==1:return float(1)/float(3)
    return sum_series2(n-1)+float(n)/float(2*n+1)

# input
n=input("Enter a number: ")
while not check(n):
    n=input("Enter a number: ")

# print
print("m[%s] is: "%n,sum_series2(float(n)))
