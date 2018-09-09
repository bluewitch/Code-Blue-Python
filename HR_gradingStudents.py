#!/bin/python3

import os
import sys

#
# Complete the gradingStudents function below.
#
def gradingStudents(grades):
    # another elegant solution with a lambda function
    # map(lambda x: 5*(1 + x//5) if (x > 37 and ((x%5) > 2)) else x, grades)
    # but we will use this for the solution
    result = []
    for i in grades:
        if i >= 38:
            if i % 5 >= 3:
                i += (5 - i % 5)
        result.append(i)
    return result

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grades = []

    for _ in range(n):
        grades_item = int(input())
        grades.append(grades_item)

    result = gradingStudents(grades)

    f.write('\n'.join(map(str, result)))
    f.write('\n')

    f.close()
