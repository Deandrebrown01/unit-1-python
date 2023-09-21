"""
Task 1: Create a list
Create a list with 4 elements and print it.
"""
Clothes = ["Ed Hardy", "Evisu", "True Religion", "Ralph Lauren"]
print(Clothes)

# I added my list by doing commas and using bracketts with quotations
"""
Task 2: Add Element to a List
Add an element to the end of the list. Print the updated 
list.
"""
Clothes.append("Playboy")
print(Clothes)
# I did the code Clothes.append and put a clothing brand I wanted to add in the parentheses with quotation marks, then I printed it.
"""
Task 3: Remove Element from a List
Remove a specific element from the list. Print the 
updated list.
"""
Clothes.remove("Playboy")
print(Clothes)
# I did the code clothes. remove and I typed in the brand I wanted to remove and I printed it.
"""
Task 4: Modify Element in a List
Modify an element at a specific index with a new value. 
Print the updated list.
"""
Clothes[1]="Rick Owens"
print(Clothes)
# Since we have the variable, I put the variable and added the number in place of the brand and I switched out the brand.

"""
Task 5: Append Multiple Elements to a List
Append multiple elements to the end of the list. Print 
the updated list.
"""
Clothes.append("H&M")
Clothes.append("Calvin Klein")
Clothes.append("Von Dutch")
Clothes.append("Affliction")
print(Clothes)
# I added append to the variable I've been using and I added more clothing brands. Then, I printed the variable.
"""
Task 6: Delete Element at a Specific Index
Delete an element at a specific index. Print the updated 
list.
"""
del Clothes[2]
print (Clothes)
# To delete the element I did the del code which stands for delete and I put the number for the brand I wanted to delete then I printed it.


"""
Task 7: Subsetting lists
Create a new variable equal to the first 2 items of your list
Then print out the new variable
"""
Fashion = (Clothes[0:2])
print(Fashion)
# I created a new variable and added the variable I've been using inside the parentheses and I added the numbers that have the two brands I wanted to print. Then I printed it
"""
Task 8: Extend a List
Extend the list with the elements of another list. Print 
the updated list.
"""
Apparel_a=["Affliction", "Von Dutch"]
Apparel_b=["Evisu", "Ed Hardy"]

Apparel= Apparel_a + Apparel_b
print(Apparel)
# I created a new variable with letters(a and b) and I added some brands. Then I created a new variable and added the variable A and B then I printed the new variable(Apparel)


