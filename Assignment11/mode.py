'''
Lift Mode Operation – Advanced Smart Elevator System


A smart building elevator works in multiple intelligent modes based on the mode number entered by the control panel.  

The system must automatically execute floor movement instructions using loops.


Write a program:


- If mode = 1  

  Normal Up Mode activated.  

  Read current floor and destination floor.  

  Print all floors from current to destination in ascending order.


- Else if mode = 2  

  Down Mode activated.  

  Read current floor and destination floor.  

  Print all floors from current to destination in descending order.


- Else if mode = 3  

  Energy Saving Mode activated.  

  Read destination floor.  

  Lift starts from ground floor (0) and stops only on alternate floors till destination.


- Else  

  Emergency Mode activated.  

  Print "Emergency Alarm" 4 times using loop.


Input:

3

6


Output:

0 2 4 6



Input:

1

2

7


Output:

2 3 4 5 6 7



Input:

2

8

3


Output:

8 7 6 5 4 3



Input:

5


Output:

Emergency Alarm

Emergency Alarm

Emergency Alarm

Emergency Alarm'''







mode=int(input("enter the mode="))
current_floor,destination=map(int,input("Enter current floor and destination floor").split(","))
if mode==3:
    i=current_floor-3
    while i<=destination:
          print(i,end=" ")
          i=i+2
elif mode==2:
    i=current_floor
    while  i>=destination:
         print(i,end=" ")
         i=i-1
elif mode==1:
    i=current_floor
    while  i<=destination:
         print(i,end=" ")
         i=i+1         
else:
     i=1
     while i<=4:
          print("Emergency" )
          i=i+1