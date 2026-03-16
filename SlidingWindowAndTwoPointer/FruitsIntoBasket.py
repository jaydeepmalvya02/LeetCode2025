arr=[3,3,3,1,2,1,1,2,3,3,4]

def FruitBasketBrute(arr):

    n=len(arr)
    mx=0
    for i in range(n):
        s=set()
        for j in range(i,n):
            s.add(arr[j])
            if len(s)<=2:
                mx = max(mx, j - i + 1)

            else:
                pass
    print(mx)

FruitBasketBrute(arr)

def FruitBasketOptimal(arr):
    hd={}
    r=0
    l=0
    mx=0
    while r<len(arr):

        if arr[r] in hd:
            hd[arr[r]]+=1


        if  arr[r] not in hd:
            hd[arr[r]] = 1
        if len(hd)<=2 :
            mx = max(mx, r - l + 1)

        if len(hd)>2:
            while len(hd)>2:
                hd[arr[l]] -= 1
                if hd[arr[l]]==0:
                    hd.pop(arr[l])
                l+=1
        print(hd)
        r+=1
    print(mx)


FruitBasketOptimal(arr)