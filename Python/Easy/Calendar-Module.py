import calendar
m,d,y = map(int,input().split())
result = (calendar.day_name[calendar.weekday(y,m,d)])
print(result.upper())