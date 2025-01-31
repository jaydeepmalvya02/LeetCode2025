mat=[
    [1,1,1,1],
    [1,0,0,1],
    [1,1,0,1],
    [1,0,1,1]
]
r=len(mat)
c=len(mat[0])
def SetZero(mat,r,c):
    rows=[-1]*r
    col=[-1]*c
    for i in  range(r):
        for j in range(c):
            if mat[i][j]==0:
                rows[i]=0
                col[j]=0
    for i in range(r):
        for j in range(c):
            if rows[i]==0 or col[j]==0:
                mat[i][j]=0

    # print(rows)
    for i in range(r):
        print(mat[i])
SetZero(mat,r,c)


def setZeroes(matrix):
    r = len(matrix)
    c = len(matrix[0])
    col0 = 1
    for i in range(r):
        for j in range(c):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                if j != 0:
                    matrix[0][j] = 0
                else:
                    col0 = 0
    for i in range(1,r):
        for j in range(1,c):
            if matrix[i][j] != 0:
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0

    if matrix[0][0] == 0:
        for i in range(c):
            matrix[0][i] = 0
    if col0 == 0:
        for j in range(r):
            matrix[j][0] = 0
    return matrix
matrix=[[0,1,2,0],[3,4,5,2],[1,3,1,5]]
setZeroes(matrix)


