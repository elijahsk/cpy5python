# Name: q4_sum_digits.py
# Author: Song Kai
# Description: Read an integer and add all the digits in the integer
# Created: 20130121

num=int(input("Enter an interger between 0 and 1000: "))
sum=0
while (num>0):
    sum+=num%10
    num//=10
print("The sum of all the digits is: ",sum)
