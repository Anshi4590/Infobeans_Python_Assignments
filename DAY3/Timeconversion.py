'''Assignment 10: Time Conversion

Convert total seconds into hours, minutes, and seconds.

Input:
Total seconds = 7384

Expected Output:
Hours = 2
Minutes = 3
Seconds = 4'''



sec = int(input("Enter the total seconds:"))
hours = sec//3600
rem = sec%3600
min = rem//60
rem1 = rem%60
print("Hours:",hours)
print("Minutes:",min)
print("seconds:",rem1)