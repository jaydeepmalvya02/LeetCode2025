arr=[1,2,3,4,5,6,7,8,9,10]
d=5
def CapacitytoD(arr,d):
    low=max(arr)
    high=sum(arr)
    while low<=high:
        mid=(low+high)//2
        t=ShipPakage(arr,mid)
        if t<=d:
            high=mid-1
        else:
            low=mid+1

    return low
        
def ShipPakage(arr,j):
    days=1
    c=0
    for i in range(len(arr)):
        if c+arr[i]<=j:
            c+=arr[i]
        else:
            days+=1
            c=arr[i]
    return days
print(CapacitytoD(arr,d))