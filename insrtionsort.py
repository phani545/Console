def insertionarray(arr):
    
    for i in range(1,len(arr)):
        key = arr[i]
        j = i -1
        
        while j >= 0 and key < arr[j]:
            arr[j+1]=arr[j]
            print(arr[j+1])
            print("--Elements--") 
            for q in range(len(arr)):
                print("%d " % arr[q] ,sep = "\t" )
            print("--Elemenst End --")
            j-=1
        arr[j+1] = key



arr = [23,12,21,4,2]
insertionarray(arr)

for i in range(len(arr)):
    print("%d" % arr[i])    



'''
a = [11,23,44,22,42,54,66]
print(a[0])
print(a[1])
'''