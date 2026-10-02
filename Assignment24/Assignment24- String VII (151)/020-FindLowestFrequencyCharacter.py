'''20. Find the lowest frequency character in a string.'''

n = input("Enter String : ").lower()
mincount = 9
minchar = ""

for i in range(0,len(n)):
    if n[i] not in minchar:      
        count = 0
        for j in range(0,len(n)):
            if n[i] == n[j]:
               count+=1

        if count<mincount:
            mincount = count
            minchar = n[i]+" "

        elif count == mincount:
            mincount = count
            minchar+= n[i]+" "
    else:
        continue

print(f"The lowest frequency character in a string is {minchar} with frequency of {mincount}")