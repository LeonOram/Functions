#Leon Oram
#17-12-2014
#Functions 2

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

def get_letter(values,word_list):
    letter=[]
    word_value=[]
    for word_num,word in enumerate(word_list):
        for letter_num,letters in enumerate(word):
            letter.append(letters) #e.g [3,4,5,6]
        word_value.append(convert(letter))
        letter=[]
    print(word_value)
            
def convert(letters):
    letters_uni=[]
    for letter in letters:
        letters_uni.append(ord(letter))
    return letters_uni
    

word_list = get_input()
letter = get_letter(values,word_list)
