class Counter():
    def __init__(self, init = 0):
        self.count = init
        
    def getCount(self):
        return self.count
        
    def inc(self):
        self.count+=1