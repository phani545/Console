#Remove the punctuations in the string

from string import punctuation

#print(punctuation) 

#P-mystr = "";
def punc(str):
    mystr=""
    for c in str:
        if c not in punctuation:
            mystr+=c;
    print(mystr, sep='\n')
    print()
str = input("Enter the string:")  
punc(str)

    
        