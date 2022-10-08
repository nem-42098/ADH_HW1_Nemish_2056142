def average(array):
    # your code goes here
   set1=set(array)
   sum=0
   for i in set1:
     sum=sum+i
   return sum/len(set1)
