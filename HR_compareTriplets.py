#!/bin/python3
# compareTriplets.py

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    score_a = 0
    score_b = 0
    for i in range(len(a)):
        if a[i] > b[i]:
            score_a += 1
        elif a[i] < b[i]:
            score_b += 1
    return score_a, score_b

a0,a1,a2 = input().strip().split(' ')
a = [int(a0),int(a1),int(a2)]

b0,b1,b2 = input().strip().split(' ')
b = [int(b0),int(b1),int(b2)]

print('%d %d' % compareTriplets(a,b))
"""
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
"""
"""
Yes a little sloppy, had to work it out in a way that made sense to me.
Hacker Rank put in the extra code I commentted out
"""
