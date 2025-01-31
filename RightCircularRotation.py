arr=[3,4,5]
n=[1,2]
k=2
def Rotation(arr,k,n):
    k=len(arr)%k
    x=Reverse(arr[:k])
    y=Reverse(arr[k:])
    z=x+y
    ans=Reverse(z)
    for i in n:
        print(ans[i])



def Reverse(arr):
    if len(arr)==1:
        return arr
    start=0
    end=len(arr)-1
    while start<end:
        arr[start],arr[end]=arr[end],arr[start]
        start+=1
        end-=1
    return arr








Rotation(arr,k,n)