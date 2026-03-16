import math
arr=[30,11,23,4,20]
h=5
def Bananas(arr,h):
    ans=-1
    low=1
    high=max(arr)
    while low<=high:
        mid=(low+high)//2
        t=Time(arr,mid)
        if t<= h:
             ans=mid
             high = mid - 1
        elif t>h:
            low=mid+1

    print(low)


def Time(arr,h):
    ans=0
    for i in range(len(arr)):
        ans+=math.ceil(arr[i]/h)
    return ans

Bananas(arr,h)