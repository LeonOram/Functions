values = [8.17,1.49,2.78,4.25,12.70,2.23,2.02,6.09,6.97,0.15,0.77,4.02,2.41,6.75,7.51,1.93,0.09,5.99,6.33,9.06,2.76,0.98,2.36,0.15,1.97,0.07]

def get_input():
    cyp = input("Please enter your encrypted message: \n" )
    cyp=cyp.lower()
    return cyp

def convert_to_uni(words):
    unicode_string=[]
    for word in words:
        for character in word:
            if ord(character) != 32:
                unicode_string.append(ord(character))
            else:
                unicode_string.append(0)
    return unicode_string

def iterate(original,values):
    max_prob=0
    for shift in range(27):
        new_unicode = []
        for letter in original:
            new=letter+shift
            if new > 122:
                new = new - 26
            new_unicode.append(new)
        current_prob= calc_prob(new_unicode,values)
        if current_prob > max_prob:
            max_prob = current_prob
            max_it = shift
    return max_it
    
def calc_prob(unicode,values):
    string_prob=0
    for character in unicode:
        if character >= 97 and character <= 122:
            index = character - 97
            current_prob = values[index]
            string_prob = string_prob + current_prob
    return string_prob

def convert_shift(uni_string,shift):
    cypher=[]
    for character in uni_string:
        if character != 0:
            new = character + shift
            if new > 122:
                new = new - 26
            elif new < 97:
                new = new+26
            cypher.append(new)
        else:
            cypher.append(0)
    return cypher

def convert_string(string,shift):
    word = ""
    new_string=[]
    for character in string:
        if character >= 97 and character <= 122:
            new_string.append(chr(character))
        else:
            new_string.append(" ")
    for character in new_string:
        word = word+character
    print("The most probable solution is '{0}' which is a shift of {1}".format(word,shift))

words = get_input()
original_unicode = convert_to_uni(words)
shift = iterate(original_unicode,values)
result = convert_shift(original_unicode,shift)
convert_string(result,shift)

