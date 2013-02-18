# Name: q07_find_largest.py
# Author: Song Kai
# Description: Find the largest integer in an array
# Created: 20130215
# Last Modified: 20130215

def check(str):
   if str.isdigit():
     return True
   else:
     print("Please enter a proper number!")
     return False

def find_largest(a):
    if len(a)==2: return max(a[0],a[1])
    return max(a[0],find_largest(a[1:]))

n=input("Enter the number of integers in the array: ")
while not check(n):
    n=input("Enter the number of integers in the array: ")
n=int(n)

alist=[]

for i in range(1,n+1):
    num=input("Enter number %d: "%i)
    while not check(num):
        num=input("Enter number %d: "%i)
    alist.append(num)
print("The largest number in alist is: ",find_largest(alist))
