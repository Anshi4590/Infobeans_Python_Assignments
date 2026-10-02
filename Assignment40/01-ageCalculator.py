'''Assignment 1 — Age Calculator

Create a program that accepts the user's date of birth and calculates:

Current age in years
Completed months
Total number of days lived
Next birthday date
Number of days remaining for the next birthday

Input:

Enter DOB (DD-MM-YYYY): 15-08-1998

Expected Output:

Age: 28 years
Total Days Lived: XXXXX days
Next Birthday: 15-08-2027
Days Remaining: XX days'''

from datetime import datetime ,date 
dob = input("Enter Date of birth in {dd-mm-yyyy}:")

#date of birth

dob  = datetime.strptime(dob,"%d-%m-%Y").date()
print(dob)

#date of today

today = date.today()
print(today)

# age 

age = today.year - dob.year
if (today.month,today.day)<(dob.month,dob.day):
    age =age-1
print(f"Age :{age}years")
    

#day lived

day=today-dob
print(day)

#next birthday date
nextYear=date(today.year+1,dob.month,dob.day)

#print(nextYear)


print(datetime.strftime(nextYear,"%d-%m-%Y"))

# days remaining

remain_days = nextYear - today
print(f"Days Remaining: {remain_days.days}days")