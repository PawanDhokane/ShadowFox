# ********If Condition********* 
# Write a program to determine the BMI Category based on user input. 
# Ask the user to: 
# Enter height in meters 
# Enter weight in kilograms 
# Calculate BMI using the formula: BMI = weight / (height)2 
# Use the following categories: 
# If BMI is 30 or greater, print "Obesity" 
# If BMI is between 25 and 29, print "Overweight" 
# If BMI is between 18.5 and 25, print "Normal" 
# If BMI is less than 18.5, print "Underweight" 
# Example: 
# Enter height in meters: 1.75 
# Enter weight in kilograms: 70 
# Output: "Normal" 

H = float(input("Enter height in meters : "))
W = float(input("Enter weight in Kg : "))

BMI = W / ((H)**2)

if BMI >=30 : 
    print("Obesity")

if BMI>=25 and BMI<30 : 
    print("Overweight")

if BMI>=18.5 and BMI<25 :
    print("Normal")

if BMI<18.5 and BMI>0 :
    print("Underweight")


