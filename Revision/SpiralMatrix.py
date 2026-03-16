matrix = [[1,2,3],[4,5,6],[7,8,9]]
r=len(matrix)
c=len(matrix[0])
def SpiralMatrix(mat,r,c):
    minr=0
    minc=0
    maxr=r-1
    maxc=c-1
    total=r*c
    c=0

    while c<total:
        # Left->To->Right
        i=minr
        j=minc
        while j<=maxc and c<total:
            print(mat[i][j],end=' ')
            j+=1
            c+=1

        minr+=1

        # Top to Bottom
        i=minr
        j=maxc
        while i<=maxr and c<total:
            print(mat[i][j],end=' ')
            i+=1
            c+=1

        maxc-=1

        #Right to Left
        i=maxr
        j=maxc
        while j>=minc and c<total:
            print(mat[i][j],end=' ')
            j-=1
            c+=1

        maxr-=1


        #Bottom to Top

        i=maxr
        j=minc
        while i>=minr and c<total:
            print(mat[i][j],end=' ')
            i-=1
            c+=1

        minc+=1

SpiralMatrix(matrix,r,c)

