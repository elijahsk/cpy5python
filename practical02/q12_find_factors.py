# Name: q12_find_factors.py
# Author: Song Kai
# Description: Find the greatest common divisor of two intergers
# Created: 20130201
# Last Modified: 20130201

# check and prompt if input is not a number string
def check(str):
    if str.isdigit():
        return True
    else:
        print("Please enter a proper number!")
        return False

# set default state of prime list to empty
prime=[]
# input the number to be factorised
num=input("Enter a number to be factorised: ")
# check and prompt until the number is really a number
while (not check(num)):
    num=input("Enter a number to be factorised: ")
num=int(num)

# find and append all the prime numbers smaller than the number into prime list
for i in range (2,num):
    indica=True
    for j in range(2,round(i**0.5)):
        if (i%j==0):
            indica=False
            break
    if (indica):
        prime.append(i)
# indica used to check whether the factor found is the first one
# (associated with the foramt of printing)
indica=True
# set default value of ansstr which is used to store the answer
ansstr=""

# using a loop check whether the number is divisible by the prime number
for i in range (0,len(prime)):
    while (num%prime[i]==0):
        num/=prime[i]
        # append the number into the answer string
        if (indica):
            ansstr+=str(prime[i])
            indica=False
        else:
            ansstr=ansstr+", "+str(prime[i])
# the situation in which num itself is a prime number
if (num!=1): ansstr+=str(num)

# print out the result
print(ansstr+".")
