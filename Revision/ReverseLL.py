from SLL import *

s=SLL()
s.InsertFromEnd(10)
s.InsertFromEnd(20)
s.InsertFromEnd(30)
s.InsertFromEnd(40)
s.InsertFromEnd(50)


def ReverseLL(head):
    if not head or head.next==None:
        return head
    newHead=ReverseLL(head.next)
    front=head.next
    front.next=head
    head.next=None
    s.start=newHead
    return s.start

ReverseLL(s.start)

s.viewList()

# def ReverseLl(head):
#     # if head==None or head.next==None:
#     #     return head
#     #
#     # newHead=ReverseLl(head.next)
#     #
#     # front=head.next
#     # front.next=head
#     # head.next=None
#     # s.start=newHead
#     # return s.start
#
#
#
#
#
#
#
#
#     #
#     # optimize Iterative Approach
#     # SpaceCompl=O(1)
#     temp=head
#     prev=None
#     while temp!=None:
#         front=temp.next
#         temp.next=prev
#         prev=temp
#         temp=front
#
#     s.start=prev
#
#
#     # Iterative approach
#     # temp=head
#     # st=[]
#     # while temp:
#     #     st.append(temp.item)
#     #     s.DeleteFromStart()
#     #     temp=temp.next
#     # for i in range (len(st)):
#     #     s.InsertFromStart(st[i])
#     #
#     # return s.viewList()
#
#
# (ReverseLl(s.start))
# s.viewList()
