# Name: q02_display_pattern.py
# Author: Song Kai
# Description: Display a triangular pattern
# Created: 20130215
# Last Modified: 20130221

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
  return int(n)

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
    
def work(n):
  dig=n+calcdig(n)
  forma="{0:>%ds}"%dig
  string=""
  for i in range(1,n+1):
    string=" "+str(i)+string;
    print(forma.format(string))
  
num=init()
work(num)
