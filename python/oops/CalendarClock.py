from clock import Clock
from calendar import Calendar

class CalendarClock(Clock, Calendar):
   def __init__(self, day,month,year,hours=0, minutes=0,seconds=0):
        Calendar.__init__(self, day, month, year)
        Clock.__init__(self, hours, minutes, seconds)
   def __str__(self):
       return Calendar.__str__(self) + ", " + Clock.__str__(self)

if __name__  == "__main__":
   x = CalendarClock(24,12,57)
   print(x)
   for i in range(1000):
      x.tick()
   for i in range(1000):
      x.advance()
   print(x)
