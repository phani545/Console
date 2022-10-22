#permitation of string

from pickletools import string1


def getpermitations(str,i=0):
    if i == len(str):
        print("".join(str))
    for j in range(i,len(str)):
        words = [c for c in str]
        words[i],words[j] = words[j],words[i]
        getpermitations(words,i+1)
        
getpermitations("Pha")   