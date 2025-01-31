arr=[3,4,-7,1,3,3,1,-4]
k=7
def Subarray(arr,k):
    n = len(arr)
    # optimize
    smap={}
    s=0
    i=0
    while i<n:
        s+=arr[i]
        if s==k:
            print(arr[:i+1])
        if s-k in smap:
            index=smap[s-k]+1
            print(arr[index:i+1])
        smap[s]=i
        i+=1
    print(smap)



    # n=len(arr)
    #
    # i=0
    # while i<n-1:
    #     s=0
    #     j=i
    #     while j<n:
    #         s+=arr[j]
    #         if s==k:
    #             print(arr[i:j+1])
    #         j+=1
    #     i+=1




Subarray(arr,k)


