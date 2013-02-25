# Name: q06_determine_prime.py
# Author: Song Kai
# Description: Display the 1st 1000 prime numbers 10 per row
# Created: 20130215
# Last Modified: 20130215

import math

# check whether the number is prime
def is_prime(num):
    for i in range(2,round(math.sqrt(num))+1):
      if num%i==0:
          return False
    return True

# initialize the values 
num=2;n=0;
# loop for 1000 prime numbers
while n<1000:
    if is_prime(num):
        n+=1
        # print with format
        print("{0:<6d}".format(num),end="")
        # turn to a new line after printing every 10 numbers
        if n%10==0: print()
    num+=1

        
    
        
