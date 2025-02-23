# 2. Numbers 
# 1. Write a function that takes two arguments, 145 and 'o', and
#  uses the `format` function to return a formatted string. Print the
#  result. Try to identify the representation used. 

def format_example(number, format_type):
    # Use the format specifier directly in the format function
    return format(number, format_type)

# Call the function with 145 and 'o' # o --> Octal
formatted_result = format_example(145, 'o')
print(formatted_result)


# 2. In a village, there is a circular pond with a radius of 84 meters.
#  Calculate the area of the pond using the formula: Circle Area = π
#  r^2. (Use the value 3.14 for π) Bonus Question: If there is exactly
#  1.4 liters of water in a square meter, what is the total amount of
#  water in the pond? Print the answer without any decimal point in
#  it. Hint: Circle Area = π r^2 Water in the pond = Pond Area
#  Water per Square Meter 

r=84
Area_of_circle = (3.14)*r*r
print(Area_of_circle)

Total_water = Area_of_circle/1.4
print(int(Total_water))


# 3. If you cross a 490 meter long street in 7 minutes, calculate your
#  speed in meters per second. Print the answer without any decimal
#  point in it. Hint: Speed = Distance / Time

distance = 490
time = 7*60
Speed = distance/time

print(int(Speed), "m/s")


