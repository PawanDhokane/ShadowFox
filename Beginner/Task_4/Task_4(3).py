# Write a program to check if two cities belong to the same country.
# Ask the user to enter two cities and print whether they belong to the same country or not. 
# Example: 
# Enter the first city: "Mumbai" 
# Enter the second city: "Chennai" 
# Output: "Both cities are in India" 
# Example: 
# Enter the first city: "Sydney" 
# Enter the second city: "Dubai" 
# Output: "They don't belong to the same country"

Australia = ["Sydney", "Melbourne", "Brisbane", "Perth"] 
UAE = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"] 
India = ["Mumbai", "Bangalore", "Chennai", "Delhi"] 

city_1 = input("Enter the first city: ").title()
city_2 = input("Enter the second city: ").title()

if city_1 in Australia  and city_2 in Australia :
    print("Both cities are in Australia.")
elif city_1 in UAE and city_2 in UAE :
    print("Both cities are in UAE.")
elif city_1 in India  and city_2 in India :
    print("Both cities are in India.")
else : 
    print("They don't belong to the same country.")



