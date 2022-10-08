# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar
#print(calendar.TextCalendar(0).formatyear(2015))
y=calendar.day_name
m=list(map(int,input().split()))

print(str(y[calendar.weekday(m[2],m[0],m[1])]).upper())
