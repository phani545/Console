num = int(input("Enter the number:"))

def ISPRIME(num):
    if num > 1:
        for n in range(2,num):
            if(num%n==0):
                return False
            
        return True
    return False

print(ISPRIME(num))
