
ele = [56,33,1,22,88,21,45,13]
#ele = [12,23,24,51,1,3]

for i in range(len(ele)):
    me=i;
    for j in range(i+1,len(ele)):
        if ele[me] > ele[j]:
            me=j
    ele[i],ele[me]=ele[me],ele[i]
    
print('Sorted elements are:')

for i in range(len(ele)):
    print(ele[i])
            
