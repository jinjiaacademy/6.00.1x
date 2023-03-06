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
# x = -25
# epsilon = 0.01
# num_guesses, low = 0, 0
# high = max(1, x)
# ans = (high + low)/2

# while abs(ans**2 - x) >= epsilon:
#     print('low =', low, 'high =', high, 'ans =', ans)
#     num_guesses += 1
#     if ans ** 2 < x:
#         low = ans
#     else:
#         high = ans
#     ans = (high + low)/2
    
# print('number of guesses =', num_guesses)
# print(ans, 'is close to square root of', x)


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

"""
Figure 3-7 Implementation of Newton-Raphson method
"""
# # Newton-Raphson for square root
# # Find x such that x**2 - 24 is within epsilon of 0.01
# k = 24
# epsilon = 0.01
# guess = k/2
# num_guesses = 0

# while abs(guess**2 - k) >= epsilon:
#     guess = guess - ((guess**2) - k)/(2*guess)
#     num_guesses += 1
# print('Square root of', k, 'is about', guess)
# print('Number of guesses', num_guesses)
 

"""
Figure 4-1 Using bisection search to approximate square root of x
"""    
# # Find approximation to square root of x
# x = 25
# epsilon = 0.01

# if x < 0:
#     print('Does not exist')
# else:
#     low = 0
#     high = max(1, x)
#     ans = (high + low)/2
#     while abs(ans**2 - x) >= epsilon:
#         if ans**2 < x:
#             low = ans
#         else:
#             high = ans
#         ans = (high + low)/2
#     print(ans, 'is close to square root of', x)    
    
"""
Figure 4-2 Summing a square root and a cube root,hard way
"""
# # Find square root of x1
# x1 = 25
# epsilon = 0.01

# if x1 < 0:
#     print('Does not exist.')
# else:
#     low = 0
#     high = max(1, x1)
#     ans = (high + low)/2
#     while abs(ans**2 - x1) >= epsilon:
#         if ans**2 < x1:
#             low = ans 
#         else:
#             high = ans
#         ans = (high + low)/2

# x1_root = ans

# # Find cube root of x2
# x2 = -8
# if x2 < 0:
#     is_pos = False
#     x2 = -x2
# else:
#     is_pos = True
# low = 0
# high = (high + low)/2
# while abs(ans**3 - x2) >= epsilon:
#     if ans**3 < x2:
#         low = ans
#     else:
#         high = ans
#     ans = (high + low)/2
# if is_pos:
#     x2_root = ans
# else:
#     x2_root = -ans
#     x2 = -x2
# print('Sum of square root of', x1, 'and cube root of', x2,
#       'is close to', x1_root+x2_root)


"""
Figure 4-3 A function for finding roots
"""
def find_root(x, power, epsilon):
    # Find interval containing answer
    if x < 0 and power % 2 == 0:
        return None # negative number has no even-powered roots
    low = min(-1, x)
    high = max(1, x)
    # Use bisection search
    ans = (high + low)/2
    while abs(ans**power - x) >= epsilon:
        if ans**power < x:
            low = ans
        else:
            high = ans
        ans = (high + low)/2
    return ans

"""
Figure 4-4 Code to test find_root
"""
def test_find_root(x_vals, powers, epsilons):
    for x in x_vals:
        for p in powers:
            for e in epsilons:
                result = find_root(x, p, e)
                if result == None:
                    val = 'No root exists'
                else:
                    val = 'Okay'
                    if abs(result**p - x) > e:
                        val = 'Bad'
                print(f'x = {x}, power = {p}, epsilon = {e}:{val}')

x_vals = (0.25, 8, -8)
powers = (1, 2, 3)
epsilons = (0.1, 0.001, 1)
test_find_root(x_vals, powers, epsilons)