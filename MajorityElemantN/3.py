arr=[1,1,1,1,3,2,2,2]
def MajorityElement(arr):

    n=len(arr)
    c1=0
    c2=0
    e1=float('-inf')
    e2=float('-inf')
    ans=[]
    for i in range(n):
        if c1==0 and arr[i]!=e2:
            c1=1
            e1=arr[i]
        elif c2==0 and arr[i]!=e1:
            c2=1
            e2=arr[i]
        elif arr[i]==e1:
            c1+=1
        elif arr[i]==e2:
            c2+=1
        else:
            c1-=1
            c2-=1
    if c1>n//3:
        ans.append(e1)
    if c2>n//3:
        ans.append(e2)
    print(ans)

    # mp={}
    # mini=(n//3)+1
    # ans=[]
    # for i in arr:
    #
    #     if i in mp:
    #         mp[i]+=1
    #
    #     else:
    #         mp[i]=1
    #
    # print(ans)
MajorityElement(arr)