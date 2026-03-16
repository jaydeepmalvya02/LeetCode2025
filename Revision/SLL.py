class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
class SLL:
    def __init__(self):
        self.start=None

    def InsertFromStart(self,value):
        n=Node(value)
        n.next=self.start
        self.start=n

    def InsertFromEnd(self,value):
        n=Node(value)
        if self.start==None:
            self.start=n
        else:
            temp=self.start
            while temp.next!=None:
                temp=temp.next
            temp.next=n
    def InsertAtPosition(self,target,value):
        n=Node(value,target.next)
        target.next=n

    def DeleteFromStart(self):
        if self.start !=None:
            self.start=self.start.next
        else:
            print("Empty List")
    def DeleteFromLast(self):
        if self.start !=None:
            if self.start.next==None:
                self.start=None
            else:
                temp=self.start
                while temp.next.next !=None:
                    temp=temp.next
                temp.next=None
        else:
            print("Empty List")

    def DeleteItem(self,value):
        if self.start!=None:
            if self.start.item==value and self.start.next==None:
                self.start=None
            elif self.start.item==value:
                self.start=self.start.next
            else:
                temp=self.start
                while temp.next.item!=value:
                    temp=temp.next
                temp.next=temp.next.next

    def Search(self,value):
        if self.start is not None:
            if self.start.item==value:
                return self.start
            else:
                temp=self.start
                while temp is not  None:
                    if temp.item==value:
                        return temp
                    temp=temp.next
    def viewList(self):
        if self.start==None:
            print("Empty")
        else:
            temp=self.start
            while temp is not None:
                print(temp.item,end="->")
                temp=temp.next


s=SLL()
#
# s.InsertFromStart(40)
#
# s.InsertFromStart(30)
#
# s.InsertFromStart(20)
#
# s.InsertFromStart(10)
# s.InsertFromEnd(50)
# s.InsertAtPosition(s.Search(40),45)
# s.DeleteFromStart()
# s.DeleteFromLast()
# s.DeleteItem(10)
# s.viewList()
