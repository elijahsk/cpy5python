# Name: q01_sum_series1.py
# Author: Song Kai
# Description: Compute the series using recursion
# Created: 20130215
# Last Modified: 20130215

def check(str):
   if str.isdigit():
     return True
   else:
     print("Please enter a proper number!")
     return False

def sum_series1(n):
    if n==1:return 1
    return sum_series1(n-1)+float(1)/float(n)

n=input("Enter a number: ")
while not check(n):
    n=input("Enter a number: ")
    
print("m[%s] is: "%n,sum_series1(float(n)))
