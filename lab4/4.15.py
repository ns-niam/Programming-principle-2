#Python: date (Third exercise)
#Write a Python program to drop microseconds from datetime

from datetime import datetime
import datetime

x = datetime.datetime.now()
print("Date and time with microseconds: ", x)

drop = x.replace(microsecond = 0)
print("Date and time without microseconds: ", drop)
