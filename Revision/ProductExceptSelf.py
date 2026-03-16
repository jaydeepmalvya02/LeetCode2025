nums = [1,2,3,4]
#

def Product(nums):
    n=len(nums)
    ans=[1]*n
    prefix=1
    suffix=1
    for i in range(n):
        ans[i]=prefix
        prefix*=nums[i]
    for j in range(n-1,-1,-1):
        ans[j]*=suffix
        suffix*=nums[j]

    print(ans)

Product(nums)