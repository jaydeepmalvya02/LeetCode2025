arr=[2,2,3,3,1,2,2]
def Majority(arr):
    c=0
    v=0
    n = len(arr)
    for i in range(n):
        if c==0:
            c=1
            v=arr[i]
        elif v==arr[i]:
            c+=1
        else:
            c-=1
    print(v)
    # h={}
    # n=len(arr)
    # for i in range(n):
    #     if arr[i] in h:
    #         h[arr[i]]+=1
    #     else:
    #         h[arr[i]]=1
    #
    # for i in h:
    #     if h[i]>n//2:
    #         print(i)
Majority(arr)