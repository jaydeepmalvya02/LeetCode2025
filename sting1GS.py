s="hello*3"
def Check(s):
    s=list(s)
    ans=''
    for i in range(len(s)):
        if ord(s[i])>=97 and ord(s[i])<123 and s[i]!='z' :

            ans+=chr(ord(s[i])+1)
        elif s[i]=='z':
            ans+='a'
    print(ans)

Check(s)
