class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next


class CLL:
    def __init__(self):
        self.head=None
        self.tail=None
    def InsertAtFirst(self,value):
        n=Node(value)
        if self.head==None:
            self.tail=n


        n.next=self.head
        self.head=n
        self.tail.next = self.head


    def InsertAtLast(self,value):
        n=Node(value)
        if self.head==None:
            self.head=n
            self.tail=n
        else:
            self.tail.next=n
            self.tail=n
            self.tail.next=self.head

    def InsertAfter(self,target,value):
        n=Node(value,target.next)
        if target==self.tail:
            self.tail=n
        target.next = n

    def DeleteFirst(self):
        self.head=self.head.next
        self.tail.next=self.head

    def DeleteLast(self):
        if self.head==self.tail:
            self.tail=None
            self.head=None
        else:
            temp=self.head.next
            while temp.next.next!=self.head:
                temp=temp.next
            temp.next=temp.next.next
            self.tail=temp
    def DeleteItem(self,value):
        if self.head.item==value:
            return self.DeleteFirst()
        elif self.tail.item==value:
            return self.DeleteLast()
        else:
            temp=self.head.next
            while temp.next!=self.head and temp.next.item!=value:
                temp=temp.next
            temp.next=temp.next.next




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
            print("Empty")
        else:
            temp=self.head.next
            print(self.head.item,end="->")
            while temp!=self.head:
                print(temp.item,end="->")
                temp=temp.next



c=CLL()
c.InsertAtFirst(30)
c.InsertAtFirst(20)
c.InsertAtFirst(10)
c.InsertAtLast(40)
c.InsertAfter(c.Search(40),45)
c.DeleteItem(30)

c.ViewList()

