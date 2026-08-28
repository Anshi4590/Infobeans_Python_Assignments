'''
45 Check whether a string starts/ends with another string. 
S = "apple pie", 

Prefix = "apple",

Suffix = "pie"
 
Start: True, End: True

'''

n = input("Enter String : ")
preffix = input("Enter preffix : ")
suffix =  input("Enter Suffix : ")

for i in range(0,len(preffix)):
    flag =0

    for j in range(len(preffix)):
        if n[i+j]==preffix[j]:
            flag = 1
            
if flag == 1:
    print("Start = True")

else:
    print("Start = False")

for k in range(len(n)-len(suffix), len(n)):
    m = 0

    for l in range(len(suffix)):
        if n[k+l]!=suffix[l]:
            m = 1
            break
if m == 0:
    print("End = True")
else:
    print("End = False")