#Leon Oram
#28-11-2014
#Dev 3
global Bob
Bob = "Hi!"

def inpu():
    valid = False
    while valid == False:
        amount = float(input("Please enter the amount: "))
        print("1.£→$")
        print("2.£→€")
        print("3.€→£")
        print("4.€→$")
        print("5.$→£")
        conversion = int(input("6.$→€ \n"))
        valid = validate(conversion)
    return amount,conversion

def validate(conversion):
    valid = False
    if conversion > 0 and conversion <=6:
        valid = True
    return valid

def get_rate(conversion):
    if conversion == 1:
        rate = 1.601
    elif conversion == 2:
        rate = 1.229
    elif conversion == 3:
        rate = 0.814
    elif conversion == 4:
        rate = 1.302
    elif conversion == 5:
        rate = 0.625
    elif conversion == 6:
        rate = 0.768
    return rate
    

def convert(amount,rate):
    total = amount * rate
    return total

amount,conversion = inpu()
rate = get_rate(conversion)
total = convert(amount,rate)
print(total)
