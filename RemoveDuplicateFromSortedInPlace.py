arr=[1,1,2,2,2,3,3,4,5,6]
def RemoveDuplicate(arr):
    n=len(arr)
    i=0
    j=1
    while j<n:

        if arr[j]!=arr[j-1] and i!=j-1:

            arr[i+1]=arr[j]
            i+=1
        j+=1
    print(arr)
    s=set()
    s.add(1)
    # print(s)







    # s=set(arr)
    # index=0
    # for i in s:
    #     arr[index]=i
    #     index+=1
    # print(arr)
    # print(index)




RemoveDuplicate(arr)