# Name: q03_determine_grade.py
# Author: Song Kai
# Description: Enter a score and determine the grade
# Created: 20130129
# Last Modified: 20130201

score=input("Enter a score: ")
while (not score.isdigit()):
    print("Please enter a proper number!!")
    score=input("Enter a score: ")
score=int(score)
if (score<0 or score>100):
    print("Invalid! Score must be between 0 - 100.")
elif (score<35):print("U")
elif (score<44):print("S")
elif (score<49):print("E")
elif (score<54):print("D")
elif (score<59):print("C")
elif (score<69):print("B")
else:print("A")

    
