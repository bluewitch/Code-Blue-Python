import re
"""
Demonstration of using the Regular Expression libraries in Python to validate credit card numbers, 
we pre-compile our re, into TESTER and run a for loop to iterate through the interger input string, 
using .strip method to clean it up and spitting out a valid credit card number using if/else
"""
TESTER = re.compile(
    r"^"
    r"(?!.*(\d)(-?\1){3})"
    r"[456]"
    r"\d{3}"
    r"(?:-?\d{4}){3}"
    r"$")
for _ in range(int(input().strip())):
    print("Valid" if TESTER.search(input().strip()) else "Invalid")
