#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k):
    # Write your code here
 s=''
 def sum1(s):
         sum=0
         for i in s:
            sum=sum+int(i)
         return str(sum)
 s=str(n)
 s=sum1(sum1(s)*k)
 
 while len(s)>1:
         sum=int(sum1(s))
         s=str(sum)
 return sum
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
