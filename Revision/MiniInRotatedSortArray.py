nums = [ 5, 1, 2,3,4]

def MinSortRotate(nums):
    n=len(nums)
    left=0
    right=n-1

    while left<right:
        mid=(left+right)//2
        if nums[mid]>nums[right]:
            left=mid+1
        else:
            right=mid

    return nums[left]

print(MinSortRotate(nums))

