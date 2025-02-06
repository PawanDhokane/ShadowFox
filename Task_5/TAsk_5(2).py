# You and your partner are planning a trip, and you want to track expenses.
# Create two dictionaries, one for your expenses and one for your partner's expenses. Each dictionary should contain at least 5 expense categories and their corresponding amounts. 
# My expenses :  
my_expenses = { 
"Hotel": 1200, 
"Food": 1200, 
"Transportation": 550, 
"Attractions": 500, 
"Healthcare" : 200,
"Shopping" : 600,
"Miscellaneous": 200 
} 
# my partner's expenses : 
partner_expenses = { 
"Hotel": 1000, 
"Food": 900, 
"Transportation": 600, 
"Attractions": 400,
"Healthcare": 400, 
"Shopping": 1900,
"Miscellaneous": 150 
}
#  Calculate the total expenses for each of you and print the results. 
my_total = 0
for expense in my_expenses :
    my_total = my_total + my_expenses[expense]
print("My total expenses are : ", my_total)

partner_total = 0
for expense in partner_expenses :
    partner_total = partner_total + partner_expenses[expense]
print("Partner's total expenses are : ", partner_total)

# Determine who spent more money overall and print the result.
if my_total>partner_total:
    print("I spent more money than my partner.")
elif my_total==partner_total:
    print("We spent equal money.")
else : 
    print("My partner spent more money than me.") 

# Find out the expense category where there is a significant difference in spending
#  between you and your partner. 
# Print the category and the difference
def find_significant_difference(my_expenses, partner_expenses):
    max_difference = 0
    category_with_max_difference = ""
    
    # Loop through each expense category
    for category in my_expenses:
        # Calculate the difference in spending for each category
        difference = abs(my_expenses[category] - partner_expenses[category])
        
        # Check if this is the highest difference so far
        if difference > max_difference:
            max_difference = difference
            category_with_max_difference = category
            
    return category_with_max_difference, max_difference

# Find the category with the significant difference
category, difference = find_significant_difference(my_expenses, partner_expenses)

# Print the result
print(f"The category with the significant difference in spending is: {category}")
print(f"The difference in spending is: {difference}")
