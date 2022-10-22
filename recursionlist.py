#recursion list sum

def recursion(data1):
    tot = 0
    for ele in data1:
        if type(ele) == type([]):
            tot = tot + recursion(ele)
        else:
            tot = tot + ele
    return tot

data1 = [2,4,[55,4,3],[2,4,3],[7,2]]
print(recursion(data1))