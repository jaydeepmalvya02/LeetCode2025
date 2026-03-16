def LongPalin(s):
    s

    ans=set()
    for r in range(len(s)):
        for j in range(len(s)):

            sub=s[r:j+1]
            if sub==sub[::-1]:
                ans.add(sub)
    res=''
    for i in ans:
        if len(i)>len(res):
            res=i
    return ans

print(LongPalin( "babad"))

