nums = [1,2,3,4]

def Brute(nums):
    n=len(nums)
    ans=[]
    for i in range(n):
        m=1
        for j in range(n):
            if j==i:
                continue
            else:
                m*=nums[j]
        ans.append(m)
    print(*ans)
Brute(nums)

def Optimize(nums):
    n=len(nums)
    ans=[1]*n
    pref=1
    for i in range(n):
        ans[i]=pref
        pref*=nums[i]
    post=1
    for i in range(n-1,-1,-1):
        ans[i]*=post
        post*=nums[i]

    print(*ans)
Optimize(nums)
