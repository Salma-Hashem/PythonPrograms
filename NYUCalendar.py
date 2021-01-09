#"NYU Calendar" Salma Hashem 
#write a program that will be able to tell a user whether s/he has the day off for any given day during
#the current semester (Fall 2019).
#ask user to input a month and a day and covert to an integer assume all dates entered are for year 2019
month=int(input("Enter a month (1-12): "))
day= int(input("Enter a day(1-31): "))

#assign each inputted month as a variable within if statements so that the numeric months in integer form
#is converted to thier english equivalents
if month==1:
    print_month="January"
if month==2:
    print_month="February"
if month==3:
    print_month="March"
if month==4:
    print_month="April"
if month==5:
    print_month="May"
if month==6:
    print_month="June"
if month==7:
    print_month="July"
if month==8:
    print_month="August"
if month==9:
    print_month="September"
if month==10:
    print_month="October"
if month==11:
    print_month="November"
if month==12:
    print_month="December"
# first evaluate months and days that are outside of the dates under consideration then print input is not valid
#(only evaluate the months with 31 days)
if month<1 or month>12:
    print("That's not a valid date!")
else:
    if month== 1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
        if day<1 or day>31:
            print("That's not a valid date!")
        #Next evaluate if inputs are a holidays using if elif, and else statements
        #The program will tell the user if school is not in session and tell the user why.
        else:
            if month==10 and day==14:
                print(print_month, day, "is Fall Recess. This is a school holiday at NYU.")
            elif month==12 and day==20:
                print(print_month, day,"is the last day of the Fall 2019 term.")
            #evaluate if the inputs are before or after the Fall 2019 term and print to user
            elif month==12 and day>20:
                print(print_month, day,"is after the end of the Fall 2019 term.")
            elif month== 1 or month==3 or month==5 or month==7 or month==8:
                if day>=1 or day<=31:
                    print(print_month, day,"is before the start of the Fall 2019 term.")
            #evaluate if input is during Fall 2019 term and print to user
            elif month==10 or month==12:
                if day>=1 or day<=31:
                    print(print_month,day, "is not a holiday at NYU. NYU is open on this day.")
    #Evaluate the month feburary with 28 days and print to the user if day is before the term or invalid
    elif month==2:
        if day<1 or day>28:
            print("That's not a valid date!")
        elif month==2:
            if day>=1 or day<=28:
                print(print_month, day, "is before the start of the Fall 2019 term.")
    #evaluate the inputted months with 30 days (no need to include months--this shortens code)
    #if day is outside of the dates under consideration then print input is invalid
    else:
        if day<1 or day>30:
            print("That's not a valid date!")
        #evaluate the inputted months for holidays 
        else:
            if month==11 and day>=27 and day<=29:
                print(print_month, day,"is during Thanksgiving break. NYU is not open on this day.")
            elif month==9 and day==3:
                print(print_month, day,"is the first day of the Fall 2019 term.")
            #evaluate if the inputs are before or during the Fall 2019 term and print to user
            elif month==9 and day<3:
                print(print_month, day, "is before the start of the Fall 2019 term.")
            elif month==4 or month==6:
                if day>=1 or day<=30:
                    print(print_month, day,"is before the start of the Fall 2019 term.")
            elif month==9 or month==11:
                if day>=1 or day<=30:
                    print(print_month,day, "is not a holiday at NYU. NYU is open on this day.")
            

