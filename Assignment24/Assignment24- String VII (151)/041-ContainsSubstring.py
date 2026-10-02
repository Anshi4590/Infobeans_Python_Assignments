'''41.Check if a string contains a substring (without using built-in method).
 S1 = "Hello", Sub="ell" 
 TRUE'''

n = input("Enter String : ")
s1 = input("Enter Substring : ")

if s1 in n:
    print("true")
else:
    print("False")


# using another way
for i in range(len(n)-len(s1)+1):
    flag = 0
    for j in range(len(s1)):
        if n[i+j]==s1[j]:
            flag = 1
    break
if flag ==1:
   print("True")
else:
    print("false")