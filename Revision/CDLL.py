class Node:
    def __init__(self,prev=None,item=None,next=None):
        self.prev=prev
        self.item=item
        self.next=next

class CDLL:
    def __init__(self):
        self.head=None
        self.tail=None
    def InsertAtFirst(self,value):
        n=Node(self.tail,value,self.head)
        if self.head==None:
            self.tail=n
        self.head=n
        self.tail.next=self.head

    def InsertAtLast(self,value):
        n = Node(self.tail, value,self.head)
        if self.head==None:
            self.tail=n
            self.head=n
        else:
            self.tail.next=n
            self.tail=n
        self.head.prev=self.tail
    def InsertAfter(self,target,value):
        n=Node(target,value,target.next)
        if target==self.tail:
            self.tail=n
        #     self.tail.next=self.head
        target.next=n
        self.head.prev = self.tail
    def DeleteFirst(self):
        self.tail.next=self.head.next
        self.head=self.head.next
        self.head.prev=self.tail

    def DeleteLast(self):
        if self.head==self.tail:
            self.tail=None
            self.head=None
        else:
            self.tail=self.tail.prev
            self.head.prev=self.tail
            self.tail.next=self.head


    def DeleteItem(self,value):
        if self.head.item==value:
            return self.DeleteFirst()
        elif self.tail.item ==value:
            return self.DeleteLast()

        else:
            temp=self.head.next
            while temp.next.item!=value and temp!=self.head:
                temp=temp.next
            temp.next=temp.next.next
            temp.next.prev=temp


    def Search(self,value):
        if self.head.item==value:
            return self.head
        elif self.tail.item==value:
            return self.tail
        else:
            temp=self.head.next
            while temp!=self.head and temp.item!=value:
                temp=temp.next
            return temp

    def ViewList(self):
        if self.head==None:
            print("Empty List")
        else:
            print(self.head.item,end="<->")
            temp=self.head.next
            while temp!=self.head:
                print(temp.item,end="<->")
                temp=temp.next

cd=CDLL()
cd.InsertAtFirst(40)
cd.InsertAtFirst(30)
cd.InsertAtFirst(20)
cd.InsertAtLast(50)
cd.InsertAfter(cd.Search(50),55)
# cd.DeleteLast()
# cd.DeleteItem(40)
print(cd.head.prev.item)
cd.ViewList()
