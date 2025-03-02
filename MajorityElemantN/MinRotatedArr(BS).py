arr=[1,2,3,4,5]
def Min(arr):
    ans=float('inf')
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if  arr[low]<=arr[mid]:
            ans = min(ans, arr[low])
            low=mid+1

        elif arr[low]<=arr[high]:
            ans = min(ans, arr[low])

            break
        else:
            ans=min(arr[mid],ans)
            high=mid-1

    print(ans)
Min(arr)