'''
stack=[]
stack.append(1)
stack.append(2)
print(stack)
#Added Stack
print(stack.pop())
'''
from collections import deque  
my_stack = deque()  
  
# append() function is used to push   
# element in the my_stack   
my_stack.append('a')  
my_stack.append('b')  
my_stack.append('c')  
  
print('Initial my_stack:')  
print(my_stack)  
  
# pop() function is used to pop   
# element from my_stack in    
# LIFO order   
print('\nElements poped from my_stack:')  
print(my_stack.pop())  
print(my_stack.pop())  
print(my_stack.pop())  
  
print('\nmy_stack after elements are poped:')  
print(my_stack)   
