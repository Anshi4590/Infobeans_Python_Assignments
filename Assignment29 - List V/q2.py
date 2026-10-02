'''2.
Secure Password Analysis

A cybersecurity team wants to identify pairs of passwords having no common characters.

Problem Statement:

Given N strings, count the number of pairs that do not share any common character.

Example:

Input

N = 4
passwords[] = {"abc", "de", "fg", "ad"}

Output

3

Explanation

("abc","de")
("abc","fg")
("de","fg")'''

n = int(input("Enter Size:"))
num =[]
for i in range(n):
    num.append(input("Enter number : "))
print(num)



new =[]
count=0
for i in num:
    for j in num:
        flag =0
        for k in i:
            if k in j:
                flag =1
                break
        if flag == 0:
            if i and j not in new:
               new.append(i)
               print(f"({i},{j})")
               count+=1
            else:
                continue
# print(new)
print(count)