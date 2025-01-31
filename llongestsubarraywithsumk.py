def longestSubarray(arr, k):
    left=right=0
    s=arr[0]
    ml=0
    n=len(arr)
    while right<n:
        while left<=right and s>k:
            s-=arr[left]
            left+=1
        if s==k:
            ml=max(ml,right-left+1)
        right += 1
        if right<n:
            s+=arr[right]

    return ml



# arr=[94 ,-33, -13, 40, -82, 94, -33, -13, 40, -82]
arr=[10, 5, 2, 7, 1, -10]
k=15
print(longestSubarray(arr, k))

# d = {}
# s = 0
# l = 0
# i = 0
# n = len(arr)
# while i < n:
#     s += arr[i]
#     if s == k:
#         l = max(len(arr[:i + 1]), l)
#     if s - k not in  d:
#         index = d[s - k]+1
#         l = max(len(arr[index:i + 1]), l)
#     d[s] = i
#     i += 1
# return l