arr=[0,3,4,7,9,10]
cows=4
def Aggressive(arr,cows):
    low=0
    high=max(arr)-min(arr)
    while low<=high:
        mid=(low+high)//2
        t=CanWePlace(arr,mid,cows)
        if t:
            low=mid+1
        else:
            high=mid-1
    return high


def CanWePlace(arr,k,cows):
    count=1
    last=arr[0]
    for i in range(1,len(arr)):
        if arr[i]-last>=k:
            count+=1
            last=arr[i]
    if count>=cows:
        return True
    else:
        return False
print(Aggressive(arr,cows))
