"""
1. Simple Counter:
Write a program that uses a while loop to print numbers from 1 to 10.
"""
i=1
while(i<=10):
    print(i)
    i+=1

"""
2. Countdown:
Write a program that uses a while loop to print numbers from 10 to 1 in descending order.
"""
z=10
while z>=0:
    print(z)
    z+=-1
"""
3. Factorial Calculation:
Write a program that calculates the factorial of a given number using a while loop.
"""
num= int(input("enter a number"))     

fac=1
o=1

while o<=num:
    fac=fac*o
    o=o+1
    print("factorial of",num,"is",fac)

"""
4. Password Guessing Game:
Create a simple password guessing game using a while loop. Ask the user to guess a predefined password and provide appropriate feedback.
"""
pwd="password"
guess=""

while guess !=pwd:
    guess=input("Enter the password:")
    if guess==pwd:
        print("Correct password!")
    else:
        print("Incorrect password")

"""
5. Sum of Digits:
Write a program that calculates the sum of the digits of a given number using a while loop.
"""
n=int(input("Enter a number:"))
tot=0
while(n>0):
    dig=n%10
    n=n//10
    print("The total sum of the digits is:",tot)

"""
6. Fibonacci Series:
Write a program that prints the first n numbers in the Fibonacci sequence using a while loop.
"""