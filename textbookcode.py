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

"""
Figure 3-1 Using exhaustive enumeration to find the cube root
"""
# # Find the cube root of a perfect cube
# x = int(input('Enter an integer: '))
# ans = 0
# while ans**3 < abs(x):
#     # print('Value of the decrementing function abs(x)-ans**3 is', 
#     #       abs(x)-ans**3)
#     ans = ans + 1
# if ans**3 != abs(x):
#     print(x, 'is not a perfect cube')
# else:
#     if x < 0:
#         ans = -ans
#     print('Cube root of', x, 'is', ans)

# max_val = int(input('Enter a positive integer: '))
# i = 0
# while i < max_val:
#     i = i + 1
# print(i)

"""
Figure 3-2 Using exhaustive enumeration to test primality
"""
# # Test if an int > 2 is prime. If not, print samllest divisor
# x = int(input('Enter an integer greater than 2: '))
# smallest_divisor = None

# for guess in range(2, x):
#     if x % guess == 0:
#         smallest_divisor = guess
#         break
# if smallest_divisor != None:
#     print('Smallest divisor of', x, 'is', smallest_divisor)
# else:
#     print(x, 'is a prime number')
    
"""
Figure 3-3 A more efficient primality test
"""
# # Test if an int > 2 is prime. If not, print smallest divisor
# x = int(input('Enter an integer greater than 2: '))
# smallest_divisor = None

# if x % 2 == 0:
#     smallest_divisor = 2
# else:
#     for guess in range(3, x, 2):
#         if x % guess == 0:
#             smallest_divisor = guess
#             break

# if smallest_divisor != None:
#     print('Smallest divisor of', x, 'is', smallest_divisor)
# else:
#     print(x, 'is a prime number')

"""
Figure 3-4 Approximating the square root using exhaustive 
enumeration
"""
# # x = int(input('Enter an integer: '))
# x = 123456
# epsilon = 0.01
# step = epsilon**3
# num_guesses = 0
# ans = 0.0

# while abs(ans**2 - x) >= epsilon and ans*ans <= x:
#     ans += step
#     num_guesses += 1
    
# print('number of guesses =', num_guesses)

# if abs(ans**2 - x) >= epsilon:
#     print('Failed on square root of', x)
# else:
#     print(ans, 'is close to square root of', x)

"""
Figure 3-5 Using bisection search to approximate square root
"""
x = -25
epsilon = 0.01
num_guesses, low = 0, 0
high = max(1, x)
ans = (high + low)/2

while abs(ans**2 - x) >= epsilon:
    print('low =', low, 'high =', high, 'ans =', ans)
    num_guesses += 1
    if ans ** 2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2
    
print('number of guesses =', num_guesses)
print(ans, 'is close to square root of', x)


"""
Figure 3-6 Using bisection search to estimate log base 2
"""
# # Find lower bound on ans
# x = 100
# lower_bound = 0
# epsilon = 0.01

# while 2**lower_bound < x:
#     lower_bound += 1
    
# low = lower_bound - 1
# high = lower_bound + 1

# # perform bisection search 
# ans = (high + low)/2
# while abs(2**ans - x) >= epsilon:
#     if 2**ans < x:
#         low = ans
#     else:
#         high = ans
#     ans = (high + low)/2
# print(ans, 'is close to the log base 2 of', x)