mat=[[1,2,3,4],
[5,6,7,8],
[9,10,11,12],
[13,14,15,16]]

r=len(mat)
c=len(mat[0])
def Rotate90(mat,r,c):
    i=0
    while i<r-1:
        j=i+1
        while j<c:
            if i!=j:
                mat[i][j],mat[j][i]=mat[j][i],mat[i][j]
            j+=1
        i+=1
    for i in range(r):
        Reverse(mat[i])
    for i in range(r):
        print(mat[i])


def Reverse(arr):
    start=0
    end=len(arr)-1
    while start<=end:
        arr[start],arr[end]=arr[end],arr[start]
        start+=1
        end-=1
    return arr






    # bruteforce using extra 2d mat
    # TC->O(n*n)
    # SC->O(n*n)
    # minr = 0
    # maxr = r - 1
    # maxc = c - 1
    # minc = 0

    # ans=[[0]*c for i in range(r)]
    # i=0
    # while i<r:
    #     j=0
    #     while j<c:
    #         ans[j][r-1-i]=mat[i][j]
    #         j+=1
    #
    #     i+=1

    # while maxc >= minc:
    #     while minr <= maxr:
    #         ans[minr][minc]=mat[minc][maxr]
    #         minc+=1
    #     maxc-=1




Rotate90(mat,r,c)