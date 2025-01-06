arr=[1,2,3,5,6]
target=4
def InsertPosition(arr,target):
    start=0
    end=len(arr)-1
    while start<=end:
        mid=(start+end)//2
        if arr[mid]>target:
            end=mid-1
        elif arr[mid]<target:
            start=mid+1
        else:
            return mid
    return start

x=InsertPosition(arr,target)
print(x)