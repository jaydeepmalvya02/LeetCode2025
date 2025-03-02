def getFloorAndCeil(x, arr):
    arr.sort()
    floor = -1
    ciel = -1
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] > x:
            ciel = arr[mid]
            high = mid - 1
        elif arr[mid] == x:
            floor = arr[mid]
            ciel = arr[mid]
            break

        else:
            floor = arr[mid]
            low = mid + 1
    return floor, ciel
arr=[36, 82, 88, 56, 21, 17, 73, 86]
x=17
print(getFloorAndCeil(x, arr)
)