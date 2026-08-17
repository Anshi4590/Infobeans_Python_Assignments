'''39 Search all occurrences of a character.
 S = "banana", 
 Char='a' 1, 3, 5 (indices)'''

n = input("Enter String :  ")
char = input("Enter char :")
if char in n:
    for i in range(len(n)):
        if n[i] == char:
            print(i,end=" ")
else:
    print("inValid character")
    