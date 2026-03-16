nums = [-2,1,-3,4,-1,2,1,-5,4]
def maxSubArray(nums):
    res = 0
    ans=float('-inf')
    n=len(nums)

    for i in range(n):
        res+=nums[i]
        if res>ans:
            ans=res
        if res<0:
            res=0


   # for j in range(k,n):

    print(ans)





maxSubArray(nums)