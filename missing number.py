arr=[1,2,4,5]
n=5
def Missing(arr,n):
    hash=[0]*(n+1)
    for i in range(len(arr)):
        hash[arr[i]]=1

    for i in range(1,n+1):
        if hash[i]==0:
            print(i)
            return i

Missing(arr,n)