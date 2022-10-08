#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    from collections import OrderedDict
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())

    z=zip(*arr)
    l1=list(z)
    #print(arr,l1[k])
    def sorting(l):
        index=[]
        sortd=[]
        for i in range(len(l)):
            sortd.append(min(l))
            index.append(l.index(min(l)))
            l[l.index(min(l))]=1000000000
        return index,sortd
    x,y=sorting(list(l1[k]))
    #print(x,y)
    l2=[]
    for i in range(m):
        l3=[]
        if i!=k:
            for j in range(len(x)):
                l3.append(list(l1[i])[x[j]])
            l2.append(l3)
        else:
            l2.append(y)
                
        
        
    #print(l2)
    for i in range(n):
        s=''
        for j in range(m):
            s=s+' '+str(l2[j][i])
        print(s.rstrip()[1:])
        

    
