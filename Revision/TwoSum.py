arr=[2,7,11,15]
target=9

def Brute(arr,target):
    n=len(arr)
    for i in range(n):
        for j in range(n-1):
            if arr[j]+arr[j+1]==target:
                return (j,j+1)


print(Brute(arr,target))

def Optimize(arr,target):
    n = len(arr)
    d={}
    for i in range(n):
        r= target-arr[i]
        if r in d:
            print(d[r],i)
        else:
            d[arr[i]]=i


    print(d)
Optimize(arr,target)

