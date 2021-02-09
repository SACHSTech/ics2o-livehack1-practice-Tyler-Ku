"""
-------------------------------------------------------------------------------
Name:   days_hours.py
Purpose:  Write a program that lets you enter a number of hours, and that converts it to days and hours. For example, 111 hours = 4 days and 15 hours.
 
Author: Ku.T
 
Created:  02/08/2021
------------------------------------------------------------------------------
"""

hours = int(input("Hours: "))

days = hours//24

remainder = hours % 24

print("There are", days, "days and", remainder,"hours in", hours, "hours")