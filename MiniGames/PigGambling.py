import random

#produce random no for roll
def roll():
    minValue=1
    maxValue=6
    roll= random.randint(minValue,maxValue)
    return roll


#Take number of players
while True :
    players=input("Enter the no of Players(2-4): ")
    if players.isdigit():
        players=int(players)
        if 2<= players <=4:
            break
        else:
            print("!!! Enter number between 2 and 4 !!!")
    else:
        print("!!! Enter a number !!!")


#Get player names
names = [0 for _ in range(players)]  # Initialize a list with a placeholder value
i = 0
while i < players:
    names[i] = input(f"Player {i + 1}, enter your name: ")
    i += 1

print("Player Names:", names)

#set max score
while True :
    maxScore=input("Enter Target Score: ")
    if maxScore.isdigit():
        maxScore=int(maxScore)
        break
    else:
        print("!!! Enter a number !!!")



playerScores = [0 for _ in range(players)]


# main  implementation
while max(playerScores) < maxScore:
    
   
    for playerindex in range(players):
        print("\n\nplayer",playerindex+1,names[playerindex],"your turn has started\n")
        
        currentScore= 0

        while True:
            ShouldRoll= input("would you like to roll (y)? : ")
            if ShouldRoll.lower() != "y":
                break
            
            value=roll()
            if value == 1:
                print("you rolled 1 you are done!")
                currentScore = 0
                break
            else:
                print("You rolled:",value)
                currentScore+= value
            
            print("your score is:",currentScore)

        playerScores[playerindex]+= currentScore
        if playerScores[playerindex] > maxScore:
            print("\n!!! yay you won the game",names[playerindex],"!!!")
       
        print("\nyour total score is:",playerScores[playerindex])


        
