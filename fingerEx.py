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

# x = int(input('Enter x: '))
# y = int(input('Enter y: '))
# z = int(input('Enter z: '))

# # # Solution 1

# if x % 2 != 0 and y % 2 != 0 and z % 2 != 0:
#     print(max(x, y, z))
# if x % 2 != 0 and y % 2 != 0 and z % 2 == 0:
#     print(max(x, y))
# if x % 2 != 0 and y % 2 == 0 and z % 2 != 0:
#     print(max(x, z))
# if x % 2 != 0 and y % 2 == 0 and z % 2 == 0:
#     print(x)
# if x % 2 == 0 and y % 2 != 0 and z % 2 != 0:
#     print(max(y, z))
# if x % 2 == 0 and y % 2 != 0 and z % 2 == 0:
#     print(y)
# if x % 2 == 0 and y % 2 == 0 and z % 2 != 0:
#     print(z)
# if x % 2 == 0 and y % 2 == 0 and z % 2 == 0:
#     print(min(x, y, z))
    
# # Solution 2

# answer = min(x, y, z)
# if x % 2 != 0:
#     answer = x
# if y % 2 != 0 and y > answer:
#     answer = y
# if z % 2 != 0 and z > answer:
#     answer = z
# print(answer)

"""
Write code that asks the user to enter their birthday in the form
mm/dd/yyyy, and then prints a string of the form 'You were born in 
the year yyyy.'
"""

# dob = input('Enter your birthday (mm/dd/yyyy): ')
# year = dob[-4:]
# print(f'You were born in the year {year}.')

"""
Replace the comment in the following code with a while loop
"""
# num_x = int(input('How many times should I print the letter X? '))
# to_print = ''
# # concatenate X to to_print num_x times
# while num_x > 0:
#     to_print += 'X'
#     # print(to_print)
#     num_x -= 1
# print(to_print)

"""
Write a program that asks the user to input 10 integers, and then
prints the largest odd number that was entered. If no odd number
was entered, it should print a message to that effect.
"""
# largest_odd = 0
# loops = 0

# while loops < 10:
#     num = int(input('Enter a number: '))
#     if num % 2 != 0 and num > largest_odd:
#         largest_odd = num
#     loops += 1

# if largest_odd:
#     print(f'The largest odd number was entered is {largest_odd}.')
# else:
#     print('No odd number was entered.')

"""
Write a program that prints the sum of the prime numbers greater
than 2 and less than 1000. Hint: you probably want to use a for 
loop that is a primality test nested inside a for loop that iterates
over the odd integers between 3 and 999.
"""

# total = 0

# for num in range(3, 1000, 2):
#     is_prime = True
#     for div in range(2, num):
#         if num % div == 0:
#             is_prime = False
#             break
#     if is_prime:
#         total += num
        
# print(total)

       