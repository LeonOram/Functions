#Leon Oram
#25-11-2014
#Dev task 2

global Bob
Bob = "Hi!"

def input_v():
    valid = False
    while valid == False:
        max_value = int(input("Please enter an odd value: "))
        valid = validate(max_value)
    count(max_value,1,max_value,2)
    count(max_value,max_value,0,-2)

def validate(value):
    if value % 2 == 1 and value > 0:
        valid = True
    else:
        print("Invalid input")
        valid = False
    return valid

def count(max_value,start,end,step):
    star = "*"
    for stars in range(start,end,step):
        print("{0:^{1}}".format(star * stars,max_value))
max_value = input_v()
