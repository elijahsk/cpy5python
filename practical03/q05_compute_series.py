# Name: q05_compute_series.py
# Author: Song Kai
# Description: Display the series in a table
# Created: 20130215
# Last Modified: 20130215

import math

def m_series(i):
    space=round(math.log10(i))+1
    formas="{0:<%ds}"%(space+5)
    formad="{0:<%dd}"%(space+5)
    formaf="{0:<%d.11f}"%(space+11)
    print(formas.format("i"),"m(i)")
    num=float(0)
    for j in range(1,i+1,2):
        num=num+float(1)/float(j*2-1)-float(1)/float(j*2+1)
        print(formad.format(j),formaf.format(num*float(4)))
m_series(19)
