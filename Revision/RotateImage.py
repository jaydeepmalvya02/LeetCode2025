matrix = [[1,2,3],[4,5,6],[7,8,9]]
r=len(matrix)
c=len(matrix[0])

def RotateImage(arr,r,c):
    i=0
    while i<=r-1:
        j=i+1
        while j<c:
            if i!=j:
                arr[i][j],arr[j][i]=arr[j][i],arr[i][j]
            j+=1
        arr[i]=Reverse(arr[i])

        i+=1
    print(arr)

def Reverse(arr):
    left=0
    right=len(arr)-1
    while left<right:
        arr[left],arr[right]=arr[right],arr[left]
        left+=1
        right-=1
    return arr
RotateImage(matrix,r,c)
