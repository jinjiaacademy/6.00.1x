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

balance = 999999
annualInterestRate = 0.18

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

initBalance = balance
monthlyInterestRate = annualInterestRate/12.0
low = balance/12.0
high = (balance * ((1.0 + monthlyInterestRate)**12))/12.0
epsilon = 0.01
minPay = (high + low)/2.0
month = 0
def calculate(month, balance, minPay, monthlyInterestRate):
    while month <12:
        unpaidBalance = balance - minPay
        balance = unpaidBalance + (monthlyInterestRate * unpaidBalance)
        month += 1
    return balance   

while abs(balance) >= epsilon:
    balance = initBalance
    month = 0
    balance = calculate(month, balance, minPay, monthlyInterestRate)
    if balance > 0:
        low = minPay
    else:
        high = minPay
    minPay = (high + low)/2.0
minPay = round(minPay,2)
print('Lowest Payment: ' + str(minPay))