#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(num_stairs):
    for stairs in range(1, num_stairs + 1):
        # just remember print has ()
        print (' ' * (num_stairs - stairs) + '#' * stairs)
    return()
    
if __name__ == '__main__':
    n = int(input())

    staircase(n)
