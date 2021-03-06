# Name: q03_find_gcd.py
# Author: Song Kai
# Description: Find greatest common divisor between two positive integers
# Created: 20130215
# Last Modified: 20130215

def gcd(x,y):
    # make the larger one in front
    if x<y:
        x+=y
        y=x-y
        x-=y
    r=x%y
    # actual finding gcd process
    while r!=0:
        x=y
        y=r
        r=x%y
    return y

# main

print(gcd(24,16))
print(gcd(255,25))
