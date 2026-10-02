'''32 Count the frequency of each word.
 S = "apple banana apple" 
 apple: 2, banana: 1'''

n = input("Enter string:")
m = n.split(" ")
count = 0
result = []

for i in m:
    if i not in result:
       count = 0
       result.append(i)
       for j in m:
            if i == j:
               count+=1
       print(f"{i}: {count}") 