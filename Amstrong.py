#l= [2,34,5]
#print(sum(l))

#Find the weather number is amstrong numner or not
n = int(input("Enter the number:"))
print(n)
sn = n
ld = len(str(n))
print("lenght of digits:", id)
sum = 0
while n > 0:
    x = n % 10
    sum = sum + x**ld
    n = n//10
if sum ==  sn:
    print("Number {} is Amstrong Number".format(sn))
else:
    print("Number {} is not a Amstrong Number".format(sn))