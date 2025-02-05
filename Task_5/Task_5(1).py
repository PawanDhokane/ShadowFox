# Create a list of your friends' names. The list should have at least 5 names.
# Create a list of tuples. Each tuple should contain a friend's name and the length of the name. 
# For example, if someone’s name is Aditya, the tuple would be: ('Aditya', 6)
# List of friends' names
friends = ["Aditya" , "Sahil", "Avishkar", "Shuham", "Vivek", "Om", "Pawan","Atharva","Mangesh","Gaurav"]

# Create a list of tuples with the name and the length of each name
friends_with_length = [(i, len(i)) for i in friends]

# Print the list of tuples
print(friends_with_length)
