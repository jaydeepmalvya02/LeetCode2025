n=5

def PascalsTriangle(n):
    ans=[[1]]
    for i in range(n-1):
        temp=[0]+ans[-1]+[0]
        row=[]
        for j in range(len(ans[-1])+1):
            row.append(temp[j]+temp[j+1])
        ans.append(row)
    return ans
x=PascalsTriangle(5)


def GenerateRows(r):
    ans=1
    ansRow=[1]
    for i in range(1,r):
        ans=ans*(r-i)
        ans=ans//i
        ansRow.append(ans)

    print(ansRow)
    return ansRow
def Pascals2(n):
    ans=[]
    for i in range(1,n+1):
        x=GenerateRows(i)
        ans.append(x)
    print(ans)
Pascals2(6)
