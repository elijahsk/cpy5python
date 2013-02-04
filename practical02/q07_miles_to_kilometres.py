# Name: q07_miles_to_kilometres.py
# Author: Song Kai
# Description: Enter miles to kilometres table
# Created: 20130201
# Last Modified: 20130201

print("Miles Kilometres Kilometres Miles")
for i in range(1,11):
    print("{0:<5}".format(i),"{0:<10.3f}".format(i*1.609),"{0:<10}".format(i*5+15),"{0:<6.3f}".format((i*5+15)/1.609))

