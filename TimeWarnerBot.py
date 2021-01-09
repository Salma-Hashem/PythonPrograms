# "Time Warner Python" Salma Hashem netid: sh5640
#Design costumer service application by asking users series of questions, and based on the customers' answers to the questions, provide them with instructions. 
#Ask the user to choose from the following options 
print("Choose from the following options: ")
#assign each menu option to a number
one= " 1. My internet is not working."
two= "2. My cable is not working."
three= "3. My phones are not working."
four= "4. My bill is wrong."
five= "5. I want to upgrade my plan."
#Print the options each on its own line and ask the user to input a number and convert into an integer
print(one, "\n", two, "\n", three, "\n", four, "\n", five)
value= int(input("(Enter a value 1 - 5): "))
#assign variables to user inputs using if else statements for scenario one and print output based on user inputs 


if value==1:
    modem_on=input("\nIs your modem on? (Enter Y or N): ")
    if modem_on=="Y":
        router_on=input("\nIs your router on? (Enter Y or N): ")
        if router_on=="Y":
            redlight= input("\nDoes your router emit a red light? (Enter Y or N): ")
            if redlight=="Y":
                print("Unplug your router and wait thirty seconds. Then plug your router into the nearest outlet to restart your router. If you still cannot connect to the internet, restart this program. Note, this program will now terminate. Goodbye!")
            else:
                comp_wifi_on=input("\nAre both your computer and wifi on? (Enter Y or N): ")
                if comp_wifi_on=="Y":
                    print("It looks like you may need additional support. Please call 555-555-5555 for additional support with this matter. Thank you for your patience.")
                else:
                    print("If your computer is not on, please turn it on by pressing the power button. Also make sure your computer's wifi is on. If you still cannot connect to the internet, restart this program. Note, this program will now terminate. Goodbye!")
        else:
            print("Plug your router into the nearest outlet to turn on your router. If you still cannot connect to the Internet, restart this program. Note, this program will now terminate. Goodbye!")
            
    else:
        print("Plug your modem into the nearest outlet to turn on your modem. If you still cannot connect to the Internet, restart this program. Note, this program will now terminate. Goodbye!")
#assign variables to user inputs using if statements for scenario two and print output based on user inputs     
if value==2:
    cable_on=input("\nIs your cable box on? (Enter Y or N): ")
    if cable_on=="Y":
        tv_on=input("\nIs your TV on? (Enter Y or N): ")
        if tv_on=="Y":
            print("It looks like you may need additional support. Please call 555-555-5555 for additional support with this matter. Thank you for your patience.")
        else:
            print("Plug your TV into the nearest outlet and press the power button on your remote to turn on your TV. If you still do not recieve a cable signal, restart this program. Note, this program will now terminate. Goodbye!")
    else:
        print("Plug your cable box into the nearest outlet to turn on your cable box. If you still do not recieve a cable signal, please restart this program. Note, this program will now terminate. Goodbye!")
#assign variables to user inputs using if statements for scenario three and print output based on user inputs 
if value==3:
    phones_on=input("\nAre your phones on? (Enter Y or N): ")
    if phone_on=="Y":
        landline_plugged=input("\nIs there a landline wire plugged into each phone or the wireless phone terminal? (Enter Y or N): ")
        if landline_plugged=="Y":
            print("It looks like you may need additional support. Please call 555-555-5555 for additional support with this matter. Thank you for your patience.")
        else:
            print("Plug a landline wire into each phone or phone terminal. If you still cannot use your phones, please restart this program. Note, this program will now terminate. Goodbye!")
    else:
        print("Plug your phones into the nearest outlet to turn them on. If you are using wireless phones, please make sure you change them before attempting to use them. If you still cannot use your phones, please restart this program. Note, this program will now terminate. Goodbye!")
#assign variables to user inputs using if statements for scenario four and print output based on user inputs
if value==4:
    late_payment= input("\nWere you late on your last payment? (Enter Y or N): ")
    if late_payment=="Y":
        print("If you were late on your last payment, you will be charged an additional 5% interest fee. Therefore, your bill may be more than usual. If you would like to contest your charge, please call 555-555-5555 for additional support with this matter. Thank you for your patience. Note, this program will now terminate. Goodbye!")
    else:
        print("It looks like you may need additional support. Please call 555-555-5555 for additional support with this matter. Thank you for your patience.")
#scenario 5--evaluate input and print output based on user input
if value==5:
    print("It looks like you may need additional support. Please call 555-555-5555 for additional support with this matter. Thank you for your patience.")
#create if statements to evaluate invalid user inputs
if value<1 or value>5:
    print("You entered an invalid menu choice. It looks like you may need additional support. Please call 555-555-5555 for additional support with this matter. Thank you for your patience.")
        
