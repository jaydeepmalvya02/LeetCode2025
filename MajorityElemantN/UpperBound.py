arr=[2,4,6,8,11,13]
x=10
def UpperBound(arr,x):
    up=-1
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]<x:
            up=mid
            low=mid+1
        elif arr[mid]==x:
            up=mid
            break
        else:
            high=mid-1
    print(up)

UpperBound(arr,x)