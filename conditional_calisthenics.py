'''
Exercise 1:
Check if an integer is even and greater than 10.
Return True if both conditions are met, False otherwise.
'''
conditions=input("Give me a number")

if conditions % 2 == 0 and conditions>10:
    print("True")
else:
    print('False')
# I made two variables and did a math problem and then used an else statement if the condiitions arent met
'''
Exercise 2:
Determine the ticket price based on age and student status.
Price is $10 if under 18 or a student, $20 otherwise.
'''
Age=input("Give me your age")
Student=input("Are you a student?")

if Age<18 or Student=='yes' :
    print('You are a student, pay $10')
elif Age>18 or Student=='no':
    print('You are not a student, pay $20')

#I made two variables and did some problems


'''
Exercise 3:
Prompt the user to enter a fruit name. Check if the fruit is in the list. 
If it is, print "Yes, that fruit is in the list." 
If it's not, print "No, that fruit is not in the list."
'''
Fruits=['Apple','Banana','Kiwi','Dragonfruit']
choice=input("Give me a fruit")

if choice in Fruits:
    print('Yes this fruit is in the list')
else:
    print('No that fruit is not in the list')

# I made a list and then a choice variable and then I made if the users choice is in fruit it says yes if its not it says no


'''
Exercise 4:
Check if a year is a century year and a leap year.
'''
year=input("Give me a year")

if year % 4:
    print("It's a leap year")

#I made a year variable and then if its a leap year its every 4 years so i put the year % 4 and i put print its a leap year


'''
Exercise 5:
Calculate the cost of shipping for an online order based on the order weight and destination zone. 
The shipping cost is $5 per kilogram for Zone A and $7 per kilogram for Zone B. 
If the order weight is less than 0 kg, return an error message.
'''
weight=input("give me your order weight")
zone=input("What zone are you in?")


if weight>0:
    if zone=="A":
        print(weight*5)
    else:
        print(weight*7)
    
# I made two variables one named weight and one named zone and then I made iit for the weight if its greater than 0 and if its zone A i put the weight*5 and then I did the same thing for zone B
    
'''
Exercise 6:
Determine the type of a triangle based on side lengths.
Equilateral, Isosceles, Scalene, or Not a triangle.
'''
side1=input("What is the side length")
side2=input("What is your other side length")
side3=input("What is your last side length")

if side1==side2 and side2==side3 and side3==side1:
    print("This is equilateral")
elif side1==side2:
    print("It's Isosceles")
else:
    print("It's Scalene")
# I looked up different triangles and used a lot of and statements
