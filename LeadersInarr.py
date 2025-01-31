arr=[10,22,12,3,0,6]
def Leaders(arr):
    n=len(arr)
    mx=float('-inf')
    ans=[]
    for i in range(n-1,-1,-1):
        if arr[i]>mx:
            ans.append(arr[i])
            mx=arr[i]
    print(*ans)
Leaders(arr)
