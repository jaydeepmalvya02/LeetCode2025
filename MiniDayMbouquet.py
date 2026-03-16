def minDays( bloomDay, m,k) :
    ans=-1
    if len(bloomDay) < m * k:
        return -1
    l = min(bloomDay)
    h = max(bloomDay)
    while l<=h:
        mid=(l+h)//2

        t=Possible(bloomDay, mid, m, k)
        if t>=m:
            ans=mid
            h=mid-1
        else:
            l=mid+1

    return l


def Possible( arr, day, m, k):
    c = 0
    b = 0
    for i in range(len(arr)):
        if arr[i] <= day:
            c += 1
        else:
            b += c // k
            c = 0
    b += c // k
    return b

arr=[1,10,3,10,2]
m=3
k=1
print(minDays(arr,m,k))
