# Name: q08_top2_scores.py
# Author: Song Kai
# Description: Enter scores of students and display the highest two
# Created: 20130201
# Last Modified: 20130201

def check(str):
    if str.isdigit():
        return True
    else:
        print("Please enter a proper number!")
        return False

n=input("Enter the total number of scores: ")
while (not check(n)):
    n=input("Enter the total number of scores: ")
n=int(n)

max1=-100
max2=-100

for i in range(0,n):
    score=input("Enter score no."+ str(i+1)+": ")
    while (not check(score)):
        score=input("Enter score no."+ str(i+1)+": ")
    score=int(score)
    if (score>max1):
        max2=max1
        max1=score
    else:
        if (score>max2):
            max2=score
print("the highest score is",max1)
print("the second highest score is",max2)
