class Node:
    def __init__(self,prev=None,item=None,next=None):
        self.prev=prev
        self.item=item
        self.next=next

class DLL:
    def __init__(self):
        self.start=None

    def InsertFromStart(self,value):
        n=Node(None,value)
        if self.start!=None:
            n.next=self.start
        self.start=n
    def InsertFromLast(self,value):
        if self.start ==None:
            n=Node(None,value)
            self.start=n
        else:
            temp=self.start

            while temp.next !=None:
                temp=temp.next
            n=Node(temp,value)
            temp.next=n
    def InsertAfter(self,target,value):
        n=Node(target,value,target.next)
        target.next=n

    def DeleteFromStart(self):
        self.start=self.start.next
        self.start.prev=None

    def DeleteFromEnd(self):
        if self.start!=None:
            if self.start.next==None:
                self.start=None
            else:
                temp=self.start
                while temp.next.next !=None:
                    temp=temp.next
                temp.next.prev=None
                temp.next=None

    def DeleteItem(self,value):
        if self.start!=None:
            if self.start.item==value and self.start.next==None:
                self.start=None
            elif self.start.item==value:
                self.start=self.start.next
                self.start.prev=None
            else:
                temp=self.start
                while temp.next.item!=value:
                    temp=temp.next
                temp.next=temp.next.next
                temp.next.prev=temp






    def Search(self,value):
        if self.start!=None:
            if self.start.item==value:
                return self.start
            else:
                temp=self.start
                while temp.item !=value:
                    temp=temp.next
                return temp
    def ViewList(self):
        if self.start==None:
            print("Empty List")
        else:
            temp=self.start
            while temp is not None:
                print(temp.item,end='<->')
                temp=temp.next



d=DLL()
d.InsertFromLast(10)
d.InsertFromLast(20)
d.InsertFromLast(30)
d.InsertAfter(d.Search(20),25)
# d.DeleteFromEnd()
d.DeleteItem(25)
d.ViewList()


