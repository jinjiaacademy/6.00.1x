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

"""
Change the code in Figure 3-2 so that it returns the largest rather
than the smallest divisor. Hint: if y*z = x and y is the smallest
divisor of x, z is the largest divisor of x.
"""

# x = int(input('Enter an integer: '))
# smallest_divisor = None

# for guess in range(2, x):
#     if x % guess == 0:
#         smallest_divisor = guess
#         break

# if smallest_divisor != None:
#     print('The largest divisor is', x/smallest_divisor)
# else:
#     print(x, 'is a prime number')
    
"""
Write a program that asks the user to enter an integer and prints
two integers: root and pwr, such that 1 < pwr < 6 and root**pwr
is equal to the integer entered by the user. If no such pair of 
integers exists, it should print a message to that effect.
"""
# x = int(input('Enter an integer: '))

# for pwr in range(2, 6):
#     for root in range(1, x):
#         if root**pwr == x:
#             print(f'{root} ** {pwr} = {x}')
#             break
# else:
#     print('No such pair of integers exists.')

"""
Write a program that prints the sum of the prime numbers greater
than 2 and less than 1000. Hint: you probably want to have a loop
that is a primality test nested inside a loop that iterates over
the odd integers between 3 and 999.
"""
# total = 0

# for num in range(3, 1000, 2):
#     is_prime = True
#     for div in range(2, num):
#         if num % div == 0:
#             is_prime = False
#             break
#     if is_prime == True:
#         total += num
        
# print(total)

"""
What would have to be changed to make the code in Figure 3-5 work
for finding an approximation to the cube root of both negative and 
positive numbers? 
Hint: think about changing low to ensure that the answer lies within
the region being searched.
"""
x = float(input("Enter a number: "))
epsilon = 0.01
low = min(-1.0, x)
high = max(1.0, x)
guess = (low + high) / 2.0
num_guesses = 0

while abs(guess ** 3 - x) >= epsilon:
    if guess ** 3 < x:
        low = guess
    else:
        high = guess
    guess = (low + high) / 2.0
    num_guesses += 1

print("Number of guesses:", num_guesses)
print("Approximation to the cube root of", x, "is:", guess)


"""
The Empire State Building is 102 stories high. A man want to know
the highest floor from which he could drop an egg without the egg
breaking. He proposed to drop an egg from the top floor. If it broke,
he would go down a floor, and try it again. He would do this until
the egg did not break. At worst, this method requires 102 eggs. 
Implement a method that at worst uses seven eggs.
"""
