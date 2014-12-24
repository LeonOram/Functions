#Leon Oram
#17-12-2014
#Functions 2
import pdb

values = [float(8.17),float(1.49),float(2.78),float(4.25),float(12.70),float(1.23),float(2.02),float(6.09),float(0.15),float(0.77),float(4.02),float(6.75),float(7.51),float(1.93),float(0.09),float(5.99),float(6.33),float(9.06),float(2.76),float(0.98),float(2.36),float(0.15),float(1.97),float(0.07)]

def get_input():
    cyp = input("Please enter your encrypted message: \n" )
    cyp=cyp.lower()
    words = cyp.split()
    return words
#try each interation of ceaser and add value
    #turn all letters in word to unicode
    #words = [[h,e,l,l,o][w,o,r,l,d]]]
    #values = [123,123]

def get_letter(word_list):
    letter=[]
    word_unicode=[]
    for word_num,word in enumerate(word_list):
        for letter_num,letters in enumerate(word):
            letter.append(letters) #e.g [3,4,5,6]
        word_unicode.append(convert(letter))
        letter=[]
    return word_unicode
            
def convert(letters):
    letters_uni=[]
    for letter in letters:
        letters_uni.append(ord(letter))
    return letters_uni
    

word_list = get_input()
word_unicode = get_letter(word_list)
word_total=0
word_total_value=[]

for word_number,current_word in enumerate(word_unicode):
    for count in range(0,26):
        for current_letter in current_word:
            #print(current_letter+count)
            if current_letter + count > 120:
                current_letter = current_letter - 26
            #print(current_letter+count-97)
            word_total = word_total + values[current_letter+count-97]
            word_total_value.append(word_total)
            Sword_total=0
    print(word_total_value)
