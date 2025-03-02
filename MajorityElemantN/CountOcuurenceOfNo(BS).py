arr=[5,7,7,8,8,10]
x=8
def FirstAndLast(arr,x):

    f=First(arr,x)
    l=Last(arr,x)
    return (f,l)

def First(arr,x):
    f=-1
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==x:
            f=mid
            high=mid-1
        elif arr[mid]>x:
            high=mid-1
        else:
            low=mid+1
    return f

def Last(arr,x):
    l=-1
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==x:
            l=mid
            low=mid+1
        elif arr[mid]>x:
            high=mid-1
        else:
            low=mid+1
    return l
def CountOcurence(arr,x):
    f = First(arr, x)
    l = Last(arr, x)
    if f==-1:
        return 0
    return l-f+1
print(CountOcurence(arr,x))

