# Name: q09_find_smallest.py
# Author: Song Kai
# Description: Find the smallest integer such that its square is greater than 12000
# Created: 20130201
# Last Modified: 20130201

# set default value of the number
n=1
# check whether the number fulfills the requirement using a loop
while (pow(n,2)<=12000):
    n+=1
# print out the result
print("The smallest number is:",n)
