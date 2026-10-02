'''19. Find the highest frequency character in a string.'''
n = input("Enter String : ").lower()
maxcount = 0
maxchar = ""

for i in range(0,len(n)):
    if n[i] not in maxchar:      
        count = 0
        for j in range(0,len(n)):
            if n[i] == n[j]:
               count+=1

        if count>maxcount:
            maxcount = count
            maxchar = n[i]+" "

        elif count == maxcount:
            maxcount = count
            maxchar+= n[i]+" "
    else:
        continue

print(f"the highest frequency character in a string is {maxchar} with frequency of {maxcount}") 