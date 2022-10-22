class stack:
    def __init__(self):
        self.stack=list()
    
    def push(self,item):
        self.stack.append(item)
    
    def pop(self):
        if len(self.stack)>0:
            return self.stack.pop()
        else:
            return "there is no elements in stack"
        
    def peek(self):
        if len(self.stack)>0:
            return self.stack[len(self.stack)-1]
        else:
            return None
    
obj = stack()
obj.push(1)
obj.push(2)
print(obj.stack)
print(obj.pop())
print('peek element', obj.peek())
print(obj.stack)
    