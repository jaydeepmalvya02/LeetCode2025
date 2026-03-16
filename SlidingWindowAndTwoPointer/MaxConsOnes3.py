arr =[1,1,1,0,0,0,1,1,1,1,0]
k=2

def MaxConsOnesBrute(arr,k):
    mxl=0
    n=len(arr)
    for i in range(n):
        zeros = 0
        for j in range(i,n):
            if arr[j]==0:
                zeros+=1
            if zeros<=k:
                mxl = max(mxl, j - i + 1)

    print(mxl)



MaxConsOnesBrute(arr,k)


def MaxOnesOptimal(arr,k):
    n=len(arr)
    l=0
    r=0
    mx=0
    z=0

    while r<n:
        if arr[r]==0:
            z+=1


        if z>k:
            if arr[l] == 0:
                z -= 1
            l+=1
        if z<=k:
            mx = max(mx, r - l + 1)
        r+=1

    print(mx)
MaxOnesOptimal(arr,k)

