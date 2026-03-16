arr=[-1,2,3,3,4,5,1]
k=4 #Size of window

def ConstantWindow(arr,k):
    ms=float('-inf')
    left=0
    right=k-1
    s=0
    i=0
    while i<=right:
        s+=arr[i]
        i+=1
    ms=max(ms,s)
    while right<len(arr)-1:
        s-=arr[left]
        right+=1
        left+=1
        s+=arr[right]
        ms=max(ms,s)
    print(ms)
ConstantWindow(arr,k)