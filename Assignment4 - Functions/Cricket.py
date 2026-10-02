
'''Assignment 7: Cricket Run Rate

In cricket, overs are given in decimal format (e.g., 48.3 means 48 overs and 3 balls). Convert overs into total balls and calculate run rate.

Input:
Total runs = 275
Overs = 48.3

Expected Output:
Total Balls = 291
Run Rate = 5.67'''



runs = int(input("Enter the Total Runs:"))
overs  = float(input("Overs:"))

balls = (int(overs)*6)
a = (overs*10)%10
balls = int(balls + a)

runrate = (runs/balls)*6
print("Total Balls:",balls)
print("RunRate:",round(runrate,2))