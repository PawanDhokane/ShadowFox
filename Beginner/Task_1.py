# 1. Variables 
# 1. Create a variable named pi and store the value 22/7 in it.
#  Now check the data type of this variable. 
pi = 22/7
print(type(pi))

# 2. Create a variable called for and assign it a value 4. See what
#  happens and find out the reason behind the behavior that you see.

# for = 4
# print(for)

# --> SyntaxError: invalid syntax because "for" is a keyword in python...


# 3. Store the principal amount, rate of interest, and time in
#  different variables and then calculate the Simple Interest for 3
#  years. Formula: Simple Interest = P x R x T / 100
print("Simple Interest Calculation")

P = float(input("Enter principal amount : "))
R = float(input("Enter Rate of Interest : "))
T = int(input("Enter Time Period in years : "))

Simple_Interest = (P*R*T)/100

print("Simple Interest is : ", Simple_Interest)
