nums = [-1,0,1,2,-1,-4]
def ThreeSumBrute(nums):
    ans=[]
    n=len(nums)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if(i!=j and i!=k and j!=k):
                    s=nums[i]+nums[j]+nums[k]
                    if s==0:
                        print([nums[i],nums[j],nums[k]])
                        print(i,j,k)

        print()

ThreeSumBrute(nums)

def ThreeOptimize(nums):
    n=len(nums)
    ans=[]
    nums.sort()
    i=0
    while i<n:
        if i>0 and nums[i-1]==nums[i]:
            pass
        else:
            j=i+1
            k=n-1
            while j<k:
                s=nums[i]+nums[j]+nums[k]
                if s==0:
                    ans.append([nums[i],nums[j],nums[k]])
                    k-=1
                    j+=1
                    while j<k and nums[j-1]==nums[j]:
                        j+=1
                    while j<k and nums[k]==nums[k+1]:
                        k-=1
                elif s<0:
                    j+=1
                else:
                    k-=1
        i+=1
    print(*ans)
ThreeOptimize(nums)

