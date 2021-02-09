"""
-------------------------------------------------------------------------------
Name:   f_to_c.py
Purpose:  Write a program that lets you enter a degree measure in Fahrenheit and prints the result in celsius degree measure.
 
Author: Ku.T
 
Created:  02/08/2021
------------------------------------------------------------------------------
"""

fahrenheit = int(input("Fahrenheit: "))

celsius = (5/9 * int(fahrenheit - 32))

print(fahrenheit, "degrees fahrenheit is", celsius, "degrees celsius")