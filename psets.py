#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 12:02:54 2023

@author: jinjialiu
"""

""" PSET1 """

"""
Problem 1
Assume s is a string of lower case characters.
Write a program that counts up the number of vowels contained
in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. 
For example, if s = 'azcbobobegghakl', your program should print:

Number of vowels: 5
"""






"""
Problem 2
Assume s is a string of lower case characters.
Write a program that prints the number of times the string 'bob' 
occurs in s. For example, if s = 'azcbobobegghakl', then your 
program should print

Number of times bob occurs is: 2
"""







"""
Problem 3
Assume s is a string of lower case characters.
Write a program that prints the longest substring of s in which 
the letters occur in alphabetical order. For example, 
if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring. For example, 
if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc
"""




"""
In this problem, you'll create a program that guesses a secret 
number!
The program works as follows: you (the user) thinks of an integer 
between 0 (inclusive) and 100 (not inclusive). The computer makes 
guesses, and you give it input - is its guess too high or too low? 
Using bisection search, the computer will guess the user's secret 
number!
"""

print("Please think of a number between 0 and 100!")

# At the start the highest the number could be is 100 and the lowest is 0.
hi = 100
lo = 0
guessed = False

# Loop until we guess it correctly
while not guessed:
    # Bisection search: guess the midpoint between our current high and low guesses
    guess = (hi + lo)//2
    print("Is your secret number " + str(guess)+ "?")
    user_inp = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")

    if user_inp == 'c':
        # We got it right!
        guessed = True
    elif user_inp == 'h':
        # Guess was too high. So make the current guess the highest possible guess.
        hi = guess
    elif user_inp == 'l':
        # Guess was too low. So make the current guess the lowest possible guess.
        lo = guess
    else:
        print("Sorry, I did not understand your input.")

print('Game over. Your secret number was: ' + str(guess))

