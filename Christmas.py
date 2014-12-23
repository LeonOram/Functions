#Leon Oram
#17-12-2014
#Functions 2

values = [8.17,1.49,2.78,4.25,12.70,1.23,2.02,6.09,0.15,0.77,4.02,6.75,7.51,1.93,0.09,5.99,6.33,9.06,2.76,0.98,2.36,0.15,1.97,0.07]
[values(i) for i in values]
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
        
