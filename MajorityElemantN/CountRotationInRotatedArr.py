arr=[5, 1, 2, 3, 4]
def CountRotation(arr):
    index=-1
    ans=float('inf')
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[low]<=arr[mid]:
            if arr[low]<ans:
                index=low
                ans=arr[low]
            low=mid+1
        elif arr[low]<=arr[high]:
            if arr[low]<ans:
                index=low
                ans=arr[low]
            low=mid+1
        else:

            if arr[mid]<ans:
                index=mid
                ans=arr[mid]
            high = mid - 1
    print(index)
CountRotation(arr)

