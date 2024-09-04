class StaticArrays:
    def __init__(self, capacity):
        self.capacity = capacity
        self.arr = [None] * capacity
        
    def insertEnd(self, value):
        if len(self.arr) == self.capacity:
            self.capacity *= 2
            self.arr.append(value)
        else:
            self.arr.append(value)
        
    def removeEnd(self):
        return self.arr.pop()
    
    def insertMiddle(self, index, value):
        if len(self.arr) == self.capacity:
            self.capacity *= 2
            self.arr.insert(index, value)
        else:
            self.arr.insert(index, value)
    
    def removeMiddle(self, index):
        return self.arr.pop(index)
    
    def printArr(self):
        return self.arr
