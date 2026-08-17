'''
2.
Find the Most Frequently Occurring Word
News Channel Keyword Analyzer

A news agency analyzes breaking news headlines to identify the most repeated keyword in a report.

Write a Python program to find the word with the highest frequency.

Input:
india won the match and india created history
Output:
india

'''
n = input("Enter String : ")
words = n.split()
maxcount=0
fc=""
for i in range(0,len(words)):
      count=0 
      for j in range(0,len(words)):
         if words[i]==words[j]:  
           count+=1
      if count > maxcount:
         maxcount = count
         fc = words[i]
                  
print(maxcount,fc)