def is_leap(year):
    leap = False
    
    # Write your logic here
    if year>=1900 & year<=100000:
        if year%4==0:
            if year%100==0 and year%400==0:
                leap=True
            if year%100!=0:
                leap=True
    return leap

