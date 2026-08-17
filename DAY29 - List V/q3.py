'''3.

MATRIX PERFORMANCE EVALUATION SYSTEM

A company records the monthly performance scores of employees in a matrix format. Each row represents an employee and each column represents a month.

The HR department wants a menu-driven application to analyze employee performance.

Menu
1. Find Employee with Highest Total Score
2. Find Month with Lowest Average Score
3. Display Employee-wise Maximum Score
4. Exit
Requirements
Choice 1 – Find Employee with Highest Total Score
Calculate the sum of each row.
Display the employee number having the highest total score.
Choice 2 – Find Month with Lowest Average Score
Calculate the average of each column.
Display the month having the lowest average score.
Choice 3 – Display Employee-wise Maximum Score
Find and display the maximum value present in each row.
Sample Input
10 20 30
40 50 60
25 35 45
Output
Employee 2 has Highest Total Score = 150

Month 1 Average = 25
Month 2 Average = 35
Month 3 Average = 45

Employee 1 Max Score = 30
Employee 2 Max Score = 60
Employee 3 Max Score = 45
'''
while True:
    print("-------- Menu --------")
    print("1. Find Employee with Highest Total Score")
    print("2. Find Month with Lowest Average Score")
    print("3. Display Employee-wise Maximum Score")
    print("4. Exit")

    r = int(input("Enter number of rows for first matrix : "))
    c = int(input("Enter number of columns for first matrix : "))

    a = []

    print("Enter elements for first matrix : ")
    for i in range(r):
        row = []
        for j in range(c):
            row.append(int(input()))
        a.append(row)
    print(a)
    choice = int(input("Enter your choice : "))

    match choice:

        case 1:
            max = 0
           
            for i in a:
                sum = 0
                for j in i:
                    sum+=j
                if sum>max:
                   max = sum
                   place = i
            print(f"Employee {(place)} has Highest Total Score = {max}")

        case 2:


            min=0
            total=0

            for i in range (r):
               
               total+=a[i][0]
            min=total//r
            month=1

            print(f"Month {month} avg is : {min}")

            for col in range(1,c):
                sum=0
                for row in range(r):
                    n=a[row][col]
                    sum+=n
                avg=sum//r
                

                print(f"Month {col+1} avg is :{avg}")

                if avg<min:
                    min=avg
                    month=col+1
            print(f"Min Average Of Month {month}: {min}")
            
       


            
            
            
        case 3:
            max = 0
            
            for i in a:
                for j in i:
                  if j>max:
                    max = j
                    place = i
                print(f"Employee {(place)} has Max Score = {max}")

        case 4:
            print("Exit")
