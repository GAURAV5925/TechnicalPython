
from calendar  import  TextCalendar, weekday

m,d,y = map(int,input().split())

year_format = TextCalendar(firstweekday=0).formatyear(y)
#Using this we declared the starting weekday to be in this case starting week will be monday hence we have kept the monday at the 0th index in the list


day = weekday(y,m,d)

#Weekday Function will return the day on which this date is located

days = ["MONDAY","TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY","SATURDAY","SUNDAY"]
#Here we created the list according to the starting week we considered


print(days[day])
