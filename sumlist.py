#sum the list of all numbers
from functools import reduce
l = [5,4,8,9,2]
print("list", sum(l))

#print(l)
def lsum(l):
    ls = reduce(lambda x, y : x+y, l)
    print(ls)
lsum(l)    
