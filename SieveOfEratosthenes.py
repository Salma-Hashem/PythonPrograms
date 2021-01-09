# Lists  Salma Hashem  11/13/19
# Write a program that uses the Sieve of Eratosthenes: Finding All Prime Numbers up to 1000

#Create a list of 1,000 values  all of which are set to zero
primes=[0]*1000
#set frist two values to 1 
primes[0]=1
primes[1]=1
# counter varible to format numbers 10 per row 
counter=0
#2 for loops to check if i is a multiple of j 
for i in range(999):
    for j in range(999):
        #check only number set to zero/ primes and make sure j is less than i becuase of multiples
        if primes[j]==0 and j<i:
            # if they are multiples then i is not prime so set i to 1
            if i%j == 0:
                primes[i]=1
                #increase counter by 1
    
# for loop to print the prime numbers up to 1000 after checking them and format to 10 numbers every row 
for i in range(999):
    if primes[i]==0:
        #format to make sure the place values are neatly aligned and add end to print a space between numbers
        print(format(i,'>8'),end='')
        counter+=1
        #once counter reaches a multiple of 10 it will print a line
        if counter%10==0:
            print()
