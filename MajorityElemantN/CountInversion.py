arr = [2, 4, 1, 3, 5]


def CountInversion(arr):
    n=len(arr)
    return MergeSort(arr,0,n-1)

def MergeSort(arr,low,high):
    c=0
    if low>=high:
        return c
    mid =(low+high)//2
    c+=MergeSort(arr,low,mid)
    c+=MergeSort(arr,mid+1,high)
    c+=Merge(arr,low,mid,high)
    return c
def Merge(arr,low,mid,high):
    temp=[]
    left=low
    right=mid+1
    c=0
    while left<=mid and right<=high:
        if arr[left]<=arr[right]:
            temp.append(arr[left])
            left+=1
        else:
            temp.append(arr[right])
            c+=mid-left+1
            right+=1

    while left<=mid:
        temp.append(arr[left])
        left+=1
    while right<=high:
        temp.append(arr[right])
        right+=1
    for i in range(low,high+1):
        arr[i]=temp[i-low]
    return c

























    # c=0
    # if len(arr) > 1:
    #     low=0
    #     high=len(arr)-1
    #
    #     mid = len(arr) // 2
    #     l = arr[:mid]
    #     r = arr[mid:]
    #     CountInversion(l)
    #     CountInversion(r)
    #     i = j = k = 0
    #     while i < len(l) and j < len(r):
    #         if l[i] > r[j]:
    #             arr[k] = r[j]
    #             j += 1
    #             c += mid - low + 1
    #         else:
    #             arr[k] = l[i]
    #             i += 1
    #
    #         k += 1
    #     while i < len(l):
    #         arr[k] = l[i]
    #         i += 1
    #         k += 1
    #     while j < len(r):
    #         arr[k] = r[j]
    #         j += 1
    #         k += 1
    #
    # print(c)
    #

    # BruteForce
    # c=0
    # for i in range(n):
    #     for j in range(i+1,n):
    #         if arr[i]>arr[j]:
    #             c+=1
    # print(c)


print(CountInversion(arr))
