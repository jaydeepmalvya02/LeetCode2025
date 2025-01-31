arr=[1,1,2,4,5,4,5]
def Once(arr):
    m={}
    for i in range(len(arr)):
        if arr[i] in m:
            m[arr[i]]+=1
        else:
            m[arr[i]]=1

    print(m)
    for i in m:
        if m[i]==1:
            print(i)
            return i

Once(arr)