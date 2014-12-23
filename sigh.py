#Leon Oram
#17-12-2014
#Functions 2

values = [float(8.17),float(1.49),float(2.78),float(4.25),float(12.7),0float(1.23),float(2.02),float(6.09),float(0.15),float(0.77),float(4.02),float(6.75),float(7.51),float(1.93),float(0.09),float(5.99),float(6.33),float(9.06),float(2.76),float(0.98),float(2.36),float(0.15),float(1.97),float(0.07)]

def get_input():
    word=[]
    cyp = input("Please enter your encrypted message: \n" )
    words = cyp.split()
    return words

def itterate(word,values):
    word_total=[]
    for i,word in enumerate(words):
        for x,letter in enumerate(word):
            letter = word[word][letter]
            value = get_value(word,values)
            word_total[i] = word_total[i] + 1

#def get_value(values,word):
print(values)   
        
