
'''Assignment 8: Compound Interest

A person invests money in a bank that provides compound interest annually.

Input:
Principal = 10000
Rate = 5%
Time = 2 years

Expected Output:
Amount after interest = 11025.0'''



P = int(input("Enter the principal:"))
R = int(input("Enter the interest rate :"))
T = int(input("Enter the time:"))
A = P*(1 + (R/100))**T
CI = A-P
print( "Compound Interest:",CI)
print( "Amount After Interest:",A)
