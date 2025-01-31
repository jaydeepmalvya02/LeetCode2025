arr = [0, 1, 2, 0, 1, 2, 1, 2, 0, 0, 0, 1]


def Sort012(arr):
    n = len(arr)
    low = 0
    mid = 0
    high = len(arr) - 1
    while mid<= high:
        # if arr[low] == 0:
        #     low += 1
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low+=1
            mid+=1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high-=1
    print(arr)


        # if arr[high] == 0 and arr[low] == 2:
        #     arr[high], arr[low] = arr[low], arr[high]
        #     low += 1
        #     high -= 1
        # if arr[high] == 0 and arr[mid] == 2:
        #     arr[mid], arr[high] = arr[high], arr[mid]
        #     mid += 1
        #     high -= 1
        # if arr[high] == 1 and arr[mid] == 2:
        #     arr[mid], arr[high] = arr[high], arr[mid]
        #     mid += 1
        #     high -= 1




Sort012(arr)


def sortArray(arr):
    low = 0
    mid = 0
    high = len(arr) - 1

    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1


# arr = [0, 2, 1, 2, 0, 1]
# arr=[0, 1, 2, 0, 1, 2, 1, 2, 0, 0, 0, 1]
# sortArray(arr)
# print("After sorting:")
# for num in arr:
#     print(num, end=" ")
# print() 

