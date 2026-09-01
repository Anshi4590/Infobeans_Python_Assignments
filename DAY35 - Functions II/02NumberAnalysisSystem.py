"""2.
NUMBER ANALYSIS SYSTEM

Scenario:

A software company wants to develop a Number Analysis System. The application should be menu-driven and perform different mathematical operations on a given number.

MENU

1. Check Perfect Number
2. Check Prime Number
3. Find Reverse of a Number
4. Calculate Factorial
5. Display Factors of a Number
6. Exit

Requirements

Choice 1 – Check Perfect Number

* Accept a number from the user.
* Pass the number to a function.
* The function should return True if the number is Perfect, otherwise False.
* Display an appropriate message based on the returned value.

Choice 2 – Check Prime Number

* Accept a number from the user.
* Pass the number to a function.
* The function should return a message such as "Prime Number" or "Not a Prime Number".
* Display the returned message.

Choice 3 – Find Reverse of a Number

* Accept a number from the user.
* Pass the number to a function.
* The function should return the reversed number.
* Display the returned value.

Choice 4 – Calculate Factorial

* Accept a number from the user.
* Pass the number to a function.
* The function should return the factorial value.
* Display the returned value.

Choice 5 – Display Factors of a Number

* Accept a number from the user.
* Pass the number to a function.
* The function should return all factors of the given number.
* Display the returned factors.

Choice 6 – Exit

Sample Output

Enter Choice : 1

Enter Number : 28

28 is a Perfect Number

---

Enter Choice : 2

Enter Number : 17

Prime Number

---

Enter Choice : 3

Enter Number : 1234

Reverse Number : 4321

---

Enter Choice : 4

Enter Number : 5

Factorial : 120

---

Enter Choice : 5

Enter Number : 12

Factors : 1 2 3 4 6 12

---

Important Instructions

1. Create separate functions for each operation.
2. Use parameters to pass values to functions.
3. Use return statements appropriately.
4. Different functions should return different types of values such as Boolean, String, Integer, and Collection/List.
5. Avoid using global variables.
6. Implement the solution using a menu-driven approach.
7. Write meaningful function names and maintain proper code readability"""




def display():
    print("\n" + "*" * 35)
    print("      NUMBER ANALYSIS SYSTEM")
    print("*" * 35)

    print("""
1. Check Perfect Number
2. Check Prime Number
3. Find Reverse of a Number
4. Calculate Factorial
5. Display Factors of a Number
6. Exit
""")

def perfectnumber(n):

    
    sum = 0
    for i in range(1,n//2+1):
        if n%i ==0:
            sum+=i

    if sum == n:
       print(f"{n} is a Perfect Number")

    else:
       print(f"{n} is not a Perfect Number") 

def primenumber(n):

    if n<2:
       return "NOt Prime"
    
    else:

        i = 2
        while i<n:
              if n%i==0:
                return "NOt Prime"

        return "Prime"

def reverse(n):

    rev = 0
    while n>0:
       d = n%10
       rev = rev*10 + d
       n = n//10
       
    return rev

def factorial(n):
    
    fact = 1
    i = 1
    while i<=n:
          fact*=i
          i+=1

    return fact

def factors(n):
    result = ""

    for i in range(1,n+1):

        if n%i==0:
            result+=str(i)+" "

    return result

while True:

    display()

    choice = int(input("Enter Choice : "))

    match choice:

        case 1:
            n = int(input("Enter Number : "))
            perfectnumber(n)

        case 2:
            n = int(input("Enter Number : "))
            print(primenumber(n))

        case 3:
            n = int(input("Enter Number : "))
            print(reverse(n))

        case 4:
            n = int(input("Enter Number : "))
            print(factorial(n))

        case 5:
            n = int(input("Enter Number : "))
            print(factors(n))

        case 6:
            print("Exiting Number Analysis System...")
            break

        case _:
            print("Invalid Choice!")