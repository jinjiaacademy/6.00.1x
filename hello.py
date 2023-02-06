# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 22:37:05 2023

@author: Jinjia Liu
"""

# print('hello world')
# print('I like 6.00.1x!')

# num = 0
# while num <= 5:
#     print(num)
#     num += 1
# print("Outside of loop")
# print(num)

# numberOfLoops = 0
# numberOfApples = 2
# while numberOfLoops < 10:
#     numberOfApples *= 2
#     numberOfApples += numberOfLoops
#     numberOfLoops -= 1
# print("Number of apples: " + str(numberOfApples))

# num = 10
# while num > 3:
#     num -= 1
#     print(num)

# num = 10
# while True:
#     if num < 7:
#         print('Breaking out of loop')
#         break
#     print(num)
#     num -= 1
# print('Outside of loop')

# num = 100
# while not False:
#     if num < 0:
#         break
# print('num is: ' + str(num))

# print('Hello!')
# num = 10

# while num > 0:
#     if num % 2 == 0:
#         print(num)
#     num -= 1

# total = 0
# num = 1
# end = 6

# while num <= end:
#     total += num
#     num += 1
# print(total)

# for num in range(11):
#     if num % 2 == 0:
#         print(num)
# print('Goodbye!')

# num = 10
# for num in range(5):
#     print(num)
# print(num)

# divisor = 2
# for num in range(0, 10, 2):
#     print(num/divisor)

# for variable in range(20):
#     if variable % 4 == 0:
#         print(variable)
#     if variable % 16 == 0:
#         print('Foo!')

# for letter in 'hola':
#     print(letter)

# count = 0
# for letter in 'Snow!':
#     print('Letter # ' + str(count) + ' is ' + str(letter))
#     count += 1
#     break
# print(count)

# greeting = 'Hello!'
# count = 0

# for letter in greeting:
#     count += 1
#     if count % 2 == 0:
#         print(letter)
#     print(letter)
# print('done')

# school = 'Massachusetts Institute of Technology'
# numVowels = 0
# numCons = 0

# for char in school:
#     if char == 'a' or char == 'e' or char == 'i'\
#         or char == 'o' or char == 'u':
#             numVowels += 1
#     elif char == 'o' or char == 'M':
#         print(char)
#     else:
#         numCons -= 1

# print('numVowels is: ' + str(numVowels))
# print('numCons is: ' + str(numCons))

# iteration = 0
# count = 0
# while iteration < 5:
#     for letter in "hello, world":
#         count += 1
#     print("Iteration " + str(iteration) + "; count is: " + str(count))
#     iteration += 1 
    
# for iteration in range(5):
#     count = 0
#     while True:
#         for letter in "hello, world":
#             count += 1
#         print("Iteration " + str(iteration) + "; count is: " + str(count))

# for iteration in range(5):
#     count = 0
#     while True:
#         for letter in "hello, world":
#             count += 1
#         print("Iteration " + str(iteration) + "; count is: " + str(count))
#         break

# count = 0
# phrase = "hello, world"
# for iteration in range(5):
#     index = 0
#     while index < len(phrase):
#         count += 1
#         index += 1
#     print("Iteration " + str(iteration) + "; count is: " + str(count))

# count = 0
# phrase = "hello, world"
# for iteration in range(5):
#     while True:
#         count += len(phrase)
#         break
#     print("Iteration " + str(iteration) + "; count is: " + str(count))

# count = 0
# phrase = "hello, world"
# for iteration in range(5):
#     count += len(phrase)
#     print("Iteration " + str(iteration) + "; count is: " + str(count))

# count = 0
# vowels = 'aeiou'

# for char in s:
#     if char in vowels:
#         count += 1
# print('Number of vowels: ', count)


# s = 'azcbobobegghakl'

# count = 0

# for n in range(len(s)):
#     if s[n:n+3] == 'bob':
#         count += 1
# print(count)



# s = 'azcbobobegghakl'

# longest = ""
# current = ""
# for i in range(len(s)):
#     if i == 0:
#         current = s[i]
#     elif s[i] >= s[i-1]:
#         current += s[i]
#     else:
#         if len(current) > len(longest):
#             longest = current
#         current = s[i]
# if len(current) > len(longest):
#     longest = current

# print(longest)

# iteration = 0
# count = 0
# while iteration < 5:
#     # the variable 'letter' in the loop stands for every 
#     # character, including spaces and commas!
#     for letter in "hello, world": 
#         count += 1
#     print("Iteration " + str(iteration) + "; count is: " + str(count))
#     iteration += 1 

# iteration = 0
# while iteration < 5:
#     count = 0
#     for letter in "hello, world":
#         count += 1
#     print("Iteration " + str(iteration) + "; count is: " + str(count))
#     iteration += 1 

# iteration = 0
# while iteration < 5:
#     count = 0
#     for letter in "hello, world":
#         count += 1
#         if iteration % 2 == 0:
#             break
#     print("Iteration " + str(iteration) + "; count is: " + str(count))
#     iteration += 1 