# lab assingments 1
# <<<<< QUE 1 >>>>>>>

# a =   input("Enter employee details:")
# n =   input("name:", )
# eid = input("Employee Id:",)
# dep = input("Department:", )
# BS =  int(input("Basic Salary:", ))
# DA = (92/100)*BS
# HRA = (58/100)*BS
# TA = (30/100)*BS
# LIC = BS+DA+HRA+TA-500
# print("DA:",DA)
# print("HRA:",HRA)
# print("TA:",TA)
# print("LIC:",LIC)

# <<<<<<  QUE 2 >>>>>>>>

# n = input("Name of Vendor : ")
# y = int(input("Year of Association : "))
# c = input("Contact number : ")
# e = input("Email Id : ")
# count = 0
# for i in range(1, 12+1):
#     d = int(input("Enter monthly purchase : "))
#     count += d
# print("Name : ", n)
# print("Year of Association : ", y)
# print("Contact Number : ", c)
# print("Email Id : ", e)
# print("Annual Amount : ", count)

#---------------------lab assignments 2----------------------
#<<<<<<< QUE 1 >>>>>>>
# V = int(input("Enter the voltage:"))
# R = int(input("Enter the resistance:"))
# i = V/R
# print(i)
# if i < 0.5 :
#     print("Low current")
# elif 0.5 <= i <= 2.0:
#     print("Normal current")
# else:
#     print("High current")

#<<<<<<< QUE 2 >>>>>>>
# h = float(input("Enter hardness: "))
# c = float(input("Enter carbon content: "))
# t = float(input("Enter tensile strength: "))
# cond1 = h > 50
# cond2 = c < 0.7
# cond3 = t > 5600
# if cond1 and cond2 and cond3:
#     print("Grade is 10")
# elif cond1 and cond2:
#     print("Grade is 9")
# elif cond2 and cond3:
#     print("Grade is 8")
# elif cond1 and cond3:
#     print("Grade is 7")
# elif cond1 or cond2 or cond3:
#     print("Grade is 6")
# else:
#     print("Grade is 5")