arr=[1,2,3,3,5,8,10,10,11]
x=4
def LowerBound(arr,x):
    lb=-1
    low=0
    high=len(arr)-1
    while low<=high:
        m=(low+high)//2
        if arr[m]>=x:
            lb=m
            high = m - 1
        elif arr[m]<x:

            low=m+1
    print(lb)
LowerBound(arr,x)


