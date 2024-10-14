'''''reverse_list_assignment.py
Bo Lontum
lab

Objective: Practice reversing a list and transferring its elements into a new list using loops.
Task: Write a Python program that works with the list called laura_things containing the following items:
"sewing machine"
"scissor"
"cutting mat"
"television"
Your program should do the following:
Create a list called laura_things with the items listed above.
Reverse the order of the items in laura_things.
Transfer each item from the reversed list into a new list called reversed_things.
Print out the new list reversed_things to show that it contains the items in reverse order.
Requirements:
You must reverse the list using slicing or a loop (do not use Python's built-in reverse methods like reverse() ).
The final output should look like this:
['television', 'cutting mat', 'scissor', 'sewing machine']
Bonus Challenge:
After reversing the list and creating reversed_things, print a message that says: "The list has been successfully reversed!"    '''


# Create the initial list called laura_things
laura_things = ["sewing machine", "scissor", "cutting mat", "television"]

# Create an empty list to hold the reversed items
reversed_things = []

# Use a loop to reverse the list
for item in range(len(laura_things) -1, -1, -1):  
    reversed_things.append(laura_things[item]) # Add items to reversed_things in reverse order

# Print the new reversed list
print(reversed_things)

# Print success message
print("The list has been successfully reversed!")




