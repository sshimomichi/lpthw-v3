my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print(f"Let's talk abount {my_name}.")
print(f"He's {my_height} inches tall.")
print(f"He's {my_weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = my_age + my_height + my_weight
print(f"If I add {my_age}, {my_height}, and {my_weight} I get {total}.")

# Drill

def convert_to_kg(arg1):
    # What we re doing is deriving at kg and rounding
    new_value = round(arg1/2.2046226218)
    return new_value

my_weight_in_kg = convert_to_kg(my_weight)

print(f"My weight in lbs is {my_weight}, which is {my_weight_in_kg} in kg!")
