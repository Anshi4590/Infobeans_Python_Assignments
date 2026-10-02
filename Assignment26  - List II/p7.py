"""
Question 7: Factorial Expansion List

Problem:
    Replace every element with its factorial value and
    perform the required analysis.

Tasks:
    - Convert each element to factorial
    - Find sum
    - Find maximum
    - Count even factorial values

Input:
    A list of integers.

Output:
    Factorial list, Sum, Maximum, Even Count

Test Cases:
    Input :
        [3, 4, 5]
    Output:
        Factorials = [6, 24, 120]
        Sum = 150
        Max = 120
        Even Count = 3
"""

# Write your code below
arr = list(map(int, input("Enter numbers: ").split(" ")))
print(arr)
fact = []
count = 0

for i in arr:
    f = 1
    for j in range(1,i+1):
        f = f*j
    fact.append(f)
    if f%2==0:
       count+=1
       
print(f"Factorial   : {fact}")
print(f"Sum         : {sum(fact)}")
print(f"Max         : {max(fact)}")
print(f"Even count  : {count}")