# List 
#You have a list of superheroes representing the Justice League. 
 
justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"] 

# Perform the following tasks: 
# Calculate the number of members in the Justice League. 
members = len(justice_league)
print(members)

# 2. Batman recruited Batgirl and Nightwing as new members.Add them to your list. 

justice_league.append("Batgirl")
justice_league.append("Nightwing")
print("Updated List :  " ,justice_league)

# 3. Wonder Woman is now the leader of the Justice League.Move her to the beginning of the list. 

leader = justice_league.index("Wonder Woman")

justice_league.insert(0,justice_league.pop(leader))
print("List with Wonder Women as a leader : ",justice_league)

# 4. Aquaman and Flash are having conflicts, and you need to separate them. Choose either "Green Lantern" or "Superman" and move them in between Aquaman and Flash. 

superman = justice_league.index("Superman")
Flash = justice_league.index("Flash")

justice_league.insert(Flash ,justice_league.pop(superman))
print("justice league after resolving conflicts :  ",justice_league)

# 5. The Justice League faced a crisis, and Superman decided to assemble a new team. Replace the existing list with the following new members: "Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow".
justice_league.clear()
justice_league.extend(["Superman" , "Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]) 

print(justice_league)
 
# 6. Sort the Justice League alphabetically. The hero at the 0th index will become the new leader. (BONUS: Can you predict who the new leader will be?) 

justice_league.sort()
print("New leader is : ", justice_league[0])
print("Justice league : ",justice_league)
