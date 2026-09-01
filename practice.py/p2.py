'''
2.   3.5 marks

A cricket academy wants to analyze player performance. Each player's information is stored as a tuple.

Tuple Format:

(player_id, player_name, runs_scored)

Requirements:

Read N player records from the user and store them as tuples in a list.
Display all player records.
Find and display the player who scored the highest runs.
Find and display the player who scored the lowest runs.
Calculate and display the total runs scored by all players.
Calculate and display the average runs scored.
Display players who scored more than 50 runs.

Test Case:

Input:

Enter number of players: 5

101 Virat 82
102 Rohit 45
103 Gill 120
104 Hardik 38
105 SKY 76

Expected Output:

All Players:
(101, 'Virat', 82)
(102, 'Rohit', 45)
(103, 'Gill', 120)
(104, 'Hardik', 38)
(105, 'SKY', 76)

Highest Scorer:
(103, 'Gill', 120)

Lowest Scorer:
(104, 'Hardik', 38)

Total Runs:
361

Average Runs:
72.2

Players Scoring More Than 50 Runs:
(101, 'Virat', 82)
(103, 'Gill', 120)
(105, 'SKY', 76)

'''

n = int(input("Enter total no. of entries : "))
l = []

for i in range(n):
        print(f"Enter player {i+1} Details ")
        id = int(input("Enter Id      :"))
        name = input("Enter Name     :")
        
        runs = int(input("Enter runs     :"))
        print()
        player =(id,name,runs)
        l.append(player)

print(l)

minscore = l[0][2]

for i in range(1,len(l)):
        if minscore<l[i][2]:
            minscore=l[i][2]

print(minscore)

maxscore = 0

for i in range(0,len(l)):
       if maxscore>l[i][2]:
          maxscore = l[i][2]

print(maxscore)
                