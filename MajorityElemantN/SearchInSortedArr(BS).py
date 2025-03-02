# arr=[4,5,6,1,2,3]
# x=3
def Search(arr,x):
    low=0
    high=len(arr)-1
    while (low<=high):
        mid=(low+high)//2
        if arr[mid]==x:
            return mid
        elif arr[low]<=arr[mid]:
            if arr[low]<=x and x<=arr[mid]:
                high=mid-1
            else:
                low=mid+1
        else:
            if arr[mid]<=x and x<=arr[high]:
                low=mid+1
            else:
                high=mid-1

# print(Search(arr,x))

def SearchRotate(arr,x):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2

        if arr[mid]==x:
            return mid
        elif arr[low]<=arr[mid]:
            if arr[mid]<=x and x<=arr[low]:
                high=mid-1
            else:
                low=mid+1
        else:
            if arr[mid]<=x and x <=arr[high]:
                low=mid+1
            else:
                high=mid-1





arr=[7,8,9,1,2,3,4,5,6]
x=9
print(SearchRotate(arr,x))

