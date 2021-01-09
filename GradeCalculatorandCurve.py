#Assignment #9 : Working with Files and Data Salma Hashem netid :sh5640 cs002-008 

#write a program that lets the user type in the name of a file


#try block for user to input class file to grade
try:
    file=input("Enter a class file to grade (i.e. class1 for class1.txt): ")
    # open a file for reading
    openfile= open(file+".txt", "r")

# if there was an error in the try block above then we can respond to it using the except block below
except:
    print("File cannot be found.")
# if the try block succeeded, we can do this
else:
    print("Successfully opened",file+".txt")
    
#part 2

#program should open up the file specified by the user and read in the data
#compute The total # of students represented in the file

print("\nGrade Summary: ")

# read in all data as one long string
alldata = openfile.read()

# output total students by counting number of N's because there is only one N in every line representing each student
numstudents=alldata.count("N")
print ("Total Students:",numstudents)

#list storing correct answers
correctanswers=['B','A','D','D','C','B','D','A','C','C','D','B','A','B','A','C','B','D','A','C','A','A','B','D','D']
#split data by line break
data_split=alldata.split("\n")


#counter accumulator variable to calculate individual score
score = 0
#use a list to store indivdual student scores
scores = []
# for loop to split using commas 
for student in data_split:
    if student!='':
        splitdata = student.split(",")
        
        #loop through answers to check if correct or not
        for answer in range(1,len(splitdata)):
            #if answer is correct
            if splitdata[answer]==correctanswers[answer-1]:
                score+=4
            #elif answer left empty
            elif splitdata[answer]=='':
                score+=0
            #else answer is incorrect
            else: 
                score-=1

        #add each individual score to list of scores
        scores.append(score)
        #reset score for each student
        score=0
print(scores)
sortedscores=scores
print(sortedscores)
#print results using max, min and sum functions 
print("Highest score:", max(scores))
print("Lowest score:", min(scores))
mean=sum(scores)/numstudents
print("Mean score:", format(mean,'.2f'))

#PART3
#have your program compute the following based on each data file
#The median value (Sort the grades in ascending order) assign len of scores to variable length 
length=len(scores)
#assign new variable sorted so it wont affect part4 when writing to file
sortedscores=sorted(sortedscores)
print(sortedscores)
print(scores)
#if the # of students is odd you can take the middle of all the grades
if length % 2 == 0: 
    median1 = sortedscores[length//2] 
    median2 = sortedscores[length//2 - 1] 
    median = (median1 + median2)/2
#If the # of students is even you can compute the mean by averaging the middle two values
else: 
    median = sortedscores[length//2]
#print median
print("Median score:", median)


#define a function to find mode
#input list which is list of scores
def mode(List): 
    counter = 0
    num = sortedscores[0] 
    #loop through every number
    for i in sortedscores:
        #frequency of number 
        freq = sortedscores.count(i)
        # if the frequency is greater than current frequency then that number is the most frequent number
        if(freq> counter):
            #make counter =current greatest frequency
            counter = freq
            #create variable to which number is most frequent
            num = i 
    #return the most frequent number
    return num

#print Mode and range 
print("Mode: ", mode(sortedscores))
print("Range:", max(sortedscores)-min(sortedscores))
#close file 
openfile.close()

#part5
# add option to curve
curve=input("Would you like to curve the exam? 'y' or 'n': ")
if curve=='y':
    #ask user to input new desired mean 
    newmean=float(input("Enter a desired mean (i.e. 75.0 to raise the mean score to 75.0): "))
    #check invalid input-only accept positive values 
    while newmean<0:
        print("Invalid curve, try again.")
        print()
        #reprompt user
        newmean=float(input("Enter a desired mean (i.e. 75.0 to raise the mean score to 75.0): "))
        continue
    #calculate number of points to add to each score 
    difference=newmean-mean
    #PART4
    # create a file object that opens the file "myfile.txt"
    # for write access ("w")
    writefile= open(file+"_grades.txt", "w+")


    # for loop to split using commas
    #counter variable for index
    answer = 0
    for student in data_split:
        if student!='':
            splitdata = student.split(",")
            #write N number 
            writefile.write(splitdata[0])
            #write comma
            writefile.write(',')
            #write individual scores truncated to 2 decimal points
            writefile.write(format(scores[answer],'.2f'))
            #write comma
            writefile.write(',')
            #write new scores after curve 
            newscore=scores[answer]+difference
            writefile.write(format(newscore,'.2f'))
            writefile.write('\n')
            #increase index by one 
            answer += 1
    # close file 
    writefile.close()
    print("Done! Check your grade file!")

else:
    #PART4
    # create a file object that opens the file "myfile.txt"
    # for write access ("w")
    writefile= open(file+"_grades.txt", "w+")


    # for loop to split using commas
    #counter variable for index
    answer = 0
    for student in data_split:
        if student!='':
            splitdata = student.split(",")
            #write N number 
            writefile.write(splitdata[0])
            #write comma
            writefile.write(',')
            #write individual scores truncated to 2 decimal points
            writefile.write(format(scores[answer],'.2f'))
            writefile.write('\n')
            #increase index by one 
            answer += 1
    # close file 
    writefile.close()






     

