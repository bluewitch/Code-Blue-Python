#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the diagonalDifference function below.
def diagonalDifference(arr):
    # Instead of indexing to access the rows, you could use iteration:
    l = sum(row[i] for i, row in enumerate(arr))
    
    # Instead of doing two passes over arr to calculate l and r, you could accumulate the 
    # difference in one pass: (note also negative indexing from end of list)
    difference = sum(row[i] - row[-i-1] for i, row in enumerate(arr))
    return abs(difference)

    # Optimized by The single-pass approach would also allow you to process input line by line,
    # instead of storing the whole arr in memory.
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
