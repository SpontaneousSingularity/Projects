import random

def roll():
    minValue=1
    maxValue=6
    roll= random.randint(minValue,maxValue)
    return roll

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


maxScore=input("maximums score: ")

        
