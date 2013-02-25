# Name: q02_display_pattern.py
# Author: Song Kai
# Description: Display a triangular pattern
# Created: 20130215
# Last Modified: 20130221

# check whether the input is a number
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
  return int(n)

# calculate length of each line by measuring the length of the numbers
def calcdig(n):
    k=9
    dig=0
    ans=0
    while n>k:
        dig=dig+1
        ans+=dig*k
        n-=k
        k*=10
    return ans+n*(dig+1)
# actual printing    
def work(n):
  # the overall length of a line after adding in all the spaces
  dig=n+calcdig(n)
  # set up the format
  forma="{0:>%ds}"%dig
  string=""
  # printing
  for i in range(1,n+1):
    string=" "+str(i)+string;
    print(forma.format(string))

# main program
num=init()
work(num)
