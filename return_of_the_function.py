"""
Task 1: Calculate the Square of a Number
Write a function that takes an integer as an argument and returns its square.
"""
def my_calc(a):
    return (a*a)

x=my_calc(7)
print(x)
assert my_calc(7) == 49
assert my_calc(9) == 81
# I asserted my functions then I did the calculation with one number since theres only one variable and I set it to the value when you multiply it by itself
"""
Task 2: Calculate the Area of a Rectangle:
Write a function that takes the length and width of a rectangle and returns its area.
"""
def my_area(c,b):
    return(c*b)
y= my_area(9,10)
print(y)

assert my_area(9,9)==81
assert my_area(7,10)==70
# On this question i put two numbers since theres two variables in the functions and then i did the math
"""
Task 3: Convert Temperature from Celsius to Fahrenheit:
Write a function that takes a temperature in Celsius and returns 
the equivalent temperature in Fahrenheit using the correct formula
"""
def my_temp(d):
    return(d * 9/5) + 32
z=my_temp(80)
print(z)
assert my_temp(80) == 176
assert my_temp(60)==140
#For task 3 I did a number then I multiplied it by 9 then divided it by 5 then I added it by 32 for both

"""
Task 4: Calculate the Average of Numbers:
Write a function that takes a list of numbers 
and returns the average (mean) of those numbers.
"""
def my_ave(k):
    return(k+10+10+10+10) /5
j=my_ave(10)
print(j)
assert my_ave(10)==10.0
assert my_ave(20)==12.0
#In task 4 I gave it one number because we are dealing with one variable and then i added it by 4 10's then divided it by 5 to get the final answer