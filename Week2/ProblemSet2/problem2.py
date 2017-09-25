#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 00:46:39 2017

@author: quangbk2010
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 23:46:59 2017

@author: quangbk2010

Problem: Now write a program that calculates the minimum fixed monthly payment needed in order 
pay off a credit card balance within 12 months. By a fixed monthly payment, we mean a single 
number which does not change each month, but instead is a constant amount that will be paid 
each month.

In this problem, we will not be dealing with a minimum monthly payment rate.

The following variables contain values as described below:

    + balance - the outstanding balance on the credit card

    + annualInterestRate - annual interest rate as a decimal
"""
balance = 999999
annualInterestRate = 0.18
monthlyInterestRate = annualInterestRate / 12
alpha0_ = 1 / (1 + monthlyInterestRate)
def findMin (tu, mau):
    minimum = tu // mau
    if (type (minimum / 10) == int):
        return minimum
    else:
        return (minimum // 10 + 1) * 10
def calculateGama (month):
    if month == 12:
        answer = 0
    else:
        answer = 1 + alpha0_ * calculateGama(month + 1)
        
    print  ("Answer for month", month, "is", answer)
    return answer

minMonthlyPayment = round (balance / calculateGama(0), 2)
"""findMin (balance, calculateGama(0))"""
print ("Lowest Payment:", minMonthlyPayment)

