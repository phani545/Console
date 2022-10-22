#Sorited the string

#input :: RED-BLUE-GREEN-WHITE-YELLOW



items = [n for n in input("ENter the string: ").split("-")]
items.sort()
print('-'.join(items))