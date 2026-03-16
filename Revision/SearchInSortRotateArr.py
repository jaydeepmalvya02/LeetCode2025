nums = [4,5,6,7,0,1,2],
target = 3

def Search(nums,target):
    left=0
    right=len(nums)-1
    while left<right:
        mid=(left+right)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]>nums[right]:
            left=mid+1
        else:
            right=mid
    return -1

print(Search(nums,target))

