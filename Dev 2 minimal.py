def input_v():
        max_value = int(input("Please enter an odd value: "))
        count_up(max_value)
        count_down(max_value)
def count_up(max_value):
    star = "*"
    for stars in range(1,max_value,2):
        total_stars = star * stars
        print("{0:^{1}}".format(total_stars,max_value))
def count_down(max_value):
    star = "*"
    for stars in range(max_value,0,-2):
        total_stars = star * stars
        print("{0:^{1}}".format(total_stars,max_value))
max_value = input_v()




