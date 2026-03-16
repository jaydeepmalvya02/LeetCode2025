class Node:
    def __init__(self,item=None,left=None,right=None):
        self.item = item
        self.left=left
        self.right=right



from collections import deque

class BST:
    def __init__(self):
        self.root=None
    def Insert(self,data):

        self.root=self.rInsert(self.root,data)
    def rInsert(self,root,data):
        if root==None:
            return Node(data)
        if data<root.item:
            root.left=self.rInsert(root.left,data)
        elif data>root.item:
            root.right=self.rInsert(root.right,data)
        return root

    def Inorder(self):
        ans=[]
        self.rInorder(self.root,ans)
        return ans
    def rInorder(self,root,ans):
        if root!=None:
            self.rInorder(root.left,ans)
            ans.append(root.item)
            self.rInorder(root.right,ans)
    def Max(self,temp):
        curr=temp
        while curr.right!=None:
            curr=curr.right
        return curr
    def Min(self,temp):
        curr=temp
        while curr.left!=None:
            curr=curr.left
        return curr
    def Delete(self,data):
        self.root=self.rDel(self.root,data)
    def rDel(self,root,data):
        if root==None:
            return root
        if data<root.item:
            root.left=self.rDel(root.left,data)
        elif data>root.item:
            root.right=self.rDel(root.right,data)
        else:
            if root.left==None:
                return root.right
            elif root.right==None:
                return root.left
            root.item=self.Min(root.right).item
            self.rDel(root.right,root.item)
        return root
    def PreOrder(self):
        ans=[]
        self.rPre(self.root,ans)
        return ans
    def rPre(self,root,ans):
        if root!=None:
            ans.append(root.item)
            self.rPre(root.left,ans)
            self.rPre(root.right,ans)
    def PostOrder(self):
        ans=[]
        self.rPost(self.root,ans)
        return ans
    def rPost(self,root,ans):
        if root!=None:
            self.rPost(root.left,ans)
            self.rPost(root.right,ans)
            ans.append(root.item)

    def BinaryTreeInsertion(self,data):
        self.root=self.RBinaryTreeInsert(self.root,data)

    def RBinaryTreeInsert(self,root,data):
        n=Node(data)
        if not root:
            return Node(data)
        q=deque([root])
        while q:
            temp=q.popleft()
            if temp.left==None:
                temp.left=n
                return root
            else:
                q.append(temp.left)
            if temp.right ==None:
                temp.right=n
                return root
            else:
                q.append(temp.right)
    def LevelOrderTraversal(self,root):
        ans=[]
        if not root:
            return None
        q=deque([root])
        while q:
            level=[]
            for i in range(len(q)):

                temp=q.popleft()
                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right)
                level.append(temp.item)
            ans.append(level)
        return ans
    def MaxPathSum(self,root):
        self.ans=float("-inf")
        def DFS(root):
            if not root:
                return 0
            leftGain=max(DFS(root.left),0)
            rightGain=max(DFS(root.right),0)
            currSum=root.item+leftGain+rightGain
            self.ans=max(currSum,self.ans)
            return root.item+max(leftGain,rightGain)
        DFS(root)
        return self.ans




    def SameTree(self,t1,t2):
        if not t1 and not t2:
            return True
        if not t1 or not t2:
            return False

        return t1.item==t2.item and self.SameTree(t1.left,t2.left) and self.SameTree(t1.right,t2.right)

    def SymmetricTree(self,t1,t2):
        if not  t1 and not t2:
            return True
        if not t1 or not t2:
            return False
        return t1.item==t2.item and self.SymmetricTree(t1.left,t2.right) and self.SymmetricTree(t1.right,t2.left)

    def Serialize(self,root):
        if not root:
            return "[]"
        q=deque([root])
        ans=[]
        while q:
            temp=q.popleft()
            if temp:
                ans.append(str(temp.item))
                q.append(temp.left)
                q.append(temp.right)
            else:
                ans.append('null')
        while ans and ans[-1]=='null':
            ans.pop()
        return "["+','.join(ans)+']'

    def DeSerialize(self,data):
        if data=="[]":
            return None

        values=data.strip('[]').split(',')
        n=Node(int(values[0]))
        q=deque([n])
        i=1
        while q:
            temp=q.popleft()
            if i<len(values) and values[i]!='null':
                temp.left=Node(int(values[i]))
                q.append(temp.left)
                i+=1

            if i<len(values) and values[i]!='null':
                temp.right=Node(int(values[i]))
                q.append(temp.right)
                i+=1
        return self.LevelOrderTraversal(n)

    def BinaryTreeFromPre(self,Pre,In):
        self.index = 0
        if len(In)==0:
            return None

        value=Pre.pop(0)
        root=Node(value)
        s=-1
        for i in range(len(In)):
            if In[i]==value:
                s=i
                break
        left=In[:s]
        right=In[s+1::]

        print(left,right)
        root.left=self.BinaryTreeFromPre(Pre,left)
        root.right=self.BinaryTreeFromPre(Pre,right)
        return root
    def ValidateBST(self,root):
        if not root:
            return True
        return self.IsBST(root,float('-inf'),float('inf'))
    def IsBST(self,t,low,high):
        if not t:
            return True
        if not(low<t.item<high):
            return False
        return self.IsBST(t.left,low,t.item) and self.IsBST(t.right,t.item,high)
    def LCS(self,root,p,q):
        if not root or root==p or root==q:
            return root
        root.left=self.LCS(root.left,p,q)
        root.right=self.LCS(root.right,p,q)
        if root.left==None:
            return root.right
        elif root.right==None:
            return root.left
        else:
            return root














# class BST:
#     def __init__(self):
#         self.root=None
#
#     def Insert(self,data):
#         self.root=self.rInsert(self.root,data)
#     def rInsert(self,root,data):
#         if root==None:
#             return Node(data)
#         if data<root.item:
#             root.left=self.rInsert(root.left,data)
#         elif data>root.item:
#             root.right=self.rInsert(root.right,data)
#         return root
#
#     def InOrder(self):
#         ans=[]
#         self.rInorder(self.root,ans)
#         return  ans
#     def rInorder(self,root,ans):
#         if root!=None:
#             self.rInorder(root.left, ans)
#             ans.append(root.item)
#
#             self.rInorder(root.right,ans)
#     def PreOrder(self):
#         ans=[]
#         self.rPreOrder(self.root,ans)
#         return ans
#
#     def Delete(self,data):
#         self.rDelete(self.root,data)
#
#     def rDelete(self,root,data):
#         if root==None:
#             return root
#
#         if data<root.item:
#             root.left=self.rDelete(root.left,data)
#         elif data>root.item:
#             root.right=self.rDelete(root.right,data)
#         else:
#             if root.left==None:
#                 return root.right
#             elif root.right==None:
#                 return root.left
#             root.item=self.Minimum(root.right)
#             self.rDelete(root.right,root.item)
#         return root
#
#
#     def Minimum(self,temp):
#         curr=temp
#         while curr.left is not None:
#             curr=curr.left
#         return curr
#
#     def Maximum(self,temp):
#         curr=temp
#         while curr.right!=None:
#             curr=curr.right
#         return curr
#
#     def rPreOrder(self,root,ans):
#         if root!=None:
#             ans.append(root.item)
#             self.rPreOrder(root.left,ans)
#             self.rPreOrder(root.right, ans)
#
#
#



b=BST()

# b.Insert(50)
# b.Insert(30)
# b.Insert(10)
# b.Insert(40)
# b.Insert(80)
# b.Insert(60)
# b.Insert(100)
# b.Insert(90)
# b.Insert(70)
# b.Insert(65)
# b.Insert(75)
# b.Insert(72)
# b.Delete(100)
b.BinaryTreeInsertion(2)
b.BinaryTreeInsertion(1)
b.BinaryTreeInsertion(3)
# print(b.LevelOrderTraversal(b.root))
# print(b.Inorder())
# print(b.PreOrder())
# print(b.PostOrder())
# print(b.Max(b.root).item)
# print(b.Min(b.root).item)
b2=BST()

# b2.BinaryTreeInsertion(1)
# b2.BinaryTreeInsertion(2)
# b2.BinaryTreeInsertion(3)
# b2.BinaryTreeInsertion(4)
# b2.BinaryTreeInsertion(5)
# print(b2.MaxPathSum(b2.root))
b3=BST()

b3.BinaryTreeInsertion(1)
b3.BinaryTreeInsertion(3)
b3.BinaryTreeInsertion(2)


# print(b2.SameTree(b2.root,b3.root))
# print(b2.SymmetricTree(b2.root,b3.root))

print(b2.DeSerialize(b2.Serialize(b2.root)))

print(b2.LevelOrderTraversal(b2.BinaryTreeFromPre([3,9,20,15,7],[9, 3, 15, 20, 7])))

print(b.ValidateBST(b.root))
b4=BST()

b4.BinaryTreeInsertion(6)
b4.BinaryTreeInsertion(2)
b4.BinaryTreeInsertion(8)
b4.BinaryTreeInsertion(0)
b4.BinaryTreeInsertion(4)
b4.BinaryTreeInsertion(7)
b4.BinaryTreeInsertion(9)
b4.BinaryTreeInsertion(3)
b4.BinaryTreeInsertion(5)
ans=b4.LCS(b4.root,2,8)
