arr=[2,0,2,1,1,0]
# using bubblesort
def SortColors(arr):
    n=len(arr)
    for i in range(n):
        for j in range(1,n):
            if arr[j-1]>arr[j]:
                arr[j-1],arr[j]=arr[j],arr[j-1]

    return arr
x=SortColors(arr)
print(x)

#selection sort

def SelectionSort(arr):
    n=len(arr)
    for i in range(n):
        mini=i
        for j in range(i+1,n):
            if arr[j]<arr[mini]:
                mini=j
        arr[mini],arr[i]=arr[i],arr[mini]
    return arr
y=SelectionSort(arr)
print(y)

#inserstionSort

def InsertionSort(arr):
    n=len(arr)

    for i in range(1,n):
        temp=arr[i]
        j=i-1
        while j>=0 and temp<arr[j]:

            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=temp
    return arr
z=InsertionSort(arr)
print(z)

def QuickSort(arr):
    n=len(arr)
    if n<=1:
        return arr
    else:

        pivot=arr[0]

    lesser=[x for x in arr[1:] if x<=pivot]
    greater=[x for x in arr[1:] if x>pivot]

    return QuickSort(lesser)+[pivot]+QuickSort(greater)
a=QuickSort(arr)
print(a)