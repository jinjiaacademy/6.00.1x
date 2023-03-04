#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 12:26:30 2023

@author: jinjialiu
"""

"""
Figure 2-7 Squaring an integer, the hard way
"""
# x = 3
# ans = 0
# num_iterations = 0
# while (num_iterations < x):
#     ans = ans + x
#     num_iterations = num_iterations + 1
#     print(f'x={x}, ans={ans}, num_iterations={num_iterations}')
# print(f'{x} * {x} = {ans}')

# x = 3
# ans = 0
# for num_iterations in range(abs(x)):
#     ans = ans + abs(x)
# print(f'{x} * {x} = {ans}')

# # Find a positive integer that is divisible by both 11 and 12
# x = 1
# while True:
#     print(x)
#     if x % 11 == 0 and x % 12 == 0:
#         break
#     x += 1
    
# print(x, 'is divisible by 11 and 12.')

# x = int(input('Enter an integer: '))
# if x % 2 == 0:
#     print('')
#     print('Even')
# else:
#     print('')
#     print('Odd')
# print('Done with conditional.')

