# Name: q08_find_uppercase.py
# Author: Song Kai
# Description: Find the number of uppercase letters in a string
# Created: 20130215
# Last Modified: 20130215

def find_num_uppercase(n):
    if len(n)==1:return n[0].isupper()
    return n[0].isupper()+find_num_uppercase(n[1:])

n=input("Enter a string: ")
    
print("The number of uppercase letter is: ",find_num_uppercase(n))
