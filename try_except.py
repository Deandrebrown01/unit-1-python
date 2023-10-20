try:
 age = int(input('Enter your age: '))
except:
 #This code isnt unable to convert a number in words to a base 10 number

 faveNum = int(input('What is your favorite number: ')) 
  
  
 


if age <= 21:
 print('You are not allowed to enter, you are too young.')
else:
 print('Welcome, you are old enough.')

print("Fun Fact! Your age divided by your favorite number is: " , age / faveNum)