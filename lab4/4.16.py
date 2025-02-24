# Python: Date (Third Exercise)
# Write a Python program to calculate the difference between two dates in seconds

from datetime import datetime

time1 = datetime(2025, 2, 1, 14, 0, 0)
time2 = datetime(2025, 2, 1, 14, 2, 30)

difference = time2 - time1  # Calculate the difference between two times.

seconds = difference.total_seconds()  # Convert the difference to seconds.

print(seconds)
