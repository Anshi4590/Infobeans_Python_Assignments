'''
79. Divide a string into n equal parts. 
S = "abcdef", 
n = 3 "ab", "cd", "ef"

'''

s = input("Enter String : ")
n = int(input("Enter number:"))
size = len(s)//n

for i in range(0,len(s),size):

    m = s[i:i+size]
    print( m, end =",")