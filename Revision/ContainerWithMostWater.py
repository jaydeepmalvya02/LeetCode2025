height = [1,8,6,2,5,4,8,3,7]
def ContainerBrute(arr):
    n=len(arr)
    ans=float("-inf")
    for i in range(n):
        res=0
        for j in range(i,n):
            h=0
            if i!=j:
                if arr[i]<arr[j]:
                    h=arr[i]
                else:
                    h=arr[j]
            w=j-i
            res=w*h
            ans=max(ans,res)







    # left=0
    # right=n-1
    # h=0
    # while left<right:
    #     if arr[left]<arr[right]:
    #         h=arr[left]
    #     else:
    #         h=arr[right]
    #     w=right-left
    #     r=w*h
    #     ans=max(r,ans)
    #
    #     left+=1
    #     right-=1
    print(ans)
ContainerBrute(height)

def ContainerOptimize(arr):
    n=len(arr)
    left = 0
    right=n-1

    ans=0

    while left<right:
        h=min(arr[left],arr[right])
        w = right - left
        if arr[left]<arr[right]:
            left+=1
        else:
            right-=1

        r=w*h
        ans=max(r,ans)

        
    print("ans:->",ans)

ContainerOptimize(height)


