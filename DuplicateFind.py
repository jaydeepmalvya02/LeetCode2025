arr=[1,3,4,2,2]

def Duplicate(arr):
    slow=0
    fast=0
    while True:
        slow=arr[slow]
        fast=arr[arr[fast]]

        if slow==fast:
            break

    slow2=0

    while True:
        slow=arr[slow]
        slow2=arr[slow2]
        if slow==slow2:
            return slow

x=Duplicate(arr)
print(x)
