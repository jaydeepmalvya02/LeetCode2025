arr=[[1,1,1],
     [1,0,1],
     [1,1,1]]
m=len(arr)
n=len(arr[0])
def SetMatrixZero(arr,n,m):

     row = [0] * n
     col = [0] * m
     for i in range(n):
          for j in range(m):
               if arr[i][j] == 0:
                    row[i] = 1
                    col[j] = 1

     for i in range(n):
          for j in range(m):
               if col[j] or row[i] == 1:
                    arr[i][j] = 0
     return arr

#
#     i=0
#     while i<m:
#         j=0
#         while j<n:
#             if arr[i][j]==0:
#                 markRow(i,m,arr)
#                 markCol(j,n,arr)
#             j+=1
#
#         i+=1
#
#     for i in range(m):
#         for j in range(n):
#             if arr[i][j]==-1:
#                 arr[i][j]=0
#     return (arr)
# def markRow(i,m,arr):
#     for j in range(m):
#         if arr[i][j]!=0:
#             arr[i][j]=-1
#
#     return arr
#
# def markCol(j,n,arr):
#     for i in range(n):
#         if arr[i][j] != 0:
#             arr[i][j] = -1
#
#     return arr
x=SetMatrixZero(arr,n,m)
print(x)