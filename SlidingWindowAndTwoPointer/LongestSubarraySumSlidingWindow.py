arr=[2,5,1,7,10]
k=14
def LongestSubarray(arr,k):
    l=0
    r=0
    n=len(arr)
    c=0
    s=0
    while r<n:
        s += arr[r]
        while s>k:
            s-=arr[l]
            l+=1
        if (s<=k):
            c = max(c, (r - l + 1))
        print(s)
        r += 1
    print(c)
LongestSubarray(arr,k)


# For optimize solution only for length of subarray
def OptimizeSubArray(arr,k):
    l = 0
    r = 0
    n = len(arr)
    c = 0
    s = 0
    while r < n:
        s += arr[r]
        if s > k:
            s -= arr[l]
            l += 1
        if (s <= k):
            c = max(c, (r - l + 1))
        print(s)
        r += 1
    print(c)

OptimizeSubArray(arr,k)