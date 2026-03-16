class Counter:
    count=0
    def __init__(self,count):
        self.count+=1
        print(self.count)

c=Counter(1)
