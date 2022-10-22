class Queue(object):
    def __init__(self):
        self.queue=[]
    
    def isEmpty(self):
        return self.queue==[]
    
    def enqueue(self,data):
        self.queue.insert(0,data)
        return '{} added to queue'.format(data)
    
    def dequeue(self,data):
        return self.queue.pop()
    
    def sizequeue(self):
        return '{} size of queue'.format(len(self.queue))
        
if __name__ == '__main__':
    
    Q=Queue()
    print(Q.enqueue(2))
    print(Q.sizequeue())
    print(Q.isEmpty())
    
    
    