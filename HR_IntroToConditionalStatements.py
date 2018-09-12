#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    #N = int(input())

    N = int(input().strip())
    # Done with Regular Expressions
    print("Not "*bool(re.match(r'^(..)(\1|\1{10,})?$','1'*N))+"Weird")
