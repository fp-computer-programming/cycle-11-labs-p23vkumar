#1. Create a Python file named lab_11-2.py
#2. Create a dictionary named grades, that contains keys for each assignment
#this quarter and the grade you received on it as the key. Make sure the
#grades are out of 100.
#3. Using a one-line statement, print a list of just all the grades you received.
#4. Using a loop, print the name of each assignment in the dictionary on a
#separate line.
#5. Using another loop, print the name and grade you received on each
#assignment that you scored an 70 or above on.
##6. Using another loop, print the name and grade you received on each
#assignment that you scored an 50 or below on.


#create new function called MidYearGrades to call function
def MidYearGrades():


    print("-----------------------------------------------------")


    #Dictionary named grades, that contains keys for each assignment
    #this quarter and the grade you received on it as the key. Make sure the
    #grades are out of 100.
    grades = {'Mid Year Project Presention': 93,
          'Mid Year Project Proposal': 100,
          'Mid Year Project Code': 97,
          'Mid Year Project Reflection': 93}


    print(grades) #one-line statement, print a list of just all the grades you received.


    print("-----------------------------------------------------")


        #loop, print the name of each assignment in the dictionary on a
                        #separate line.
    for (k,v) in grades.items():
        print("Assignment:", k, ",Grade: ", v)


    print("-----------------------------------------------------")


    #loop, print the name and grade you received on each
#assignment that you scored an 70 or above on.
    print("Grades for 70 and above")
    for (k,v) in grades.items():
        if v >= 70:  #if values are 70 or above, then print grade, otherwise print nothing
            print(v)
    else:
        print("Nothing")
   
    print("-----------------------------------------------------")


   # Using another loop, print the name and grade you received on each
#assignment that you scored an 50 or below on.
    print("Grades for 50 and below")
    for (k,v) in grades.items():
        if v <= 50: #if values are 50 or below, then print grade, otherwise print nothing
            print(v)
        else:
            print("Nothing")


MidYearGrades() #close the function in order to close the overall function