# Name: q07_display_matrix.py
# Author: Song Kai
# Description: Display a n*n matrix with 1 and 0 generated randomly
# Created: 20130215
# Last Modified: 20130215

import random

def check(str):
   if str.isdigit():
     return True
   else:
     print("Please enter a proper number!")
     return False

def print_matrix(n):
    for i in range(0,n):
        print(random.randint(0,1),end="")
        for j in range(1,n):
            print(" ",random.randint(0,1),end="")
        print()

n=input("Enter the dimension of the matrix: ")
while not check(n):
    n=input("Enter the dimension of the matrix: ")
print("Below is the matrix generated:")
print_matrix(int(n))
