# Name: q05_count_letter.py
# Author: Song Kai
# Description: Find the number of occurences of a specified letter
# Created: 20130215
# Last Modified: 20130215

def count_letter(string,char):
    if len(string)==1: return (string[0]==char)
    return (string[0]==char)+count_letter(string[1:],char)

string=input("Enter a string: ")
char=input("Enter a specific char you want to serach: ")

print(count_letter(string,char))
