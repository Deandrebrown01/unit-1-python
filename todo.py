ToDos=[]



while True:
    Remove=input("Would you like to remove or add from the list?")
    
    print(ToDos)

    if Remove =='remove':
        A=input("What do you want to remove?")
        ToDos.remove(A)
        print(ToDos)
    elif Remove =='add':
        B=input("What do you want to add?")

        ToDos.append(B)
        print(ToDos)
    else:
        print('Ok No Problem')

    B=print("Your current list is")
    print(ToDos)















