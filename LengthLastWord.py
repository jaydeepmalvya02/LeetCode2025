s="Hello World"

def LastWord(s):
    n=len(s)
    i=n-1
    c=0
    while s[i]==' ':
        i-=1
    while s[i]!=' ':
        c+=1
        i-=1
    print(c)
LastWord(s)