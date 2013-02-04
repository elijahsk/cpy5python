# Name: q12_find_factors.py
# Author: Song Kai
# Description: Find the greatest common divisor of two intergers
# Created: 20130201
# Last Modified: 20130201

def check(str):
    if str.isdigit():
        return True
    else:
        print("Please enter a proper number!")
        return False

prime=[]
num=input("Enter a number to be factorised: ")
while (not check(num)):
    num=input("Enter a number to be factorised: ")
num=int(num)

for i in range (2,num):
    indica=True
    for j in range(2,round(i**0.5)):
        if (i%j==0):
            indica=False
            break
    if (indica):
        prime.append(i)
indica=True
ansstr=""
for i in range (0,len(prime)):
    while (num%prime[i]==0):
        num/=prime[i]
        if (indica):
            ansstr+=str(prime[i])
            indica=False
        else:
            ansstr=ansstr+", "+str(prime[i])
if (num!=1): ansstr+=str(num)
print(ansstr+".")
