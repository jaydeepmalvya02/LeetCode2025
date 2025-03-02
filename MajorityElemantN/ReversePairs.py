def reversePairs(arr):
    n = len(arr)
    return MergeSort(arr, 0, n - 1)


def MergeSort( arr, low, high):
    c = 0
    if low >= high:
        return c
    mid = (low + high) // 2
    c += MergeSort(arr, low, mid)
    c += MergeSort(arr, mid + 1, high)
    c += CountPairs(arr, low, mid, high)
    Merge(arr, low, mid, high)
    return c


def Merge( arr, low, mid, high):
    c = 0
    t = []
    left = low
    right = mid + 1

    while left <= mid and right <= high:
        if arr[left] > arr[right]:
            t.append(arr[right])
            right += 1
        else:
            t.append(arr[left])
            left += 1
    while left <= mid:
        t.append(arr[left])
        left += 1
    while right <= high:
        t.append(arr[right])
        right += 1
    for i in range(low, high + 1):
        arr[i] = t[i - low]
    return c


def CountPairs(arr, low, mid, high):
    c = 0
    right = mid + 1
    for i in range(low, mid + 1):
        while right <= high and arr[i] > 2 * arr[right]:
            right += 1
        c += (right - (mid + 1))
    return c
arr=[2,4,3,5,1]
print(reversePairs(arr))