s = "pwwkew"

def SubStr(s):
    n=len(s)
    l = 0
    for i in range(n):

        for j in range(0,n):
            sub=''
            for k in range(i,j+1):
                if s[k] in sub:
                    break
                else:
                    sub+=s[k]
                print(s[k], end='-')
            l=max(l,len(sub))
            print()
    print(l)


SubStr(s)


def SubOptimixzeStr(s):
    charSet=set()
    l=0
    res=0
    for i in range(len(s)):
        while s[i] in charSet:
            charSet.remove(s[l])
            l+=1
        charSet.add(s[i])
        res=max(res,i-l+1)

    print(res)


    # for j in range(len(s)-1):
    #     c = ''
    #     for i in range (j+1,len(s)):
    #         if  s[i]!=s[i-1] and s[i] not in c:
    #             c+=s[i]
    #         else:
    #             c=s[i]
    #         l=max(l,len(c))
    # print('ans:->',l)
SubOptimixzeStr(s)