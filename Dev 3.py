#Leon Oram
#28-11-2014
#Dev 3

global Bob
Bob = "Hi!"

def inpu():
    while valid == False
        amount = int(input("Please enter the amount: "))
        conversion = int(input("1.£→$ \n2.£→€ \n3.€→£ \n4.€→$ \n5.$→£ \n6.$→€ \n"))
        valid = validate(conversion)
    return amount,conversion

def validate(conversion):
    if conversion > 0 and conversion <=6:
        valid = True
    return valid

amount,conversion = inpu()
rate = select_conversion(conversion)
total = convert(rate)
display(total)
