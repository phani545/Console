n= int(input("Enter the number:"))

dl = len(str(n))
number1 = list(map(int,str(n)))
print(number1)

number2 = list(map(lambda x:x**dl, number1))
print(number2)

s = sum(number2)
print(s)

if(s==n):
    print("number {} is a amstrongnumber".format(n))
else:
    print("Number {} is not a amstrongNumber".format(n))