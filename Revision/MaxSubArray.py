nums = [-2,1,-3,4,-1,2,1,-5,4]

def Brute(nums):
    n=len(nums)
    ms=float("-inf")
    for i in range(n):
        m=0
        for j in range(i,n):
            s=0
            for k in range(i,j+1):
                s+=nums[k]

            m=max(m,s)
        ms=max(m,ms)
    print("->",ms)


Brute(nums)

def Optimize(nums):
    s=0
    ans=float('-inf')
    for i in range(len(nums)):
        s+=nums[i]
        if s>ans:
            ans=s
        if s<0:
            s=0


    print(ans)
Optimize(nums)