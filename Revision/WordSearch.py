word = "ABCCED"
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
r=len(board)
c=len(board[0])
def Search(arr,target,r,c):

    for i in  range(r):
        for j in range(c):
            if arr[i][j]==target:
                return True
    return False
def WordSearch(word):
    ans=False
    for i in range(len(word)):
        ans=Search(board,word[i],r,c)
        if ans==False:
            return False

    return True
print(WordSearch(word))



