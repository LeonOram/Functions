#Leon Oram
#28-11-2014
#SC 1
global Bob
Bob = "Hi!"

def get_input():
    valid = False
    while valid == False:
        print("Please select what conversion to carry out: ")
        print("1. Feet and Inches to Meters and Centimeters")
        print("2. Meters and Centimeters to Feet and Inches")
        conversion = int(input(""))
        valid = validate_input(conversion)
    return conversion

def validate_input(inp):
    if inp == 1 or inp == 2:
        valid = True
    else:
        print("Invalid conversion. Try again ")
        valid = False
    return valid

def select_conversion(conversion):
    if conversion == 1:
        feet,inch = input_feet_inches()
        meters,centi = feet_to_meters(feet,inch)
        output_meters(feet,inch,meters,centi)
    elif conversion == 2:
        meter,centimeter = input_meters_centimeters()
        feet,inch = meters_to_feet(meter,centimeter)
        output_feet(meter,centimeter,feet,inch)
            
def input_feet_inches():
    valid = False
    while valid == False:
        feet = int(input("Feet: "))
        inch = int(input("Inches: "))
        valid = validate_inch(inch)
    return feet,inch

def validate_inch(inch):
    if inch < 12:
        valid = True
    else:
        print("That is not a valid format. Please try again.")
        valid = False
    return valid

def feet_to_meters(feet,inch):
    total_inch = feet * 12 + inch
    total_centimeters = total_inch * 2.54
    meters = total_centimeters // 100
    centimeters = total_centimeters % 100
    return meters,centimeters

def output_meters(feet,inch,meters,centi):
    print("{0}\" {1}' = {2}m {3:.2f}cm ".format(feet,inch,meters,centi))

def input_meters_centimeters():
    valid = False
    while valid == False:
        meters = int(input("Meters: "))
        centi = int(input("Centimeters: "))
        valid = validate_meter(centi)
    return meters,centi

def validate_meter(centi):
    if centi < 100:
        valid = True
    else:
        print("That is not a valid format. Please try again.")
        valid = False
    return valid

def meters_to_feet(meter,centimeter):
    total_centimeter = meter * 100 + centimeter
    total_inch = total_centimeter * 0.397
    feet = total_inch // 12
    inch = total_inch % 12
    return feet,inch

def output_feet(meters,centi,feet,inch):
    print("{0}m {1}cm = {2}\" {3:.2f}'".format(meters,centi,feet,inch))

conversion = get_input()
total = select_conversion(conversion)
