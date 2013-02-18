# Name: q06_determine_prime.py
# Author: Song Kai
# Description: Display the 1st 1000 prime numbers 10 per row
# Created: 20130215
# Last Modified: 20130215

import math

def is_prime(num):
    for i in range(2,round(math.sqrt(num))+1):
      if num%i==0:
          return False
    return True

num=2;n=0;
while n<1000:
    if is_prime(num):
        n+=1
        print("{0:<6d}".format(num),end="")
        if n%10==0: print()
    num+=1

        
    
        
