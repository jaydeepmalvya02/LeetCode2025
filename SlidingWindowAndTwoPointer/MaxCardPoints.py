class Solution:
    def maxScore(self, cardPoints, k) :
        maxPoints = 0
        n = len(cardPoints)
        ls = 0
        for i in range(k):
            ls += cardPoints[i]
        maxPoints=ls
        rs = 0
        r=n-1
        for j in range(k - 1, -1,-1):
            ls -= cardPoints[j]
            rs += cardPoints[r]
            r-=1
        maxPoints = max( maxPoints,ls+rs)
        return maxPoints


cardPoints=[1,2,3,4,5,6,1]
k=3
s=Solution()
print(s.maxScore(cardPoints,k))
