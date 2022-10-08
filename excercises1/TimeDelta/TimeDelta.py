#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the time_delta function below.
def time_delta(t1, t2):
  import datetime
  t1=t1.split()
  t2=t2.split()
  y=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
  print(str(t1[5]))
  dt1 = datetime.datetime(int(t1[3]),y.index(t1[2])+1,int(t1[1]),int(t1[4][0:2]),int(t1[4][3:5]),int(t1[4][6:8]))
  
  #dt1_gmt=datetime.datetime(int(t1[3]),y.index(t1[2])+1,int(t1[1]),int(t1[5][1:3]),int(t1[5][3:5]))
  if t1[5][0]=='-':
    dt1=dt1+datetime.timedelta(hours=int(t1[5][1:3]), minutes=int(t1[5][3:5]))
   
  else:
   
    dt1=dt1+datetime.timedelta(hours=-int(t1[5][1:3]),minutes=-int(t1[5][3:5]))
 
  dt2 = datetime.datetime(int(t2[3]),y.index(t2[2])+1,int(t2[1]),int(t2[4][0:2]),int(t2[4][3:5]),int(t2[4][6:8]))
  if t2[5][0]=='-':
    
    dt2=dt2+datetime.timedelta(hours=int(t2[5][1:3]),minutes=int(t2[5][3:5]))
   
  else:
    dt2=dt2+datetime.timedelta(hours=-int(t2[5][1:3]),minutes=-int(t2[5][3:5]))
  print(dt2)
  #dt2_gmt=datetime.datetime(int(t1[3]),y.index(t1[2])+1,int(t1[1]),int(t2[5][1:3]),int(t2[5][3:5]))
  time_diff=dt1-dt2
  print(time_diff)
  tsecs=time_diff.total_seconds()
  
  #time_diff_gmt=dt1_gmt-dt2_gmt
  #tsecs_gmt=time_diff_gmt.total_seconds()
  
#   gmt_tsecs=((int(t1[5])-int(t2[5]))//100)*3600+((int(t1[5])-int(t2[5]))%100)*60
  
#   total_sec=tsecs-tsecs_gmt
  return str(abs(int(tsecs)))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
