mat = [[1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 10, 11, 12],
       [13, 14, 15, 16]
       ]
r=len(mat)
c=len(mat[0])


def SpiralPrint(mat,r,c):
    minr=0
    maxr=r-1
    minc=0
    maxc=c-1
    #top

    t = r * c
    count=0
    while count<t:
        i=minr
        j=minc
        while j<=maxc and count<t:
            print(mat[i][j],end=' ')
            j+=1
            count+=1

        minr+=1

        #right
        i=minr
        j=maxc
        while i<=maxr  and count<t:
            print(mat[i][j],end=' ')
            i+=1
            count-=1
        
        maxc-=1

        #bottom
        i=maxr
        j=maxc
        while j>=minc and count<t:
            print(mat[i][j], end=' ')
            j-=1
            count+=1
        maxr-=1

        #left
        i=maxr
        j=minc
        while i>=minr and count<t:
            print(mat[i][j], end=' ')
            i-=1
            count+=1
        minc+=1

SpiralPrint(mat,r,c)

