# Python: Date (First Exercise)
# Write a Python program to subtract five days from the current date

from datetime import datetime, timedelta
import datetime

x = datetime.datetime.now()  # To determine the current time.
print("Current time: ", x)
y = timedelta(days=5)
result = x - y
print("Time after subtracting 5 days: ", result)
