def TwoSum(num,target):
    h={}
    for i in range(len(num)):
        s=target-num[i]
        if s in h:
            return (h[s],i)
        h[num[i]]=i

print(TwoSum([2,7,11,15],9))




def BestBuySellStock(arr):
    mp=arr[0]
    maxp=0
    for i in range(1,len(arr)):
        p=arr[i]-mp
        mp=min(arr[i],mp)
        maxp=max(p,maxp)
    return maxp

print(BestBuySellStock( [7,1,5,3,6,4]))

def ProductExceptSelf(arr):
    ans=[1]*len(arr)
    prefix=1
    for i in range(len(arr)):
        ans[i]=prefix
        prefix*=arr[i]
    suffix=1
    for i in range(len(arr)-1,-1,-1):
        ans[i]*=suffix
        suffix*=arr[i]
    return ans
print(ProductExceptSelf( [1,2,3,4]))


def MaxSubarr(arr):
    ans=float('-inf')
    s=0
    for i in range(len(arr)):
        s+=arr[i]
        if s<0:
            s=0
        ans=max(ans,s)
    return ans
print(MaxSubarr([-2,1,-3,4,-1,2,1,-5,4]))



def MinInRotatedArr(arr):
    left=0
    right=len(arr)-1
    while left<right:
        mid=(left+right)//2
        if arr[left]<arr[right]:
            right=mid-1
        else:
            left=mid
    return arr[left]


print(MinInRotatedArr([4,5,1,2,3]))

def ThreeSum(arr):
    ans=[]
    arr.sort()
    for i in range(len(arr)):
        if i>0 and arr[i]==arr[i-1]:
            pass
        else:
            j = i+1
            k = len(arr) - 1
            while j < k:
                s=arr[i] + arr[j] + arr[k]
                if s == 0:
                    ans.append([arr[i], arr[j], arr[k]])
                    j += 1
                    k -= 1
                    while j < k and arr[j] == arr[j + 1]:
                        j += 1
                    while j<k and arr[k] == arr[k - 1]:
                        k -= 1
                elif s<0:
                    j+=1
                else:
                    k-=1



    return ans
print(ThreeSum( [-1,0,1,2,-1,-4]))

def container(arr):
    ans=0
    l=0
    r=len(arr)-1
    while l<r:
        w=r-l
        h=min(arr[l],arr[r])
        if arr[l]<arr[r]:
            l+=1
        else:
            r-=1
        ans=max(ans,w*h)


    return ans
print(container([1,8,6,2,5,4,8,3,7]))



def SetMatZero(arr):
    r=len(arr)
    c=len(arr[0])
    rows=[0]*r
    cols=[0]*c
    for i in range(r):
        for j in range(c):
            if arr[i][j]==0:
                rows[i]=1
                cols[j]=1

    for i in range(r):
        for j in range(c):
            if cols[j] ==1 or rows[i]==1:
                arr[i][j]=0
    return arr



print(SetMatZero([[1,1,1],[1,0,1],[1,1,1]]))










# def TwoSum(arr,t):
#     d={}
#     for i in range(len(arr)):
#         s=t-arr[i]
#         if s in d:
#             return (d[s],i)
#         else:
#             d[arr[i]]=i
#
#
# print(TwoSum( [2,7,11,15],9))
#
#
#
#
#
# def BestTimeToBuyAndSell(arr):
#     maxP=float('-inf')
#     mini=arr[0]
#     for i in range(1,len(arr)):
#         p=arr[i]-mini
#         mini=min(arr[i],mini)
#         maxP=max(maxP,p)
#     return maxP
#
#
# print(BestTimeToBuyAndSell([7,1,5,3,6,4]))
#
# def ProductExceptSelf(arr):
#     n=len(arr)
#     ans=[1]*n
#     prefix=1
#     for i in range(n):
#         ans[i]=prefix
#         prefix*=arr[i]
#     suffix=1
#     for j in range(n-1,-1,-1):
#         ans[j]*=suffix
#         suffix*=arr[j]
#     return ans
# print(ProductExceptSelf([1,2,3,4]))
#
# def MaxSubarray(arr):
#     maxSum=float('-inf')
#     n=len(arr)
#     s = 0
#     for i in range(n):
#         s+=arr[i]
#         if s<0:
#             s=0
#         maxSum=max(s,maxSum)
#     return maxSum
#
# print(MaxSubarray( [-2,1,-3,4,-1,2,1,-5,4]))
#
#
#
#
# def MaxProSubArray(arr):
#     maxP=float('-inf')
#     s=1
#     for i in range(len(arr)):
#         s*=arr[i]
#         maxP=max(maxP,s)
#     if maxP==1:
#         return max(arr)
#     else:
#         return maxP
#
#
# print(MaxProSubArray([2,3,-2,4]))
#
# def FindMinRotatedArray(arr):
#     low=0
#     high=len(arr)-1
#     while low<high:
#         mid=(low+high)//2
#         if arr[mid]>arr[high]:
#             low=mid+1
#
#         else:
#             high=mid
#     return low
#
# print(FindMinRotatedArray([4,5,1,2,3]))
#
#
#
#
#
#
# # def TwoSum(arr,target):
# #     d={}
# #     for i in range(len(arr)):
# #         r=target-arr[i]
# #         if r in d:
# #             return d[r],i
# #         else:
# #             d[arr[i]]=i
# #
# # print(TwoSum( [2,7,11,15],9))
# #
# # def BestTimeBuySellStocks(arr):
# #     maxp=float('-inf')
# #     mini=arr[0]
# #     for i in range(1,len(arr)):
# #         p=arr[i]-mini
# #         mini=min(arr[i],mini)
# #         maxp=max(maxp,p)
# #     return maxp
# # print(BestTimeBuySellStocks([7,1,5,3,6,4]))
# #
# #
# # def ProductExceptSame(arr):
# #     n=len(arr)
# #     ans=[1]*n
# #     suffix=1
# #     prefix=1
# #     for i in range(n):
# #         ans[i]=suffix
# #         suffix*=arr[i]
# #     for i in range(n-1,-1,-1):
# #         ans[i]*=prefix
# #         prefix*=arr[i]
# #     return  ans
# # print(ProductExceptSame( [1,2,3,4]))
# #
# # def MaxSubArrSum(arr):
# #     maxSum=float('-inf')
# #     s=arr[0]
# #     for i in range(1,len(arr)):
# #         s+=arr[i]
# #         if s<0:
# #             s=0
# #         else:
# #             maxSum=max(s,maxSum)
# #     return maxSum
# #
# #
# #
# #
# # print(MaxSubArrSum( [-2,1,-3,4,-1,2,1,-5,4]))
# #
# #
# #
# #
# # def MaxProdSubArr(arr):
# #     maxP=0
# #     s=1
# #     for i in range(len(arr)):
# #         s*=arr[i]
# #         if s<0:
# #             s=1
# #
# #         maxP=max(s,maxP)
# #     if maxP==1:
# #         return max(arr)
# #     else:
# #         return maxP
# # print(MaxProdSubArr([2,3,-2,4]))
# #
# # def FindMinInRotatedArr(arr):
# #     l=0
# #     r=len(arr)-2
# #     while l<r:
# #         mid=(l+r)//2
# #         if arr[l]>arr[r]:
# #             l=mid+1
# #         else:
# #             r=mid
# #     return arr[l]
# #
# # print(FindMinInRotatedArr([1,2,3,4,5]))
# #
# # def SearchInRotated(arr,target):
# #     l=0
# #     r=len(arr)-1
# #     while l<r:
# #         m=(l+r)//2
# #         if arr[m]==target:
# #             return m
# #         elif arr[l]>arr[r]:
# #             l=m+1
# #         else:
# #             r=m
# #     return -1
# #
# #
# # print(SearchInRotated([4,5,6,7,0,1,2],3))
# #
# #
# # def ThreeSum(arr):
# #     ans=[]
# #     arr.sort()
# #     n=len(arr)
# #     for i in range(n):
# #         if i>0 and arr[i]==arr[i-1]:
# #             pass
# #         else:
# #             j = i + 1
# #             k = n - 1
# #             while j < k:
# #                 s = arr[i] + arr[j] + arr[k]
# #                 if s == 0:
# #                     ans.append([arr[i],arr[j] ,arr[k]])
# #                     j+=1
# #                     k-=1
# #                     while j<k and arr[j]==arr[j-1]:
# #                         j+=1
# #                     while j<k and arr[k]==arr[k+1]:
# #                         k-=1
# #                 elif s<0:
# #                     j+=1
# #                 else:
# #                     k-=1
# #     return ans
# #
# #
# # print(ThreeSum( [-1,0,1,2,-1,-4]))
# #
# # def ContainerWithMostWater(arr):
# #     mini=arr[0]
# #     ans=0
# #     l=0
# #     r=len(arr)-1
# #     while l<r:
# #         h=min(arr[l],arr[r])
# #         w=r-l
# #         if arr[l]<arr[r]:
# #             l+=1
# #         else:
# #             r-=1
# #         ans=max(ans,w*h)
# #
# #
# #     return ans
# #
# #
# #
# # print(ContainerWithMostWater( [1,8,6,2,5,4,8,3,7]))
# #
# #
# # def SetMatZero(arr):
# #     r=len(arr)
# #     c=len(arr[0])
# #     row=[-1]*r
# #     col=[-1]*c
# #     for i in range(r):
# #         for j in range(c):
# #             if arr[i][j]==0:
# #                 row[i]=0
# #                 col[j]=0
# #     for i in range (r):
# #         for j in range(c):
# #             if row[i]==0 or col[j]==0:
# #                 arr[i][j]=0
# #
# #     return arr
# #
# # print(SetMatZero([[1,1,1],[1,0,1],[1,1,1]]))
# # def Reverse(arr):
# #     l=0
# #     r=len(arr)-1
# #     while l< r:
# #         arr[l],arr[r]=arr[r],arr[l]
# #         l+=1
# #         r-=1
# #     return arr
# #
# # def RotateImage(arr):
# #     r=len(arr)
# #     c=len(arr[0])
# #     for i in range(r):
# #         for j in range(i,c):
# #             if i!=j:
# #                 arr[i][j],arr[j][i]=arr[j][i],arr[i][j]
# #     for i in range(r):
# #         arr[i]=Reverse(arr[i])
# #     return arr
# #
# # print(RotateImage( [[1,2,3],[4,5,6],[7,8,9]]))
# #
# #
# # def LongSubStrWithOutRepeating(str):
# #     charSet=set()
# #     for i in range(len(str)):
# #         if str[i] not in charSet:
# #             charSet.add(str[i])
# #         else:
# #             while str[i] not in charSet:
# #                 charSet.remove(str[i])
# #     return len(charSet)
# #
# #
# # print(LongSubStrWithOutRepeating("abcabcbb"))
# #
# # def LongRepCharRepl(s,k):
# #     l=0
# #     maxc=0
# #     d={}
# #     ans=0
# #
# #     for r in range(len(s)):
# #         d[s[r]]=d.get(s[r],0)+1
# #         maxc=max(maxc,d[s[r]])
# #         if r-l+1-d[s[r]]>k:
# #             d[s[r]]-=1
# #         else:
# #             ans=max(ans,r-l+1)
# #     return ans
# #
# #
# # print(LongRepCharRepl("ABAB",2))
# #
# # def MinWindowSub(s,t):
# #     l=0
# #     start=-1
# #     minL=float('inf')
# #     cd={}
# #     wc={}
# #     formed=0
# #     for i in range(len(t)):
# #         cd[t[i]]=cd.get(t[i],0)+1
# #     required=len(cd)
# #
# #     for r in range(len(s)):
# #         c=s[r]
# #         wc[c]=wc.get(c,0)+1
# #         if c in cd and cd[c]==wc[c]:
# #             formed+=1
# #         wc[c]-=1
# #
# #         while l<r and formed==required:
# #             if r-l+1 < minL:
# #                 minL=r-l+1
# #                 start=l
# #             if s[l] in cd and wc[s[l]]<cd[s[l]]:
# #                 formed-=1
# #             l+=1
# #     return s[start:start+minL]
# #
# #
# #
# #
# # print(MinWindowSub("ADOBECODEBANC","ABC"))
# #
# # # arr= [2,7,11,15]
# # # target=9
# # # def TwoSum(arr,target):
# # #     d={}
# # #     for i in range(len(arr)):
# # #         r=target-arr[i]
# # #         if r in d:
# # #             return (d[r],i)
# # #         d[arr[i]]=i
# # #
# # # print(TwoSum(arr,target))
# # #
# # #
# # # def BestTimeToBuySellStocks(arr):
# # #     mini=arr[0]
# # #     maxp=float("-inf")
# # #     for i in range(1,len(arr)):
# # #         p=arr[i]-mini
# # #         mini=min(arr[i],mini)
# # #         maxp=max(maxp,p)
# # #     return maxp
# # #
# # # print(BestTimeToBuySellStocks([7,1,5,3,6,4]))
# # #
# # #
# # # def ProductOfArrayExceptSelf(arr):
# # #     n=len(arr)
# # #     ans=[1]*n
# # #     prefix=1
# # #     suffix=1
# # #     for i in range(n):
# # #         ans[i]=prefix
# # #         prefix*=arr[i]
# # #     for j in range(n-1,-1,-1):
# # #         ans[j]*=suffix
# # #         suffix*=arr[j]
# # #     return ans
# # #
# # #
# # # print(ProductOfArrayExceptSelf([1,2,3,4]))
# # #
# # #
# # # def MaxSubArraySum(arr):
# # #     mxs=0
# # #     s = 0
# # #     for i in range(len(arr)):
# # #
# # #         s+=arr[i]
# # #         if s<0:
# # #             s=0
# # #         mxs=max(s,mxs)
# # #     return mxs
# # #
# # # print(MaxSubArraySum([-2,1,-3,4,-1,2,1,-5,4]))
# # #
# # #
# # #
# # # def MaxProdSubarray(arr):
# # #     maxp=0
# # #     s=1
# # #     for i in range(len(arr)):
# # #         s*=arr[i]
# # #         if s<0:
# # #             s=1
# # #         maxp=max(s,maxp)
# # #     if maxp==1:
# # #         return max(arr)
# # #     else:
# # #         return maxp
# # # print(MaxProdSubarray([-2,0,-1]))
# # #
# # #
# # #
# # #
# # # def SubarrayBitwiseOR(arr):
# # #     s = set()
# # #     n = len(arr)
# # #     for i in range(n):
# # #         ans = 0
# # #         for j in range(i, n):
# # #             ans |= arr[j]
# # #             if ans not in s:
# # #                 s.add(ans)
# # #     return len(s)
# # #
# # #
# # # print(SubarrayBitwiseOR([1,2,4]))
# # #
# # #
# # # def MiniInRotatedArr(arr):
# # #     left=0
# # #     right=len(arr)-1
# # #
# # #     while left<right:
# # #         mid=(left+right)//2
# # #
# # #         if arr[mid]>arr[right]:
# # #             left=mid+1
# # #         else:
# # #             right=mid
# # #     return arr[left]
# # #
# # #
# # #
# # # print(MiniInRotatedArr([3,4,5,1,2]))
# # #
# # # def SearchInRotatedArr(arr,target):
# # #     l=0
# # #     r=len(arr)-1
# # #     while l<r:
# # #         m=(l+r)//2
# # #         if arr[m]==target:
# # #             return m
# # #         elif arr[m]>arr[r] :
# # #             l=m+1
# # #         else:
# # #             r=m
# # #     return -1
# # #
# # # print("Ans :-",SearchInRotatedArr([4,5,6,7,0,1,2],3))
# # #
# # #
# # # def ThreeSum(arr):
# # #     n=len(arr)
# # #     ans=[]
# # #     arr.sort()
# # #     i=0
# # #     while i<n:
# # #         if i>0 and arr[i-1]==arr[i]:
# # #             pass
# # #         else:
# # #             j=i+1
# # #             k=n-1
# # #             while j<k:
# # #                 s=arr[i]+arr[j]+arr[k]
# # #                 if s==0:
# # #                     ans.append([arr[i],arr[j],arr[k]])
# # #                     k-=1
# # #                     j+=1
# # #                     while j<k and arr[j]==arr[j-1]:
# # #                         j+=1
# # #                     while j<k and arr[k]==arr[k+1]:
# # #                         k-=1
# # #                 elif s<0 :
# # #                     j+=1
# # #                 else:
# # #                     k-=1
# # #         i+=1
# # #     return ans
# # #
# # #
# # # print(ThreeSum( [-1,0,1,2,-1,-4]),"ans")
# # #
# # #
# # # def MostWaterContainer(arr):
# # #     n=len(arr)
# # #     l=0
# # #     r=n-1
# # #     ans=0
# # #     while l<r:
# # #         h=min(arr[l],arr[r])
# # #         w=r-l
# # #         if arr[l]<arr[r]:
# # #             l+=1
# # #         else:
# # #             r-=1
# # #         ans=max(ans,w*h)
# # #     return ans
# # #
# # #
# # #
# # #
# # # print(MostWaterContainer([1,8,6,2,5,4,8,3,7]))
# # #
# # #
# # # def SetMatrixZeros(arr):
# # #     r=len(arr)
# # #     c=len(arr[0])
# # #     row=[0]*r
# # #     col=[0]*c
# # #     for i in range(r):
# # #         for j in  range(c):
# # #             if arr[i][j]==0:
# # #                 row[i]=1
# # #                 col[j]=1
# # #     for i in range(r):
# # #         for j in range(c):
# # #             if row[i]==1 or col[j]==1:
# # #                 arr[i][j]=0
# # #     return arr
# # #
# # # print(SetMatrixZeros([[1,1,1],[1,0,1],[1,1,1]]))
# # #
# # #
# # # def SpiralMatrix(arr):
# # #     r=len(arr)
# # #     c=len(arr[0])
# # #     t=r*c
# # #     minr=0
# # #     maxr=r-1
# # #     minc=0
# # #     maxc=c-1
# # #
# # #     c=0
# # #     while c<t:
# # #         # Left-To-Right
# # #         i=minr
# # #         j=minc
# # #         while j<=maxc and c<t:
# # #             print(arr[i][j],end='->')
# # #             j+=1
# # #             c+=1
# # #         minr+=1
# # #
# # #         #Top-To-Bottom
# # #         i=minr
# # #         j=maxc
# # #         while i<=maxr and c<t:
# # #             print(arr[i][j], end='->')
# # #             c += 1
# # #             i+=1
# # #
# # #         maxc-=1
# # #
# # #         #Right-Left
# # #         i=maxr
# # #         j=maxc
# # #         while j>=minc and c<t:
# # #             print(arr[i][j], end='->')
# # #             c += 1
# # #             j-=1
# # #
# # #         maxr-=1
# # #
# # #         #bottom-top
# # #         i=maxr
# # #         j=minc
# # #         while i>=minr and c<t:
# # #             print(arr[i][j], end='->')
# # #             c+=1
# # #             i-=1
# # #         minc+=1
# # #     return arr
# # #
# # #
# # #
# # #
# # #
# # # print(SpiralMatrix([[1,2,3],[4,5,6],[7,8,9]]))
# # #
# # #
# # #
# # #
# # # def RotateImage(arr):
# # #     r=len(arr)
# # #     c=len(arr[0])
# # #     for i in range(r):
# # #         for j in range(i,c):
# # #             if i!=j:
# # #                 arr[i][j], arr[j][i]=arr[j][i],arr[i][j]
# # #     for i in range(r):
# # #         arr[i]=Reverse(arr[i])
# # #     return arr
# # #
# # #
# # #
# # #
# # #
# # # def Reverse(arr):
# # #     l=0
# # #     r=len(arr)-1
# # #     while l<r:
# # #         arr[l],arr[r]=arr[r],arr[l]
# # #         l+=1
# # #         r-=1
# # #     return arr
# # #
# # #
# # #
# # # print(RotateImage([[1,2,3],[4,5,6],[7,8,9]]))
# # #
# # #
# # # def exist(arr,word):
# # #     n = len(word)
# # #     r = len(arr)
# # #     c = len(arr[0])
# # #     row = [[0] * c for _ in range(r)]
# # #
# # #     def Search(arr, t,r,c):
# # #
# # #
# # #
# # #
# # #         for i in range(r):
# # #             for j in range(c):
# # #                 if arr[i][j] == t and (row[i][j] == 0):
# # #                     row[i][j] = 1
# # #                     return True
# # #
# # #         return False
# # #
# # #     for i in word:
# # #         if Search(arr, i,r,c) == False:
# # #             return False
# # #     return True
# # # print(exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"ABCB"))
# # #
# # # def LongSubStrWithoutRepeat(s):
# # #     n=len(s)
# # #     ans=0
# # #     str = set()
# # #     for i in range(n):
# # #
# # #         while s[i] in str:
# # #             str.remove(s[i])
# # #         str.add(s[i])
# # #         ans=max(len(str),ans)
# # #     return  ans
# # #
# # #
# # # print(LongSubStrWithoutRepeat("abcabcbb"))
# # #
# # #
# # #
# # # def MinWIndowSubStr(s,t):
# # #     l=0
# # #     start=-1
# # #     formed=0
# # #     d={}
# # #     wc={}
# # #     minL=float('inf')
# # #
# # #     for i in t:
# # #         if i in d:
# # #             d[i]+=1
# # #         else:
# # #             d[i]=1
# # #     required=len(d)
# # #     for r in range(len(s)):
# # #         char=s[r]
# # #         wc[char]=wc.get(char,0)+1
# # #         if char in d and wc[char]==d[char]:
# # #             formed+=1
# # #         wc[char]-=1
# # #         while l<r and formed==required:
# # #             if r-l+1<minL:
# # #                 minL=r-l+1
# # #                 start=l
# # #             if s[l] in d and wc[s[l]]<d[s[l]]:
# # #                 formed-=1
# # #
# # #
# # #             l+=1
# # #
# # #     return s[start:start+minL]
# # #
# # # print("ans",(MinWIndowSubStr("ADOBECODEBANC","ABC")))
# # #
# # #
# # #
# # #
# # #
# # # def LongestSubarrReplacement(s,t):
# # #     res=0
# # #     maxc=0
# # #     l=0
# # #     count={}
# # #     for r in range(len(s)):
# # #         c=s[r]
# # #         count[c]=count.get(c,0)+1
# # #         maxc=max(maxc,count[c])
# # #         if r-l+1-maxc>t:
# # #             count[c]-=1
# # #         res=max(res,r-l+1)
# # #     return res
# # #
# # # print(LongestSubarrReplacement("ABAB",2))
# # #
# # #
# # #
# # #
# # #
# #
# #
# #
# #
# # # def TwoSum(arr,target):
# # #
# # #     right=0
# # #     d={}
# # #     while right<len(arr):
# # #         s=target-arr[right]
# # #         if s in d:
# # #             return (d[s],right)
# # #
# # #         else:
# # #             d[arr[right]]=right
# # #         right+=1
# # # # print(TwoSum(arr= [2,7,11,15], target =9 ))
# # #
# # # def BestTimeToBuySellStocks(arr):
# # #
# # #     mini=arr[0]
# # #     maxi=float('-inf')
# # #     for i in range(1,len(arr)):
# # #         p=arr[i]-mini
# # #         mini= min(arr[i],mini)
# # #         maxi=max(p,maxi)
# # #     return maxi
# # # # print(BestTimeToBuySellStocks([7,1,5,3,6,4]))
# # #
# # # def ContainsDuplicate(arr):
# # #     s=set()
# # #     for i in arr:
# # #         if i in s:
# # #             return True
# # #         else:
# # #             s.add(i)
# # #     return False
# # #
# # # # print(ContainsDuplicate([1,2,3,1]))
# # #
# # # def ProdOfArrExceptSelf(arr):
# # #     n=len(arr)
# # #     ans=[1]*n
# # #     prefix = 1
# # #     suffix = 1
# # #     for i in range(n):
# # #         ans[i]=prefix
# # #         prefix*=arr[i]
# # #     for j in range(n-1,-1,-1):
# # #         ans[j]*=suffix
# # #         suffix*=arr[j]
# # #     return ans
# # #
# # # print(ProdOfArrExceptSelf([1,2,3,4]))
# # #
# #
# # # a=[1,3]
# # # a.append(a)
# # # print(a)
# # # print('a'+'b')
