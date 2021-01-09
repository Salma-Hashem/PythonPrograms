# Pick up sticks Salma Hashem 9/30/19 
# write a program for two humans to play a simple game of "Pick Up Sticks"
#The game begins with a number of sticks on a table (between 10 and 100)
#Each player, in turn, takes between 1-3 sticks off the table.
#The player to take the last stick loses.

# ask user to input number of sticks on the table
sticks= int(input("How many sticks are on the table? (enter a number between 10 and 100): "))

# first check if data is invalid and reprompt them
while sticks<10 or sticks>100:
    print("Invalid number of sticks, try again.")
    sticks= int(input("How many sticks are on the table? (enter a number between 10 and 100): "))
    
# assign "counter" accumulator variables
# assign trials variable to be able to switch between player 1 and 2 
trials=1
# assign stick remains variable so it will update the number of sticks left 
sticksremain=sticks
while True:
    print("\nThere are", sticksremain,"sticks on the table")
    # check if its players one turn based on which trial it is-- player 1 is odd trials and player 2 is even trials 
    if trials%2==1:
        print("Turn: Player 1")
    elif trials%2==0:
        print("Turn: Player 2")
#asssign removed variable and convert to int
    removed=int(input("How many sticks do you want to remove from the table? (1, 2 or 3): "))
    # check if it is an invalid input
    if removed<1 or removed>3:
        print("Invalid number of sticks, try again.")
        # reprompt them if its invalid
        continue
    #check if # of sticks removed is greater than # of sticks remaining 
    elif removed> sticksremain:
        print("You can't take that many sticks off of the table. Try again.")
        continue
    # if # of sticks removed is less than those remaining then go through the following statements 
    elif removed<sticksremain:
        if removed==1 or removed==2 or removed==3:
            sticksremain-=removed
            trials+=1
        # check if game is over by checking if # of sticks removed = number of sticks remaining 
    elif removed==sticksremain:
       # check which player lost by checking if the last trial was odd for player 1 or even for player 2 
        if trials%2==1:
            print("Player 1 loses!")
        elif trials%2==0:
            print("Player 2 loses!")
        break
    
