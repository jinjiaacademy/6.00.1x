#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 10:45:40 2023

@author: jinjialiu
"""

"""
Write a program that examines three variables - x, y, and z - and 
prints the largest odd number among them. If none of them are odd,
it should print the smallest value of the three.
"""

x = int(input('Enter x: '))
y = int(input('Enter y: '))
z = int(input('Enter z: '))

# Solution 1

if x % 2 != 0 and y % 2 != 0 and z % 2 != 0:
    print(max(x, y, z))
if x % 2 != 0 and y % 2 != 0 and z % 2 == 0:
    print(max(x, y))
if x % 2 != 0 and y % 2 == 0 and z % 2 != 0:
    print(max(x, z))
if x % 2 != 0 and y % 2 == 0 and z % 2 == 0:
    print(x)
if x % 2 == 0 and y % 2 != 0 and z % 2 != 0:
    print(max(y, z))
if x % 2 == 0 and y % 2 != 0 and z % 2 == 0:
    print(y)
if x % 2 == 0 and y % 2 == 0 and z % 2 != 0:
    print(z)
if x % 2 == 0 and y % 2 == 0 and z % 2 == 0:
    print(min(x, y, z))
    
# Solution 2

answer = min(x, y, z)
if x % 2 != 0:
    answer = x
if y % 2 != 0 and y > answer:
    answer = y
if z % 2 != 0 and z > answer:
    answer = z
print(answer)