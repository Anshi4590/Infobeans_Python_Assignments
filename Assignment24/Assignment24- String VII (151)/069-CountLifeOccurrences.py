'''69 Count how many times 'life' appears in a string. 
S = "life is life" '''

s = input("Enter String : ")

sub = "life"
count = 0

for i in range(0,len(s)-len(sub)+1):
    flag = 0 
    for j in range(len(sub)):
        if s[i+j]!= sub[j]:
                flag = 1
                break
    if flag == 0:      
       count+=1
print(count)