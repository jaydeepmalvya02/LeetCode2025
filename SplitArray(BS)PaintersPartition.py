arr=[10,20,30,40]
k=2
def SplitArr(arr,k):
    low=max(arr)
    high=sum(arr)
    while low<=high:
        mid=(low+high)//2
        t=CountT(arr,mid)
        if t<=k:
            high=mid-1
        else:
            low=mid+1
    return low


def CountT(arr,m):
    count=1
    p=0
    for i in range(len(arr)):
        if p+arr[i]<=m:
            p+=arr[i]
        else:
            count+=1
            p=arr[i]
    return count
print(SplitArr(arr,k))