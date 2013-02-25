# Name: q01_display_reverse.py
# Author: Song Kai
# Description: Display an integer in reverse order
# Created: 20130215
# Last Modified: 20130221

# check whether input is a number
def check(str):
  if str.isdigit():
    return True
  else:
    print("Please enter a proper number!")
    return False

# input
def init():
  n=input("Enter a number: ")
  while (not check(n)):
    n=input("Enter a number: ")
  return n

# reverse process
def work():
  return num[::-1]

# output
def outit():
  k=0
  # skip the zero at the beginning (if any)
  while (num[k]=='0'): k+=1
  print(num[k:])  
  
#main program
num=init()
num=work()
outit()
