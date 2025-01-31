arr=[100,102,100,101,101,4,3,2,3,2,1,1,1,2]
def LongestSubsequence(arr):

    n=len(arr)
    # Optimal
    s=set()
    for i in arr:
        s.add(i)
    long=1
    for i in s:
        if i-1 in s:
            c=1
            x=i
            while x in s:
                x+=1
                c+=1
            long=max(long,c)
    print(long)





    # arr.sort()
    # small=float('-inf')
    # longest=1
    # c=0
    # for i in range(n):
    #     x=arr[i]
    #     if x-1==small:
    #         c+=1
    #         small=arr[i]
    #     elif arr[i]!=small:
    #         c=1
    #         small=arr[i]
    #     longest=max(longest,c)
    #
    # print(longest)



    # longest=1
    # for i in range(n):
    #     x=arr[i]
    #     c=1
    #     while linearsearch(arr,x+1)==True:
    #         x=x+1
    #         c+=1
    #     longest=max(c,longest)
    # print(longest)



# def linearsearch(arr,x):
#     n=len(arr)
#     for i in range(n):
#         if arr[i]==x:
#             return True
#     return False

LongestSubsequence(arr)