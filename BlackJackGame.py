# Black jack Salma Hashem 11/15/19

# Create lists for cards and list with corresponding values
cards  = ['10 of Hearts', '9 of Hearts', '8 of Hearts', '7 of Hearts', '6 of Hearts', '5 of Hearts', '4 of Hearts', '3 of Hearts', '2 of Hearts', 'Ace of Hearts', 'King of Hearts', 'Queen of Hearts', 'Jack of Hearts', '10 of Diamonds', '9 of Diamonds', '8 of Diamonds', '7 of Diamonds', '6 of Diamonds', '5 of Diamonds', '4 of Diamonds', '3 of Diamonds', '2 of Diamonds', 'Ace of Diamonds', 'King of Diamonds', 'Queen of Diamonds', 'Jack of Diamonds', '10 of Clubs', '9 of Clubs', '8 of Clubs', '7 of Clubs', '6 of Clubs', '5 of Clubs', '4 of Clubs', '3 of Clubs', '2 of Clubs', 'Ace of Clubs', 'King of Clubs', 'Queen of Clubs', 'Jack of Clubs', '10 of Spades', '9 of Spades', '8 of Spades', '7 of Spades', '6 of Spades', '5 of Spades', '4 of Spades', '3 of Spades', '2 of Spades', 'Ace of Spades', 'King of Spades', 'Queen of Spades', 'Jack of Spades']
values = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 10, 10]

# import random and set two lists to represent dealing two cards at random use indices for every time to find corresponding name and values
import random

deal1=[random.randint(0, len(cards)-1)]
deal2=[random.randint(0, len(cards)-1)]
hand=[cards[deal1[0]],cards[deal2[0]]]
worth=values[deal1[0]]+values[deal2[0]]

# report players hand and value
print("Player hand:",hand,"is worth", worth)
#Remove cards dealt from deck 
del cards[deal1[0]]
del cards[deal2[0]]
del values[deal1[0]]
del values[deal2[0]]
# ask user to input if they wannt hit or stand
h_s=input("(h)it or (s)tand? ")
#while loop for players turn
while h_s=="h":
    print("You drew", cards[deal1[0]])
    # add dealt card to list to print
    hand+=[cards[deal1[0]]]
    worth+=values[deal1[0]]
    #delete the dealt card
    del cards[deal1[0]]
    del values[deal1[0]]
    #print results
    print("Player hand:",hand,"is worth", worth)
    #randomize deal again
    deal1=[random.randint(0, len(cards)-1)]
    #check if worth is greater than 21
    if worth>21:
        print("Bust!\nComputer Wins!")
        break
    #check if total worth is 21 aka blackjack
    elif worth==21:
        print("Player got 21! Blackjack!\nPlayer wins!")
        break
    #if worth is less than 21, reprompt user if they want to hit or stand
    else:
        h_s=input("(h)it or (s)tand? ")
# if player wants to stand go to computer 
if h_s=="s":
    # create a new hand and worth list for computer so its not the same values as player
    hand2=[cards[deal1[0]],cards[deal2[0]]]
    worth2=values[deal1[0]]+values[deal2[0]]
    #print results
    print("\nComputer hand: ",hand2,"is worth", worth2)
    #while loop for computers turn--computer should continue to hit
    while h_s=="s":
        # deal a random card and print name using index
        print("Computer drew", cards[deal2[0]])
        #get rid of card dealt and its value from the lists 
        del cards[deal2[0]]
        del values[deal2[0]]
        # to randomly deal another card
        deal2=[random.randint(0, len(cards)-1)]
        # counter accumulator variables to track name of cards and their values 
        hand2+=[cards[deal2[0]]]
        worth2+=values[deal2[0]]
        print("\nComputer hand: ",hand2,"is worth", worth2)
        #if computer lost aka got more than 21 
        if worth2>21:
            print("Bust!\nPlayer Wins!")
            break
        #if computer won and got 21 aka blackjack
        elif worth2==21:
            print("Computer got 21! Blackjack!\nComputer wins!")
            break
        #if computer earns more points than player  
        elif worth2>worth:
            print("Computer wins!")
            break
        
        
