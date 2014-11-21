#Leon Oram
#21-11-2014
#Fun Dev Task 1

global Bob

def user_input():
    hours = int(input("Please input the number of hours: "))
    mins = int(input("Please input the number of minutes: "))
    seconds = int(input("Please input the number of seconds: "))
    return hours,mins,seconds

def total_time(hours,mins,seconds):
    addi_mins =cal_hours(hours)
    mins = mins + addi_mins
    addi_seconds = cal_mins(mins)
    seconds = seconds + addi_seconds
    return seconds
    
def cal_hours(hours):
    addi_mins = hours * 60
    return addi_mins

def cal_mins(mins):
    addi_seconds = mins * 60
    return addi_seconds

def display(total):
    print(total)

def main():
    hours,mins,seconds = user_input()
    total = total_time(hours,mins,seconds)
    display(total)

main()
