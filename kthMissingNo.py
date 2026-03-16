arr=[2,3,4,7,11]
k=5
def Missing(arr,k):
    low=0
    high=len(arr)-1
    c=0
    while low<=high:
        mid=(low+high)//2
        t=arr[mid]-(mid+1)

        c=t
        if t<k:
            low=mid+1
        else:
            high=mid-1
    return low+k
    # for i in range(low,high+1):
    #     t=Find(arr,i)
    #     if not t and c<k:
    #         c+=1
    #
    #     if c==k:
    #         return i


def Find(arr,t):

    for i in range(len(arr)):
        if arr[i]==t:
            return True
        else:
            return False

print(Missing(arr,k))