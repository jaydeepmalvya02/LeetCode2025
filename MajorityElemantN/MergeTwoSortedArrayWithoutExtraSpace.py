import math
arr1=[1,2,3,0,0,0]
arr2=[2,5,6]
n=3
m=3
def MergeArray(arr1,arr2,n,m):
    l=n+m
    gap=(l//2)+(l%2)
    while gap>0:
        left = 0
        right =left+ gap
        while right < n + m :
            if left<n and right>=n:
                Swap(arr1,arr2,left,right-n)
            elif left>=n:
                Swap(arr2,arr2,left-n,right-n)
            else:
                Swap(arr1, arr1, left, right)
            left += 1
            right += 1

        if gap==1:
            break
    

        gap=(gap//2)+gap%2
    print(arr1[:n]+arr2)
def Swap(arr1,arr2,i,j):
    if arr1[i]>arr2[j]:
        arr2[j],arr1[i]=arr1[i],arr2[j]
    return arr1,arr2









    # i = 0
    # j = 0
    # while i < n + m - 1 and j < m:
    #     k = n + m - 2
    #     while k > i:
    #         arr1[k + 1] = arr1[k]
    #         k -= 1
    #     if arr1[i] > arr2[j]:
    #         arr1[i + 1] = arr1[i]
    #         arr1[i] = arr2[j]
    #     else:
    #         arr1[i + 1] = arr2[j]
    #     i += 1
    #     j += 1
    # print(arr1)


MergeArray(arr1,arr2,n,m)