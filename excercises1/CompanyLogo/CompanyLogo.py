#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    from collections import Counter
    s = input()
    l=list(s)
    l.sort()
    c1=Counter(l)
    d=c1.most_common(3)
    for i in range(3):
        print(d[i][0],d[i][1])
    
    # d=c1.most_common(3)
    # value=set([d[0][1], d[1][1] ,d[2][1]])
    # char1=[d[0][0], d[1][0] ,d[2][0]]
    # char2=[d[0][0], d[1][0] ,d[2][0]]
    
    # if len(value)==3:
    #     for i in range(3):
    #         print(d[i][0],d[i][1])
    # elif len(value)==1:
    #     char2.sort()
    #     for i in char2:
    #         print(i,d[char1.index(i)][1])
    # elif len(value)==2:
    #       if d[0][1]==d[1][1]:
    #           if d[0][0]> d[1][0]:
    #             print(d[1][0],d[1][1])
    #             print(d[0][0],d[0][1])
    #             print(d[2][0],d[2][1])
    #           else:
    #             for i in range(3):
    #                 print(d[i][0],d[i][1])
    #       if d[1][1]==d[2][1]:
    #           if d[1][0]> d[2][0]:
    #             print(d[0][0],d[0][1])
    #             print(d[2][0],d[2][1])
    #             print(d[1][0],d[1][1])
                
    #           else:
    #             for i in range(3):
    #                 print(d[i][0],d[i][1])
            
        
        
    
    
        
        
    
