# Name: q09_find_smallest.py
# Author: Song Kai
# Description: Find the smallest integer such that its square is greater than 12000
# Created: 20130201
# Last Modified: 20130201

n=1
while (pow(n,2)<=12000):
    n+=1
print("The smallest number is:",n)
