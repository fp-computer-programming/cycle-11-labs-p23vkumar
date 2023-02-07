#1. Create a Python file named lab_11-4.py
#2. Create a variable, weekdays and set it equal to a tuple that
#contains the days Monday – Friday as strings.
#3. Create a variable weekends and set it equal to a tuple that contains
#Saturday and Sunday as strings.
##4. Create a variable called days_of_the_week and set it equal to the
#concatenation of the two previous variables.
#5. Printing days_of_the_week should display a tuple containing all
#the days of the week in order.




#•A tuple is a compound data type
#• Tuples are immutable lists
#•Used when data will not be changed
#2.  variable, weekdays and set it equal to a tuple that
#contains the days Monday – Friday as strings.
weekdays = ('Monday', 'Tuesday,', 'Wednesday', 'Thursday', 'Friday')


#variable weekends and set it equal to a tuple that contains
#Saturday and Sunday as strings.
weekends = ('Saturday', 'Sunday')


#variable called days_of_the_week and set it equal to the
#concatenation of the two previous variables.
days_of_the_week = weekdays + weekends
##5. Printing days_of_the_week should display a tuple containing all
#the days of the week in order.
print(days_of_the_week)
