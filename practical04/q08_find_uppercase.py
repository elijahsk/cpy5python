# Name: q08_find_uppercase.py
# Author: Song Kai
# Description: Find the number of uppercase letters in a string
# Created: 20130215
# Last Modified: 20130215

# find the number of uppercase letters in the string
# value of True as 1 and value of False as 0
def find_num_uppercase(n):
    if len(n)==1:return int(n[0].isupper())
    return int(n[0].isupper())+find_num_uppercase(n[1:])

# input
n=input("Enter a string: ")

# print the result of find_num_uppercase function
print("The number of uppercase letter is: ",find_num_uppercase(n))
