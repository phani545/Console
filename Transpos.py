#Transpose the matrix

import numpy as np
x = [[3,4],
     [5,7],
     [2,1]]

result=[[0,0,0],
        [0,0,0]]

c =np.transpose(x)
print("NUmp is : {} ".format(c))
for i in range(len(x)):
    for j in range(len(x[0])):
        result[j][i]=x[i][j]

print("Matrix::")
for r in result:
    print(r)