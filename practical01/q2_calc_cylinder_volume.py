# Name: q2_calc_cylinder_volume.py
# Author: Song Kai
# Description: Read in radius and length compute the volume of a cylinder
# Created: 20130121

import math
r = float(input("Enter the radius of the cylinder: "))
l = float(input("Enter the length of the cylinder: "))
print( "The volume of the cylinder is :","{0:8.3f}".format(r**2*l*math.pi))
