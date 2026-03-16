def PalindSubStr(s):
    n=len(s)
    c=0

    for i in range(n):
        for j in range(i,n):
            sub=''
            for k in range(i,j+1):
                sub+=s[k]
            print(sub)

            if Palind(sub)==True:
                c+=1
    return c


def Palind(s):
    if len(s)==1:
        return True
    else:
        arr=list(s)
        l=0
        r=len(arr)-1
        while l<r:
            arr[l],arr[r]=arr[r],arr[l]
            l+=1
            r-=1
        sub=''.join(arr)
        if s==sub:
            return True
        else:
            return False


print(PalindSubStr("aaa"))


