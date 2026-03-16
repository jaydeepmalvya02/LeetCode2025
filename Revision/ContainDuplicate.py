nums = [1,2,3,1]
def Duplicate(nums):
    d={}
    for i in range(len(nums)):
        if nums[i] in d:
            d[nums[i]]+=1
        else:
            d[nums[i]]=1
    print(d)
    for j in d:
        if d[j]>1:
            return True
        else:
            return False

print(Duplicate(nums))