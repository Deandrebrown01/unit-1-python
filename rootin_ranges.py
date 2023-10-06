"""
Exercise 1:
Write a program to print numbers from 1 to 10 using a for loop.
"""
for x in range(11):
    print(x)

"""
Exercise 2:
Write a program to count by 10s from 900 to 1000
"""
for v in range(900,1001,10):
    print(v)

"""
Exercise 3:
Write a program that counts form 1-100 by 9
"""
for d in range(1,910,9):
    print(d)
"""
Exercise 4:
Write a program to calculate the sum of all numbers from 1 to 10 using a for loop.
"""
c=0
for q in range(1,11):
    c= q+c
    print(c)

"""
Excercise 5:
Uncomment the following code and run it. Then answer the following:
- What is the ouput of the code?

- Explain the iterative process that this code executes to get that output
"""

rows=5

for i in range(rows):
    for j in range(i+1):
        print('*', end=' ')
    print()
#The output of the code is it makes 5 rows with stars dedicated to each from 1 to 5. The process that this code executes is a variable called rows =5 and there are two for loops. One sets the range from 1-5 and the second 1 adds each number by 1 and it prints stars with spaces to split them. This is how the code is processed.