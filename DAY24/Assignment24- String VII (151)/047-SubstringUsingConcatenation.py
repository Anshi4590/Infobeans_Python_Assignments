'''47 Check for substring using concatenation trick.
 S1="CDAB", 
 S2="ABCD" 
 True (S1 is in S2+S2)'''

name = input("Enter String : ")
sub = input("Enter substring : ")

m = name + name
flag = 1

for i in range(len(m)):
    current = m[i]

    for j in range(i + 1, len(m)):
        current += m[j]

        if current == sub:
            print("true")
            flag = 0
            break

    if flag == 0:
        break

if flag == 1:
    print("not found")

    