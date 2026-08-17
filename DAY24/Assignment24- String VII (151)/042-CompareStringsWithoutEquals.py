'''42.Check if two strings are equal without using equals().
 S1 = "abc", S2 = "abc"
 output - TRUE'''


s1 = input("Enter String : ")
s2 = input("Enter String : ")
flag = 0
if len(s1)==len(s2):
    for i in range(len(s1)):
        if s1[i]!=s2[i]:
             flag = 1
             print("False")
             break
    if flag == 0:
        print("True")       

else :
   print("False")