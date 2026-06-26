'''4. E-Learning Course Access System

An online learning platform grants access based on subscription type, course progress, and test score.

If subscription is premium, then check progress. If progress is at least 80, then check test score. If score is at least 70, unlock certificate; otherwise allow retry. If progress is less than 80, ask to complete course. If subscription is basic, then check progress. If progress is at least 50, allow limited access; otherwise lock content. If subscription is neither, deny access.

Input:
Subscription = premium
Progress = 85
Test Score = 65

Output:
Access Status = Retry Test'''

#solution


subs = input("Subsscription:")
progress = int(input("Progress"))
tscore = int(input("Test score:"))

if subs.lower() =="premium":
   if progress>=80:
        if tscore>=70:
           print("Access Status = unlock certificate")
        else:
           print("Access Status = Retry Test")
   else:
      print("Access Status = complete course")

elif subs.lower() == "basic":
   if progress>=50:
      print("Access Status = limited acess")
   else:
      print("Access Status = lock content")
else:
   print("Access Status = denyed acess")


     
