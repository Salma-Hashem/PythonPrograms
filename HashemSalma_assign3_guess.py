# Assignment 3 part 2 "Guess the Number Game" Salma Hashem netid:sh5640 cs002 M/Th 12:30-1:45
#Write a program that lets the user guess an integer between 1 and 10. The integer should be randomly selected by your program when it starts up.
#Your player is allowed to guess three times - if they guess correctly, they win and the program ends.
#If they guess incorrectly they should be told if the number they guessed was too high or too low and then be asked to guess another time.
#At the end of the program you shoud display the secret number as well as how many attempts it took to guess that number.

#Import random module and assign a variable for a number that will be guessed
import random

num= random.randint(1,10)
#print to the user the range of the number that needs to be guessed 
print("I'm thinking of a number between 1 and 10!")
# prompt user to input guess
guess= int(input("What's your guess? "))
#evaluate if the answer is correct, too low, or too high with an if statement
if guess<num:
    #1st try
    print("Too low, try again.")

    #ask 2nd time
    guess2= int(input("What's your guess? "))
    if guess2<num:
        print("Too low, try again.")

        #ask 3rd time
        guess3= int(input("What's your guess? "))
        if guess3 != num:
            print("The secret number was "+str(num)+".")
            print ("You didn't guess the number.")
        else:
            print("You got it! \nThe secret number was "+str(num)+"."+"\nIt took you 3 tries to guess the number.")
        
    elif guess2>num:
        print("Too high, try again.")
         #ask 3rd time
        guess3= int(input("What's your guess? "))
        if guess3 != num:
            print("The secret number was"+str(num)+".")
            print ("You didn't guess the number.")
        else:
            print("You got it! \nThe secret number was "+str(num)+"."+"\nIt took you 3 tries to guess the number.")
    else:
        print("You got it! \nThe secret number was "+str(num)+"."+"\nIt took you 2 tries to guess the number.")
    
    
elif guess> num:
    print("Too high, try again.")
    #ask 2nd time
    guess2= int(input("What's your guess? "))
    if guess2<num:
        print("Too low, try again.")

        #ask 3rd time
        guess3= int(input("What's your guess? "))
        if guess3 != num:
            print("The secret number was secret was "+str(num)+".")
            print ("You didn't guess the number.")
        else:
            print("You got it! \nThe secret number was "+str(num)+"."+"\nIt took you 3 tries to guess the number.")
        
    elif guess2>num:
        print("Too high, try again.")
         #ask 3rd time
        guess3= int(input("What's your guess? "))
        if guess3 != num:
            print("The secret number was"+str(num)+".")
            print ("You didn't guess the number.")
        else:
            print("You got it! \nThe secret number was "+str(num)+"."+"\nIt took you 3 tries to guess the number.")
    else:
        print("You got it! \nThe secret number was "+str(num)+"."+"\nIt took you 2 tries to guess the number.")


        
