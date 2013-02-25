# Name: q10_find_largest.py
# Author: Song Kai
# Description: Find the largest integer such that its cube is less than 12000
# Created: 20130201
# Last Modified: 20130201

# set default value of the number
n=1
# check whether the number fulfills the requirement using a loop
while (pow(n,3)<12000):n+=1
# print out the result
print("the largest integer is:",n-1)
