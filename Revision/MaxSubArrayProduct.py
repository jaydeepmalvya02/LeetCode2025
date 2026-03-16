arr=[-2,0,-1]

def productSubarray(arr):
    res=1
    ans=float('-inf')
    for i in range(len(arr)):

        res*=arr[i]
        ans=max(res,ans)
    print(ans)

def Brute(arr):
    n=len(arr)
    ans=float("-inf")
    for i in range(n):
        p=1
        for j in range(0,n):
            pk=1
            for k in range(i,j+1):
                print(arr[k])
                pk*=arr[k]
            p=max(p,pk)
        ans=max(p,ans)
        print()
    print("ans->",ans)
Brute(arr)

def Optimize(arr):
    n=len(arr)
    s=arr[0]
    maxi=float("-inf")
    for i in range(1,n):
        s*=arr[i]
        maxi=max(maxi,s)
        if s<0:
            s=1
    print(maxi)
Optimize(arr)

