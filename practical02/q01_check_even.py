# Name: q01_check_even.py
# Author: Song Kai
# Description: Check whether a number is even
# Created: 20130129
# Last Modified: 20130201

num=input("Enter a number: ")
while (not num.isdigit()):
	print("Please enter a proper number!!")
	num=input("Enter a number: ")
num=int(num)
	
if (num%2==0):
    print(num,"is even.")
else:
    print(num,"is odd.")

          
