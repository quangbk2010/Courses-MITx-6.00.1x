#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 23:46:59 2017

@author: quangbk2010

Problem: Write a program to calculate the credit card balance after one year 
if a person only pays the minimum monthly payment required by the credit card company each month.
At the end of 12 months, print out the remaining balance. 
Be sure to print out no more than two decimal digits of accuracy

The following variables contain values as described below:

    + balance - the outstanding balance on the credit card

    + annualInterestRate - annual interest rate as a decimal

    + monthlyPaymentRate - minimum monthly payment rate as a decimal
    
Monthly interest rate= (Annual interest rate) / 12.0
Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance) 
"""
balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
monthlyInterestRate = annualInterestRate / 12
def calculateBalance (month):
    if month == 1:
        remainBalance = balance * (1 - monthlyPaymentRate) * ( 1 + monthlyInterestRate)
    else:
        remainBalance = calculateBalance (month - 1) * (1 - monthlyPaymentRate) * ( 1 + monthlyInterestRate)
    print ("Month", month, "Remaining balance:", round (remainBalance, 2))
    return remainBalance

balanceAfter12Month = calculateBalance (12)
print ("Remaining balance:", round (balanceAfter12Month, 2))