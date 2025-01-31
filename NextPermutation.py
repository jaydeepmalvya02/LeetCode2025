arr=[2,1,5,4,3,0,0]
n=len(arr)
def Permutation(arr,n):
    index=-1
    for i in range(n-2,-1,-1):
        if arr[i]<arr[i+1]:
            index=i
            break
    for j in range(n-1,index-1,-1):
        if arr[j]>arr[index]:
            arr[index],arr[j]=arr[j],arr[index]
            break


    return Reverse(arr,index+1,n-1)

def Reverse(arr,start,end):
    while start<end:
        arr[start],arr[end]=arr[end],arr[start]
        start+=1
        end-=1
    return arr

print(Permutation(arr,n))