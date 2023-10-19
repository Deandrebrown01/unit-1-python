"""
Task 1: People Class
Define a class called Person with attributes name and age.
Then, write a method within the class to introduce the person with their name and age.

Create a new object using this new class, and call the method you created.
"""
class person:
    species='Homosapien'

    def __init__(self,name,age):
        self.name="DeAndre"
        self.age="16"

    def hi(self):
        print("Hi my name is" + self.name + "I am" + self.age)
       
       
DeAndre = person("DeAndre",16)
     
     
DeAndre.hi()


        


"""
Task 2: Animals Speak
Create a base class Animal with a empty method called speak. 

Then create two subclasses, Dog and Cat, each with their own speak method. 

Create objects using these subclasses and call the speak method.
"""
class Animal:
    def speak():
        print("Bark")

class Cat:
    def speak():
        print("Meow")

Elephant=Cat("Meow")
Prince=Animal("Bark")

Elephant.speak


"""
Task 3: Banking
Create a class BankAccount with attributes balance and owner. 

Include methods for depositing and withdrawing money, which should modify the balance attribute.

Test these methods with instances of the class.
"""
class BankAccount:
    def deposit():
        print