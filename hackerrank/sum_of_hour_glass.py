# https://www.hackerrank.com/challenges/2d-array/problem 
#!/bin/python

import math
import os
import random
import re
import sys


# Complete the hourglassSum function below.
def hourglassSum(arr):
    sum_of_hg = []
    for i in range(len(arr) - 2):
        for k in range(len(arr) - 2):
            s = 0
            s += arr[i][k] + arr[i][k + 1] + arr[i][k + 2]
            s += arr[i + 1][k + 1]
            s += arr[i + 2][k] + arr[i + 2][k + 1] + arr[i + 2][k + 2]
            sum_of_hg.append(s)

    return max(sum_of_hg)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in xrange(6):
        arr.append(map(int, raw_input().rstrip().split()))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
