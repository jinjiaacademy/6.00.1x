#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 21:10:29 2023

@author: jinjialiu
"""
# balance = 484
# annualInterestRate = 0.2
# monthlyPaymentRate = 0.04

# i = 1
# while i <= 12:
#     monthlyInterestRate = annualInterestRate/12.0
#     minimumMonthlyPayment = balance * monthlyPaymentRate
#     unpaidBalance = balance - minimumMonthlyPayment
#     updatedBalance = unpaidBalance + monthlyInterestRate * unpaidBalance
#     balance = updatedBalance
#     i += 1

# print(f'Remaining Balance: {round(balance, 2)}')

# balance = 3329
# annualInterestRate = 0.2

# monthlyInterestRate = annualInterestRate/12.0
# fixedPayment = 10

# def calBalance(balance, monthlyInterestRate):
#     i = 1
#     while i <= 12:
#         unpaidBalance = balance - fixedPayment
#         balance = unpaidBalance + unpaidBalance * monthlyInterestRate
#         i += 1
#     return balance

# while calBalance(balance, monthlyInterestRate) > 0:
#     fixedPayment += 10
#     calBalance(balance, monthlyInterestRate)

# print("Lowest Payment is:", str(fixedPayment))

