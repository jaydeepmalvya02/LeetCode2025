arr=[25,46,28,49,24]
m=4

def Allocate(arr,m):
    low=max(arr)
    high=sum(arr)
    while low<=high:
        mid=(low+high)//2
        t=countStu(arr,mid)
        if t<=m:
            high=mid-1
        else:
            low=mid+1
    return low

def countStu(arr,pages):
    s=1
    p=0
    for i in range(len(arr)):
        if p+arr[i]<=pages:
            p += arr[i]

        else:
            s += 1
            p = arr[i]

    return s
print(Allocate(arr,m))