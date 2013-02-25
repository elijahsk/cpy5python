# Name: q02_triangle.py
# Author: Song Kai
# Description: Validating triangles and computing perimeter
# Created: 20130129
# Last Modified: 20130201

# input length of first side
s1=input("Enter side 1: ")
# check and prompt until input is really a number
while (not s1.isdigit()):
	print("Please enter a proper number!!")
	s1=input("Enter side 1: ")
s1=int(s1)
# input length of second side
s2=input("Enter side 2: ")
# check and prompt until input is really a number
while (not s2.isdigit()):
	print("Please enter a proper number!!")
	s2=input("Enter side 2: ")
s2=int(s2)
# input length of third side
s3=input("Enter side 3: ")
# check and prompt until input is really a number
while (not s3.isdigit()):
	print("Please enter a proper number!!")
	s3=input("Enter side 3: ")
s3=int(s3)

# arrange the sequence of length in an ascending order
if (s1>s2):
       t=s1
       s1=s2
       s2=t
if (s2>s3):
       t=s2
       s2=s3
       s3=t
if (s1>s2):
       t=s1
       s1=s2
       s2=t

# check whether they can form a triangle
if (s3<s2+s1 and s1>s3-s2):
    print("Perimeter: ",s1+s2+s3)
else:
    print("Invalid triangle!")
       
