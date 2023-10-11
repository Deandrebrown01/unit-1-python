"""
Exercise 1:
Write a Python program that prints the current date and time using the datetime module.
"""
import datetime
x=datetime.datetime.now()
print (x)

"""
Exercise 2:
Write a Python program that prints the current date and time using the datetime module.
Using the strftime function format the date in standard U.S. date format (MM/DD/YYYY)
"""
from datetime import datetime
now=datetime.now()
formatted=now.strftime("%m/%d/%-y")
print(formatted)


"""
Exercise 3:
Using the strptime function, convert two strings into dates.
Then find the difference in days between the two.
"""
from datetime import datetime
date_string="12/08/2023"
year_string="06/22/2024"


date_object=datetime.strptime(date_string,"%m/%d/%Y")
year_object=datetime.strptime(year_string,"%m/%d/%Y")

print(date_object)
print(year_object)

"""
Excercise 4:
Write a program that asks the user for their birthdate and calculates their current 
age using the datetime module.
"""
from datetime import datetime
bday=input("What is your birthday")

