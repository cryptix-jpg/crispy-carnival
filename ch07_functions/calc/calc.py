# DESCRIPTION : practicing functions by using a 4 way calculator 

import calc_util

print("Welcome to the Calculator\n")

num1 = float(input("What is the first number? "))
num2 = float(input("What is the second number? "))

print("\nSUM = ", calc_util.add(num1, num2))
print("DIFFERENCE = ", calc_util.subtract(num1, num2))
print("PRODUCT = ", calc_util.multiply(num1, num2))
print("QUOTIENT = ", calc_util.divide(num1, num2))

print("\nHave a nice, mathy day.")