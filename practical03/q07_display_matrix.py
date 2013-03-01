# Name: q07_display_matrix.py
# Author: Song Kai
# Description: Display a n*n matrix with 1 and 0 generated randomly
# Created: 20130215
# Last Modified: 20130215

import random

# check whether the string can be converted into a number
def check(str):
   if str.isdigit():
     return True
   else:
     print("Please enter a proper number!")
     return False

# actual random printing process
def print_matrix(n):
   # n rows
    for i in range(0,n):
        print(random.randint(0,1),end="")
        # n columns
        for j in range(1,n):
            print(" ",random.randint(0,1),end="")
        print()

# input the dimension
n=input("Enter the dimension of the matrix: ")
# check until n is really a number
while not check(n):
    n=input("Enter the dimension of the matrix: ")
# print
print("Below is the matrix generated:")
print_matrix(int(n))
