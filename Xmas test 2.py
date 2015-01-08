values = [8.17,1.49,2.78,4.25,12.70,1.23,2.02,6.09,0.15,0.77,4.02,6.75,7.51,1.93,0.09,5.99,6.33,9.06,2.76,0.98,2.36,0.15,1.97,0.07]

def get_input():
    cyp = input("Please enter your encrypted message: \n" )
    cyp=cyp.lower()
    return cyp

def convert_to_uni(words):
    unicode_string=[]
    for word in words:
        for character in word:
            unicode_string.append(ord(character))
    return unicode_string

def iterate(original,values):
    max_prob=0
    for shift in range(26):
        new_unicode = []
        for letter in original:
            new=letter+shift
            if new > 122:
                new = new - 26
            new_unicode.append()
        current_prob= calc_prob(new_unicode,values)
        if current_prob > max_prob:
            max_prob = current_prob
            max_it = shift

def calc_prob(unicode,values):
    for character in unicode:
        if character >9
    

words = get_input()
original_unicode = convert_to_uni(words,values)
