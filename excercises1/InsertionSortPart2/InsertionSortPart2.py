#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort2' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort2(n, arr):
    # Write your code here
    
    for i in range(1,n):
        min1=arr[i]
        for j in range(0,i):
            if min1<arr[j]:
                
                list1=arr[j:]
                arr[j]=min1
                list1.remove(min1)
                for k in range(j+1,n):
                    arr[k]=list1[k-j-1]
                break
   
        print(*arr)
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
