arr=[
    [1,3,5,7],
    [10,11,16,20],
    [23,30,34,60]
]
target=16
def Search(arr,target):
    m=len(arr[0])

    start=0
    mid=m-1
    while start<m and mid>0:


        if arr[start][mid]==target:
            return [start,mid]
        elif arr[start][mid]>target:
            mid-=1

        else:
            start+=1


x=Search(arr,target)
print(x)




a=[1,2]
b=a
b.append(3)
print(a)