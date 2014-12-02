#Leon Oram
#28-11-2014
#Dev 3

def get_input():
    print("Please select what conversion to carry out: ")
    print("1. Feet and Inches to Meters and Centimeters")
    print("2. Meters and Centimeters to Feet and Inches")
    conversion = input(int())
    return conversion

def select_conversion(conversion):
    if conversion == 1:
        total = feet_to_meter()
    
