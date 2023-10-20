# Task 1: Greeting Function
# Write a function `greet(name)` that takes a name as a parameter and prints a greeting message like "Hello, [name]!".
def my_name(name):
    print("Nice to meet you" + name)

my_name("De'Andre")

# I mad a function called my_name with name inside it. Then I printed nice to meet you + the variable name. Lastly the function My_name I set as my name.

# Task 2: Sum of Two Numbers
# Write a function `sum_numbers(a, b)` that takes two numbers as parameters and returns their sum.
def sum_numbers(a,b):
    print(a + b)
 
sum_numbers(12,12)

# I made a function called sum numbers and then I made two parameters and then i printed the two parameters in the print statement. Then lastly, I put two numbers it should add.



# Task 3: Calculate Factorial
# Write a function `factorial(n)` that calculates the factorial of a given number `n`.
def my_factorial(n):
   if n==1:
       return 1
   else:
       return n* my_factorial(n-1)
   
print(my_factorial(8))



# Task 4: Check Even or Odd
# Write a function `is_even(num)` that takes a number as a parameter and returns `True` if the number is even, and `False` otherwise.
num=(input("Give me a number"))
def is_even(num):
   if num %2==0:
       print("Even")
       
   else:
       print("Odd")
       
  

   


    


# Task 5: Calculate Area of a Rectangle
# Write a function `calculate_area(length, width)` that calculates and returns the area of a rectangle given its length and width.
def calculate_area(length,width):
    print(length*width)
calculate_area(900,100)
