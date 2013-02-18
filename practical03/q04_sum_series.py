# Name: q04_sum_series.py
# Author: Song Kai
# Description: Display the series in a table
# Created: 20130215
# Last Modified: 20130215

import math

def m_series(i):
    space=round(math.log10(i))+1
    formas="{0:<%ds}"%(space+5)
    formad="{0:<%dd}"%(space+5)
    formaf="{0:<%d.4f}"%(space+4)
    print(formas.format("i"),"m(i)")
    diff=float(0)
    for j in range(1,i+1):
        
        diff+=float(j)/float(j+1)
        print(formad.format(j),formaf.format(diff))

m_series(20)
