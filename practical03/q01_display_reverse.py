# Name: q01_display_reverse.py
# Author: Song Kai
# Description: Display an integer in reverse order
# Created: 20130215
# Last Modified: 20130215

def check(str):
  if str.isdigit():
    return True
  else:
    print("Please enter a proper number!")
    return False

def init():
  n=input("Enter a number: ")
  while (not check(n)):
    n=input("Enter a number: ")
  return n

def work():
  return n[::-1]

def outit():
  print(n)  
  

num=init()
num=work()
outit()
