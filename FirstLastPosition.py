arr=[5,7,7,8,8,10]
target=8
def FirstLastIndex(arr,target):
    #o(n)
    # first=-1
    # last=-1
    # for i in range(len(arr)):
    #     if arr[i]==target:
    #         if first==-1:
    #             first=i
    #
    #         last=i
    # return [first,last]
    def First(arr,target):
        start = 0
        end = len(arr) - 1
        first = -1

        while start <= end:
            mid = (start + end) // 2
            if arr[mid] == target:
                first = mid
                end = mid - 1
            elif arr[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return first
    def Second(arr,target):
        start = 0
        end = len(arr) - 1

        last = -1
        while start <= end:
            mid = (start + end) // 2
            if arr[mid] == target:
                last= mid
                start=mid+1
            elif arr[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return last
    x=First(arr,target)
    if x==-1:
        return [-1,-1]
    y=Second(arr,target)
    return [x,y]

x=FirstLastIndex(arr,target)
print(x)
