# Name: q08_top2_scores.py
# Author: Song Kai
# Description: Enter scores of students and display the highest two
# Created: 20130201
# Last Modified: 20130207

def check(str):
    if str.isdigit():
        return True
    else:
        print("Please enter a proper number!")
        return False

# input the number of scores
n=input("Enter the total number of scores: ")
# check and prompt until the number is really a number
while (not check(n)):
    n=input("Enter the total number of scores: ")
n=int(n)

# set default value for maximum score and name of the scorers
max1=-100
max2=-100
name1=""
name2=""

for i in range(0,n):
    # input the score and name
    score=input("Enter score no."+ str(i+1)+": ")
    name=input("Enter name no."+ str(i+1)+": ")
    # check and prompt until the score is a number
    while (not check(score)):
        score=input("Enter score no."+ str(i+1)+": ")
    score=int(score)
    # check if the new score is the maximum so far, do replacing accordingly
    if (score>max1):
        max2=max1
        name2=name1
        max1=score
        name1=name
    else:
        # check if the new score is the second maximum so far
        if (score>max2):
            max2=score
            name2=name
# print out the result
print("the highest score is",max1,"from",name1)
print("the second highest score is",max2,"from", name2)
