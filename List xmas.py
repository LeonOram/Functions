import random
count = 0

def get_list():
    numbers=[]
    for no in range(16):
        numbers.append(no)
    return numbers

def get_number(numbers):
    select = random.randint(0,len(numbers)-1)
    return select

numbers = get_list()
while count !=6:
    select = get_number(numbers)
    if numbers[select] != 0:
        print(select)
        numbers[select]=0
        count=count+1

