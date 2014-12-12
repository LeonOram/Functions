#Leon Oram
#11-12-2014
#SC2
import random
def get_input():
    valid = False
    while valid == False:
        start_count = int(input("Please enter the starting number of counters (10-50): "))
        valid = validate_start(start_count)
    return start_count        

def validate_start(start_count):
    if start_count >= 10 and start_count <= 50:
        valid = True
    else:
        valid = False
        print("Invalid number of starting counter")
    return valid

def user_input():
    valid = False
    print("Your turn")
    while valid == False:
        user_remove = int(input("Please enter the amount of counters to remove (1, 2 or 3): "))
        valid = validate_user(user_remove)
    return user_remove


def validate_user(user):
        if user >0 and user < 4:
            valid = True
        else:
            print("Invalid amount of counters")
            valid = False
        return valid

def cpu_gen():
    print("It's the CPU's turn")
    if total_left >= 5:
        cpu_remove = random.randint(1,3)
        print("The CPU removes {0} counter(s)".format(cpu_remove))
    elif total_left == 4:
        cpu_remove = 3
    elif total_left == 3:
        cpu_remove = 2
    elif total_left == 2:
        cpu_remove = 1
    else:
        print("GG")
        cpu_remove = 1
    return cpu_remove

def remove_(remove,total_left):
    remaining = total_left - remove
    if remaining < 1:
        print("Game Over!")
        cont = False
    else:
        print("{} counters left".format(remaining))
        cont = True
    return remaining,cont

#Main
total_left = get_input()
cont = True
while cont == True:
    remove = cpu_gen()
    total_left,cont = remove_(remove,total_left)
    if cont == True:
        remove = user_input()
        total_left,cont = remove_(remove,total_left)
        if cont == False:
            print("You Lose!")
    else:
        print("You Win!")
        
    

    


