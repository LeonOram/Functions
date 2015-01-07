#Leon Oram
#29-12-2014
#Functions 2 1

def get_input():
    string=input("Please enter your message: ")
    string=string.lower()
    string = string.split()
    shift=int(input("Please enter the value to shift: "))
    return string,shift

def convert_unicode(string):
    uni_string=[]
    for count,word in enumerate(string):
        for character in word:
            uni_string.append(ord(character))
        uni_string.append(0)
    return uni_string

def convert_shift(uni_string,shift):
    cypher=[]
    for character in uni_string:
        new = character + shift
        if new > 122:
            new = new - 26
        elif new < 97:
            new = new+26
        cypher.append(new)
    return cypher

def convert_string(string,shift):
    word = ""
    new_string=[]
    for character in string:
        if character != shift:
            new_string.append(chr(character))
        else:
            new_string.append(" ")
    for character in new_string:
        word = word+character
    print(word)
    
string,shift  =get_input()
uni_string = convert_unicode(string)
string = convert_shift(uni_string,shift)
convert_string(string,shift)
