class Stk:
    #Constructor
    def __init__(self):
        self.stack=[]
        self.numofitems=0
        
    #Checking
    def isempty(self):
        return self.stack==[]
    
    #pushinf element
    def push(self,data):
        self.stack.insert(self.numofitems,data)
        self.numofitems+= 1 #increment index
        return '{} pushed to stack'.format(data)
    
    #pop the element
    def pop(self):
        self.numofitems-=1
        data =self.stack.pop(self.numofitems)
        return '{} pop to stack'.format(data)
    
    #size of stack
    
    def size(self):
        return len(self.stack)
    
    ##testing
    
if __name__ == '__main__':
    s = Stk()
    print(s.push(2))
    print(s.push(3))
    print(s.push(5))    
    print(s.stack)
    
    print(s.pop())
    
    print(s.push(6)) 
    print(s.push(9)) 
    print(s.stack)    

        