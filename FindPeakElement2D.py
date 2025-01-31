mat=[[1,2,3],[8,16,4],[7,6,5]]
def FindPeak(mat):
    n = len(mat)
    m = len(mat[0])
    x, y = 0, m - 1
    while x < n or y >= 0:
        if x + 1 < n and mat[x + 1][y] > mat[x][y]:
            x += 1
        elif y - 1 >= 0 and mat[x][y] < mat[x][y - 1]:
            y -= 1
        else:
            break
    return [x, y]


# n=len(arr)
    # m=len(arr[0])
    # if n==1 and m==1:
    #     return [0,0]
    # if arr[0][0]>arr[0][1] and arr[0][0]>arr[1][0]:
    #     return [0,0]
    # if arr[0][m-1]>arr[0][m-2] and arr[0][m-1]>arr[1][m-1]:
    #     return [0,m-1]
    # if arr[n-1][0]>arr[n-1][1] and arr[n-2][0]<arr[n-1][0]:
    #     return [n-1,0]
    # if arr[n-1][m-1]>arr[n-1][m-2] and arr[n-1][m-1]>arr[n-2][m-1]:
    #     return [n-1][m-1]
    # low=1
    # high=n-2
    # mid=m-2
    # while low <n and mid>0:
    #     if arr[low][mid]>arr[low][mid-1] and arr[low][mid]>arr[low][mid+1] and arr[low+1][mid]<arr[low][mid]:
    #         return [low,mid]
    #     elif arr[low][mid]<arr[low][mid+1] :
    #         mid-=1
    #     else:
    #         low+=1

def Largest(arr):
    n=len(arr)
    l=-1
    for i in range(n):
        if arr[i]>l:
            l=arr[i]
    return l


x=FindPeak(mat)
print(x)

