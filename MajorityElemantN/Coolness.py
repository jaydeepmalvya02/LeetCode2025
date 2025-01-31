x=102
k=2
def Coolness(x,k):
    c=0
    sub = str(bin(k))
    # ss=''
    # for i in range(2,len(sub)):
    #     ss+=sub[i]
    for i in range(1,x+1):
        s=str(bin(i))
        c += s.count(sub)
        print(c)
    print(c)
Coolness(x,k)