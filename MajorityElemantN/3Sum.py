arr=[-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]
def ThreeSum(nums):
    n = len(nums)
    i = 0
    ans = []
    nums.sort()

    while i < n:
        if i > 0 and nums[i - 1] == nums[i]:
            pass
        else:
            j = i + 1
            k = n - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s == 0:
                    ans.append([nums[i], nums[j], nums[k]])
                    k -= 1
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1

                elif s < 0:
                    j += 1
                else:
                    k -= 1

        i += 1
    print(ans)
    # n=len(arr)
    # s=set()
    # for i in range(n):
    #     for j in range(i,n):
    #
    #         for k in range(j, n):
    #             if i!=j and i!=k and j!=k:
    #                 if arr[i]+arr[j]+arr[k]==0:
    #                     temp=[arr[i],arr[j],arr[k]]
    #                     temp.sort()
    #                     s.add(tuple(temp))
    #
    #
    # print(s)

ThreeSum(arr)