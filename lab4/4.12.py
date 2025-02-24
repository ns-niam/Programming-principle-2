# Python: Dates (Examples and Theories from W3SCHOOL)
# A date in Python is not a data type of its own, but we can import a module named datetime to work with dates as date objects.

import datetime

x = datetime.datetime.now()  # To determine the current time.
print(x)

x = datetime.datetime.now()
print(x.year)
print(x.strftime("%A"))   
# Outputs the full name of the day of the week. Example: Monday, Tuesday.
print(x.strftime("%B"))   
# Outputs the full name of the month.
print(x.strftime("%Y"))   
# Outputs the year.
print(x.strftime("%d"))   
# Outputs the day.

y = datetime.datetime(2020, 5, 17)
print(y)

z = datetime.datetime(2018, 6, 1)
print(z.strftime("%B"))
print(z.strftime("%a")) 
print(z.strftime("%A")) 

t = datetime.datetime(1465, 7, 15)
print(z.strftime("%C"))
print(t)
print(z.strftime("%A"))
print(z.strftime("%a"))
print(z.strftime("%B"))
print(z.strftime("%Y"))
print(z.strftime("%b"))

import datetime 
x = datetime.datetime(2025, 2, 10)
print(x.strftime("%A"))

y = datetime.datetime(2025, 2, 11)
print(y.strftime("%A"))

z = datetime.datetime(2025, 2, 12)
print(z.strftime("%A"))

t = datetime.datetime(2025, 2, 13)
print(t.strftime("%A"))

b = datetime.datetime(2025, 2, 14)
print(b.strftime("%A"))

c = datetime.datetime(2025, 2, 15)
print(c.strftime("%A"))

d = datetime.datetime(2025, 2, 16)
print(d.strftime("%A"))
