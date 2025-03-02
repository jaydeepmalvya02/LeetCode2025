
def BinarySearch(arr,low,high,k):
    if low<=high:
        mid=(low+high)//2
        if arr[mid]==k:
            return mid

        elif arr[mid]>k:
            return BinarySearch(arr, low, mid - 1, k)

        elif arr[mid]<k:
            return BinarySearch(arr, mid + 1, high, k)
    else:
        return -1




arr=[2,4,5,6,7,8,9]
low=0
high=len(arr)-1
k=5
print(BinarySearch(arr,low,high,k))
