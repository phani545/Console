#numbers 1 to 1000 which divisible by 7 not by 5
l = []

for i in range(1,1000):
    if i%7==0 and i%5!=0:
        l.append(str(i))

print(", ".join(l))
