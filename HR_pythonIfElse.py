#!/bin/python3

n = int(input())
"""
Given an integer, perform the following conditional actions:
If  is odd, print Weird
If  is even and in the inclusive range of  to , print Not Weird
If  is even and in the inclusive range of  to , print Weird
If  is even and greater than , print Not Weird
"""
check = {True: "Not Weird", False: "Weird"}
print(check[ n%2==0 and (n in range(2,6) or n > 20)])
