#!/bin/python3

# Complete the plusMinus function below.

import math
import os
import random
import re
import sys

def plusMinus(arr):
    positive_count = 0
    zero_count = 0
    negative_count = 0
    #hackerrank takes care of the reading of input()
    #n = int(input().strip())
    #arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
    for num in arr:
        if num > 0:
            positive_count += 1
        elif num == 0:
            zero_count += 1
        else:
            negative_count += 1

    print(positive_count / n)
    print(negative_count / n)
    print(zero_count / n)
    
    #needto return or EOF error
    return()
    
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

plusMinus(arr)
