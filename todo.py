ToDos=[]

A=input("What do you want to add?")

ToDos.append(A)
print(ToDos)





Remove=input("Would you like to remove anything?")


delete=input("What would you like to remove from the list?")


if Remove=='Yes':
    ToDos.remove(delete)
    print(ToDos)
else:
    print("Ok No Problem")

B=print("Your current list is")
print(ToDos)











