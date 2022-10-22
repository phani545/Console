#Start the index from 1 for list
from operator import index


li = [45,25,66,33,21,85]

for ind,val in enumerate(li,start =1):
    print("{} ===> {}".format(ind,val))
    
    
print(list(enumerate(li)))