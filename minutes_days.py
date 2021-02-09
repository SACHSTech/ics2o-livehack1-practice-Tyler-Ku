"""
-------------------------------------------------------------------------------
Name:   minutes_days.py

Purpose:  Write a program that lets you enter a number of minutes, and that will calculate
the number of days, hours and minutes that represents (Hint: use the modulus operator).
 
Author: Ku.T
 
Created:  02/09/2021
------------------------------------------------------------------------------
"""

minutes = int(input("Minutes: "))

days = minutes//1440

days_remainder = minutes % 1440

hours = days_remainder//60

hours_remainder = days_remainder 

minutes

print(days, hours)

#print("There are", days, "days and", remainder,"hours in", hours, "hours")