# Name: q11_find_gcd.py
# Author: Song Kai
# Description: Find the greatest common divisor of two intergers
# Created: 20130201
# Last Modified: 20130201

def check(str):
    if str.isdigit():
        return True
    else:
        print("Please enter a proper number!")
        return False

n1=input("Enter the first number: ")
while (not check(n1)):
    n1=input("Enter the first number: ")
    
n2=input("Enter the second number: ")
while (not check(n2)):
    n2=input("Enter the second number: ")
    
n1=int(n1)
n2=int(n2)

n11=n1
n21=n2

if (n1>n2):
    n1=n1+n2
    n2=n1-n2
    n1=n1-n2

r=n1%n2

while (r!=0):
    n1=n2
    n2=r
    r=n1%n2

print("the greatest common divisor of",n11,"and",n21,"is",n2)
