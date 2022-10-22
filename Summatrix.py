a = [[1,5,6],
     [5,6,8],
     [5,3,1]]
b = [[5,2,1],
     [4,2,6],
     [8,6,3]]

result = [[0,0,0],
          [0,0,0],
          [0,0,0]]

#print("a length is :{} ".format(len(a)))
#print(a[0])

for i in range(len(a)):
    for j in range(len(a[0])):
        result[i][j] = a[i][j] + b[i][j]
        
for r in result:
    print(r)
