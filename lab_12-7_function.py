#1. Create a Python file named lab_12-7.py
#2. Create a second Python file named lab_12-7_functions.py
#. In the lab_12-7_functions.py file, create AT LEAST 10 different
#functions (you may copy from earlier assignments). Within the
#functions you write, you must account for the following:
#a. at least one function must use a dictionary (can be as the argument)
#b. you must use at least 3 different lists
#c. you must use a for loop, a while loop, and enumerate
#d. you must use at least 5 built in functions (like lower()).
##e. your functions all must return at the end.
#f. at least 5 of the functions must be over 15 (logical) lines of code in length)
#4. In the lab_12-7.py file, call (print) at least 4 of the functions. You
#may choose any method to do this.


#d. you must use at least 5 built in functions (like lower()).


#function 1 calkling maximum value in alist
def maximumidea():
    number1 = int(input("Enter A Number: "))
    number2 = int(input("Enter A Number: "))
    number3 = int(input("Enter A Number: "))
    number4 = int(input("Enter A Number: "))
    x = [number1, number2, number3, number4]


    key_max = max(x)


    print(key_max)


    if key_max == 0:
        print('Maximum is Zero')
    else:
        print('Maximum is', key_max)


print(maximumidea())




#function 2


def minimunset():
    number1 = int(input("Enter A Number: "))
    number2 = int(input("Enter A Number: "))
    number3 = int(input("Enter A Number: "))
    number4 = int(input("Enter A Number: "))
    x = [number1, number2, number3, number4]
        #create variable for list
    key_min = min(x)
        #create a variabke for the minimum value
    print(key_min)


        #conditional to detemrine if conditions are met
    if key_min == 47:
        print('Maximum is 47')
    else:
        print('Maximum is', key_min)


print(maximumidea())








def createupperstring():
    word1 = input("Please Enter word with the letter S: ")
    if word1[0] == 'S':        #conditional to detemrine if conditions are met


        word1 = word1.upper()
        return word1        #conditional to detemrine if conditions are met


    else:
        print("Please re-enter word starting with the letter S")          #conditional to detemrine if conditions are met


print(createupperstring())








def createlowerstring():
    word2 = input("Please Enter word with the letter r: ")
    if word2[0] == 'r':#conditional to detemrine if conditions are met
        word2 = word2.lower()#conditional to detemrine if conditions are met for lowercase word
        return word2#conditional to detemrine if conditions are met
    else:
        print("Please re-enter word starting with the letter r")#conditional to detemrine if conditions are met
print(createupperstring())


def multiplynumbers():
    product1 = input("Number: ") #variable to inoput a number two times
    product2 = input("Number: ")
    product = int(product1) * int(product2)


    numberedlist = [product1, product2, product]
    print(numberedlist)


    if product > 50:
        return product#conditional to detemrine if conditions are met
    else:
        print("Try Again")#conditional to detemrine if conditions are met
       
print(multiplynumbers())


def activation():
    #print dashed lines for orgnaization of seperation
    print("-------------------------------------------------------------------------------------------------------------------------")
   #List of choices like a typical event would have
   #A Game that could take place in real life or not = theme of the overall code
    print("Wel. Wel. Wel. Welcome. Analysis of ship operating at 37% efficiency")
    print("Caution, Many security systems are implemented. Enter at your own risk")
    print("Please select the number for purpose of arrival")
    print("Select 1 for Quiz")
    print("Select 2 for Football Game")
    print("Select 3 for Movie Audition")
    print("Select 4 for Chess Tournament")
    print("-------------------------------------------------------------------------------------------------------------------------")
 
    #input variable to input choice
    Procedure = int(input("Enter Selection: "))
 
        #while loop to account for all possible choices
    while(Procedure != 4):
        if (Procedure == 1):
            print("If here for Quiz, Please Proceed and Enter the Code.")
            break
               #variable pertaining to input of question
               #if else statements for conditions of questions
            #if answers meets the reuqirments for answers of the questions
        elif (Procedure == 2): #another if stament just in case the original choice is not inputed
            print("If here for Football Game, Please Exit the Area and head to Raferty Stadium")
            print("If here for Quiz, Please Proceed and Enter the Code.")
            break
           
        elif (Procedure == 3):
            print("If here for Movie Audition, Please Exit the Area and head to JFK Airport to take the flight to Warner Bros for the new Batman movie Audition")
            print("If here for Quiz, Please Proceed and Enter the Code.")
            break
           
        elif (Procedure == 4):
            print("If here for Chess Tournament, Please Exit the Area and head to the Student Life Center for furthur instructions")
            print("If here for Quiz, Please Proceed and Enter the Code.")
            break


        else:
            print("Needs Updating. Till Next time")
            break


#close full function
activation()


#function 3


def forlist():
    eng_sp = {'one':'uno', 'two':'dos', 'three':'tres'}
    keys = eng_sp.values()
    print(keys)
    for (k,v) in eng_sp.items():
        print("Got key", k, "that maps to", v)


    grades = {'Mid Year Project Presention': 93,
          'Mid Year Project Proposal': 100,
          'Mid Year Project Code': 97,
          'Mid Year Project Reflection': 93}


    print(grades)


    print(grades.values())


    for (k,v) in grades.items():
        print("Assignment: ", k, "Grade: ", v)
print(forlist())






def multiplesofthree():




    #list is equal to parenthesses
    List = []




    while True:
        #ask user to input a multiple of three
        inputednumber = int(input("Hello. Please Enter a Number that is only a multiple of three: "))
        #if inputed value is a multiple of three
        if inputednumber%3:
            print(List) #print(list)
            break
        #if user enters -1
        #official list
        elif inputednumber == -1:
            print(List)
            break #break the statement once done
        #append each value of a multiple of three to the list aside from -1
        else:
            List.append(inputednumber)




#close function
multiplesofthree()


def indexed_names(ListOfNames):
#function called indexed_names.
#The function should take a list of names as its only parameter.
    numberedlist = []
    # for index in range enumerate the new list of names
    for i, v in enumerate(ListOfNames):
        #append the list with a number with the name
        numberedlist.append(f'{i}: {v}')
    #print a new list
    print(numberedlist)




        # list is passed as an argument to the function,




print(indexed_names(['Batman Begins (2005)', 'The Dark Knight (2008)', "The Dark Knight Rises (2012)"]))
# function should return a new list where each value is replaced by the index,
#followed by a color, space, and the original value
print(indexed_names(['Man of Steel (2013)', 'Batman vs Superman: Dawn of Justice (2016)', "Zack Synder's Justice League (2021)"]))
print(indexed_names(['Lord of the Rings: Fellowship of the Ring (2001)', 'Lord of the Rings: The Two Towers (2002)', "Lord of the Rings: Return of the King (2003)"]))


def find_sum(num1, num2):
#4. Add statements to the function that adds the arguments passed to num1 and num2 and
#stores them in a new variable num_sum
    num_sum = num1 + num2
    return num_sum #Finish the function with a statement that returns num_sum


#6. Create a statement that calls the function to find the sum of 111 and 222. Set it
#equal to the variable my_sum
my_sum = find_sum(111, 222)
#7. Add another print statement after the previous statement that prints my_sum
print(my_sum)


#8. What happens when you run the program?


print("After I run the program, the value of 333 is printed")