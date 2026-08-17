'''1.
=========================================================
        MATRIX OPERATIONS MANAGEMENT SYSTEM
=========================================================


A data analysis company stores numerical information in matrix form.
To help employees perform matrix-related operations efficiently,
the company wants a menu-driven application.

The application should allow the user to:

1. Add Two Matrices
2. Subtract Two Matrices
3. Compare Two Matrices
4. Exit

The user must enter the number of rows, columns, and all matrix
elements. The program should perform the selected operation and
display the result.

---------------------------------------------------------
Requirements
---------------------------------------------------------

1. Display the following menu repeatedly until the user chooses Exit.

   1. Add Two Matrices
   2. Subtract Two Matrices
   3. Compare Two Matrices
   4. Exit

2. Read the number of rows and columns from the user.

3. Read all elements of Matrix A and Matrix B from the user whenever
   required.

4. Based on the user's choice:

   Choice 1 - Add Two Matrices
   --------------------------------
   Add corresponding elements of both matrices and display
   the resultant matrix.

5. Choice 2 - Subtract Two Matrices
   --------------------------------
   Subtract corresponding elements of Matrix B from Matrix A
   and display the resultant matrix.

6. Choice 3 - Compare Two Matrices
   --------------------------------
   Check whether both matrices are equal.

   Two matrices are considered equal if:
   - They have the same dimensions.
   - Corresponding elements are equal.

   Display:
   "Matrices are Equal"
   or
   "Matrices are Not Equal"

7. Choice 4 - Exit
   --------------------------------
   Display:
   "Thank You for Using Matrix Operations Management System"

---------------------------------------------------------
Sample Input/Output
---------------------------------------------------------

Menu
1. Add Two Matrices
2. Subtract Two Matrices
3. Compare Two Matrices
4. Exit

Enter your choice: 1

Enter number of rows: 2
Enter number of columns: 2

Enter Matrix A:
1 2
3 4

Enter Matrix B:
5 6
7 8

Result Matrix:
6 8
10 12

---------------------------------------------------------

Menu
1. Add Two Matrices
2. Subtract Two Matrices
3. Compare Two Matrices
4. Exit

Enter your choice: 3

Enter number of rows: 2
Enter number of columns: 2

Enter Matrix A:
1 2
3 4

Enter Matrix B:
1 2
3 4

Output:
Matrices are Equal

---------------------------------------------------------

Menu
1. Add Two Matrices
2. Subtract Two Matrices
3. Compare Two Matrices
4. Exit

Enter your choice: 4

Output:
Thank You for Using Matrix Operations Management System

========================================================'''
while True:
    print("-------- Menu --------")
    print("1. Add Two Matrices")
    print("2. Subtract Two Matrices")
    print("3. Compare Two Matrices")
    print("4. Exit")

    r1 = int(input("Enter number of rows for first matrix : "))
    c1 = int(input("Enter number of columns for first matrix : "))
    print = int(input("Enter elements for first matrix : "))
    a = []

    
    r2 = int(input("Enter number of the rows for second matrix : "))
    c2 = int(input("Enter number of the columns for second matrix : "))
    
    b = []

    choice = int(input("Enter your choice : "))
    if r1!=r2 or c1!=c2:
        print("Operation on Matrix not possible ")

    else:

        print = int(input("Enter elements for first matrix : "))
        for i in range(r1):
                row = []
                for j in range(c1):
                    row.append(int(input()))
                a.append(row)

        print = int(input("Enter elements for second matrix : "))
        for i in range(r2):
            row = []
            for j in range(c2):
                row.append(int(input()))
            b.append(row)

        result = []

        match choice:

            case 1:
                    print("1. Adding Two Matrix: ")
                    for i in range(len(a)):
                        row=[]
                        for j in range(len(b)):
                            row.append(a[i][j]+b[i][j])
                        result.append(row)
                        

            case 2:
                    print("2. Subtracting two matrix :")
                    for i in range(len(a)):
                        row=[]
                        for j in range(len(b)):
                            row.append(a[i][j]-b[i][j])
                        result.append(row)

            case 3:
                print("3. comparing two matrix :")
                flag = 1
                for i in range(len(a)):
                    for j in range(len(b)):
                        if (a[i][j])!=(b[i][j]):
                            flag = 0
                            print("Two matrix are not equal")
                            break
                if flag == 1:
                    print("Two matrix are Equal")
                            
            case 4:
                  print("Exit")
