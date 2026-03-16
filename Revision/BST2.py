import queue
from collections import  deque
class Node:

    def __init__(self,left=None,item=None,right=None):
        self.left=left
        self.item=item
        self.right=right

class BST:
    def __init__(self):
        self.root=None

    def Insert(self,data):

        self.root=self.rInsert(self.root,data)

    def rInsert(self,root,data):
        if root==None:
            return Node(None,data)
        elif root.item>data:
            root.left=self.rInsert(root.left,data)
        else:
            root.right=self.rInsert(root.right,data)
        return root

    def InsertLevel(self,data):
        self.root=self.RInsertLevelOrder(self.root,data)
    def RInsertLevelOrder(self,root,data):
        n=Node(None,data)
        if not root:
            return n
        q=deque([root])

        while q:
            temp=q.popleft()
            if not temp.left:
                temp.left=n
                return root
            else:
                q.append(temp.left)
            if not temp.right:
                temp.right=n
                return root
            else:
                q.append(temp.right)




    def Inorder(self):
        ans=[]
        self.rInorder(self.root,ans)
        return ans
    def rInorder(self,root,ans):
        if root is not  None:
            self.rInorder(root.left, ans)
            ans.append(root.item)
            self.rInorder(root.right, ans)
    def PreOrder(self):
        ans=[]
        self.rPre(self.root,ans)
        return ans
    def rPre(self,root,ans):
        if root!=None:
            ans.append(root.item)
            self.rPre(root.left,ans)
            self.rPre(root.right,ans)
    def maxDepth(self, root):
        if root==None:
            return 0
        lh=self.maxDepth(root.left)
        rh=self.maxDepth(root.right)
        return 1+max(lh,rh)
    def SameTree(self,t1,t2):
        a=t1
        b=t2
        if not a and not b:
            return True
        if a and b and a.item==b.item:
            return self.SameTree(a.left,b.left) and self.SameTree(a.right,b.right)
        return False

    def Invert(self,root):
        if root ==None:
            return None
        else:
            temp=root.left
            root.left=root.right
            root.right=temp
            self.Invert(root.left)
            self.Invert(root.right)
            return root
    def LevelOrder(self,root):
        ans=[]
        if root==None:
            return ans
        q=queue.Queue()
        q.put(root)
        while not q.empty():
            level=[]
            for i in range(q.qsize()):
                temp=q.get(i)
                if temp.left:
                    q.put(temp.left)

                if temp.right:
                    q.put(temp.right)
                level.append(temp.item)

            ans.append(level)

        return ans


    def MaxPathSumBt(self):
        self.ans=float('-inf')
        def dfs(node):
            if not node:
                return 0
            leftGain=max(dfs(node.left),0)
            rightGain=max(dfs(node.right),0)
            currSum=node.item+leftGain+rightGain
            self.ans=max(currSum,self.ans)
            return node.item+max(leftGain,rightGain)
        dfs(self.root)
        return self.ans
    def MaxDepth(self,root):
        if not root:
            return 0

        lh=self.MaxDepth(root.left)
        rh=self.MaxDepth(root.right)



        return 1+max(lh,rh)




b=BST()
# b.Insert(4)
# b.Insert(2)
# b.Insert(7)
# b.Insert(1)
# b.Insert(3)
# b.Insert(6)
# b.Insert(9)
# b.Insert(3)

b.Invert(b.root)
# print(b.PreOrder())
# print(b.maxDepth(b.root))
# b1=BST()
# b1.Insert(50)
# b1.Insert(40)
# b1.Insert(60)
# print(b.SameTree(b.root,b1.root))

b.InsertLevel(1)
b.InsertLevel(2)
b.InsertLevel(3)

print(b.LevelOrder(b.root))
print(b.Inorder())
print(b.MaxPathSumBt())
print(b.MaxDepth(b.root))