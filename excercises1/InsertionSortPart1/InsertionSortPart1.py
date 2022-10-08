#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    sort_n=arr[-1]
    for i in range(n):
        if arr[n-i-2]>sort_n and (n-i-2>=0):
            arr[n-i-1]=arr[n-i-2]
            print(*arr)
        elif n-i-2<0:
            arr[0]=sort_n
            print(*arr)
        else:
            arr[n-i-1]=sort_n
            print(*arr)
            break
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
