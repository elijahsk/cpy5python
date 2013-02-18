# Name: q03_find_gcd.py
# Author: Song Kai
# Description: Find greatest common divisor using recursion
# Created: 20130215
# Last Modified: 20130215

def gcd(x,y):
    if x<y:
        x+=y
        y=x-y
        x-=y
    if x%y==0:return y
    return gcd(y,x%y)

    
print(gcd(24,16))
print(gcd(255,25))

