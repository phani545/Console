#string palingrom




s = 'MOME'
s1 = s[::-2]

print(s1)

def Checkpalindrom(str1):
    if str1 == str1[::-1]:
        print("GIVEN STRING IS {} PALINDROME NUMBER".format(str1))
    else:
        print("GIVEN STRING is {} NOT A PALINDROM NUMBER".format(str1))
    
    
    
str1=input("ENTER THE STRING")
Checkpalindrom(str1)