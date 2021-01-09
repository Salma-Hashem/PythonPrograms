# Roll the Dice Salma Hashem 9/30/2019 
#write a program which  prompts the user for the number of sides to the pair of dice they will be rolling.
#Your user should be able to select from among 4-, 6-,7-, 8-,10-, 12-, 16- or 20-sided dice.
#You can assume that they will enter integers. You will need to validate their input before you continue.
#You should re-prompt the user to enter a value if they supply bad data.
#Keep rolling until it gets snake eyes 
#import random to generate random rolls
import random
# assign "counter" accumalator variables 
sides=int(input("How many sides on your dice? "))
tries=0
listtries=1
doubles=0
total1=0
total2=0
# while statement to check invalid inputs and trap them/ reprompt them to input good data
while sides!=4 and sides!=6 and sides!=7 and sides!=8 and sides!=10 and sides!=12 and sides!=16 and sides!=20:
    print("Sorry, that's not a valid size value. Try again!")
    sides=int(input("How many sides on your dice? "))
#while statment to check valid inputs depending on number of sides 
while sides==4 or sides==6 or sides==7 or sides==8 or sides==10 or sides==12 or sides==16 or sides==20:
    if sides==4:
        # assign randomly generated roll to each die 
        dice4=random.randint(1,4)
        dice4_2=random.randint(1,4)
        # print the output to user
        print(str(listtries)+". die number 1 is "+ str(dice4)+ " and die number 2 is "+ str(dice4_2) +".")
        tries+=1
        listtries+=1
        total1+=dice4
        total2+=dice4_2
        # check if dice are doubles
        if dice4==dice4_2:
            doubles+=1
            # if doubles check if snake eyes and if it is break program
            if dice4==1 and dice4_2==1:
                print("\nYou got snake eyes! Finally! on try number "+ str(tries)+"!")
                break
        
    elif sides==6:
        # assign random generated roll to each die 
        dice6=random.randint(1,6)
        dice6_2=random.randint(1,6)
        # print the output to user
        print(str(listtries)+". die number 1 is "+ str(dice6)+ " and die number 2 is "+ str(dice6_2) +".")
        tries+=1
        listtries+=1
        total1+=dice6
        total2+=dice6_2
        # check if dice are doubles
        if dice6==dice6_2:
            doubles+=1
             # if doubles check if snake eyes and if it is break program
            if dice6==1 and dice6_2==1:
                print("\nYou got snake eyes! Finally! on try number "+ str(tries) +"!")
                break
    elif sides==7:
        # assign randomly generated roll to each die 
        dice7=random.randint(1,7)
        dice7_2=random.randint(1,7)
        # print the output to user
        print(str(listtries)+". die number 1 is "+ str(dice7)+ " and die number 2 is "+ str(dice7_2) +".")
        tries+=1
        listtries+=1
        total1+=dice7
        total2+=dice7_2
        # check if dice are doubles
        if dice7==dice7_2:
            doubles+=1
            # if doubles check if snake eyes and if it is break program
            if dice7==1 and dice7_2==1:
                print("\nYou got snake eyes! Finally! on try number "+ str(tries) +"!")
                break

    elif sides==8:
        # assign randomly generated roll to each die 
        dice8=random.randint(1,8)
        dice8_2=random.randint(1,8)
        # print the output to user
        print(str(listtries)+". die number 1 is "+ str(dice8)+ " and die number 2 is "+ str(dice8_2) +".")
        tries+=1
        listtries+=1
        total1+=dice8
        total2+=dice8_2
        # check if dice are doubles
        if dice8==dice8_2:
            doubles+=1
            # if doubles check if snake eyes and if it is break program
            if dice8==1 and dice8_2==1:
                print("\nYou got snake eyes! Finally! on try number "+ str(tries) +"!")
                break
    elif sides==10:
        # assign randomly generated roll to each die 
        dice10=random.randint(1,10)
        dice10_2=random.randint(1,10)
        # print the output to user
        print(str(listtries)+". die number 1 is "+ str(dice10)+ " and die number 2 is "+ str(dice10_2) +".")
        tries+=1
        listtries+=1
        total1+=dice10
        total2+=dice10_2
        # check if dice are doubles
        if dice10==dice10_2:
            doubles+=1
            # if doubles check if snake eyes and if it is break program
            if dice10==1 and dice10_2==1:
                print("\nYou got snake eyes! Finally! on try number "+ str(tries) +"!")
                break
    elif sides==12:
        # assign randomly generated roll to each die 
        dice12=random.randint(1,12)
        dice12_2=random.randint(1,12)
        # print the output to user
        print(str(listtries)+". die number 1 is "+ str(dice12)+ " and die number 2 is "+ str(dice12_2) +".")
        tries+=1
        listtries+=1
        total1+=dice12
        total2+=dice12_2
        # check if dice are doubles
        if dice12==dice12_2:
            doubles+=1
            # if doubles check if snake eyes and if it is break program
            if dice12==1 and dice12_2==1:
                print("\nYou got snake eyes! Finally! on try number "+ str(tries) +"!")
                break
    elif sides==16:
        # assign randomly generated roll to each die 
        dice16=random.randint(1,16)
        dice16_2=random.randint(1,16)
        # print the output to user
        print(str(listtries)+". die number 1 is "+ str(dice16)+ " and die number 2 is "+ str(dice16_2) +".")
        tries+=1
        listtries+=1
        total1+=dice16
        total2+=dice16_2
        # check if dice are doubles
        if dice16==dice16_2:
            doubles+=1
            # if doubles check if snake eyes and if it is break program
            if dice16==1 and dice16_2==1:
                print("\nYou got snake eyes! Finally! on try number "+ str(tries) +"!")
                break
    elif sides==20:
        # assign randomly generated roll to each die 
        dice20=random.randint(1,20)
        dice20_2=random.randint(1,20)
        # print the output to user
        print(str(listtries)+". die number 1 is "+ str(dice20)+ " and die number 2 is "+ str(dice20_2) +".")
        tries+=1
        listtries+=1
        total1+=dice20
        total2+=dice20_2
        # check if dice are doubles
        if dice20==dice20_2:
            doubles+=1
            # if doubles check if snake eyes and if it is break program
            if dice20==1 and dice20_2==1:
                print("\nYou got snake eyes! Finally! on try number "+ str(tries) +"!")
                break
# Print number of doubles and average rolls of each die found through accumalator variables and format to 2 decimal places

print("Along the way you rolled doubles", doubles, "times")
print("The average roll for die #1 was", format((total1/tries),'.2f'))
print("The average roll for die #2 was", format((total2/tries),'.2f'))

    
