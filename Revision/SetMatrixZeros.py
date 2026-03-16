matrix = [[1,1,1],[1,0,1],[1,1,1]]
r=len(matrix)
c=len(matrix[0])

def SetZero(matrix,r,c):
    row=[0]*r
    col=[0]*c
    for i in range(r):
        for j in range(c):
            if matrix[i][j]==0:
                row[i]=1
                col[j]=1
            print(matrix[i][j],end=' ')
        print()
    for i in range(r):
        for j in range(c):
            if row[i]==1 or col[j]==1:
                matrix[i][j]=0

    print(*matrix,end='\n')

SetZero(matrix,r,c)

