# Name: q7_generate_payroll.py 
# Author: Song Kai
# Description: Read  information and prints a payroll statement
# Created: 20130121

name= input("Enter name: ")
time= int(input("Enter number of hours worked weekly: "))
pay= float(input("Enter hourly pay rate: "))
cpf= int(input("Enter CPF contribution rate(%): "))

print("Payroll statement for ",name)
print("Number of hours worked in week: ",time)
print("Hourly pay rate: $",pay)
print("Gross pay = $","{0:<4.2f}".format(pay*time))
print("CPF contribution at ",cpf,"% = $", "{0:<4.2f}".format(pay*time*cpf/100))
print("Net pay = $", "{0:<4.2f}".format(pay*time*(100-cpf)/100))
