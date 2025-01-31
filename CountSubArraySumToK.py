from collections import defaultdict

arr=[1,2,3,-3,1,1,1,3]
k=3
def SubArrayCount(arr,k):
    mp=defaultdict(int)
    mp[0]=1
    s=0
    c=0
    for i in range(len(arr)):
        s+=arr[i]
        r=s-k
        c+=mp[r]
        mp[s]+=1
    print(c)
SubArrayCount(arr,k)

arr = [1, 2, 3, -3, 1, 1, 1, 3]
k = 3

# without import
# def SubArrayCount(arr, k):
#     mp = {}
#     mp[0] = 1
#     s = 0
#     c = 0
#     for i in range(len(arr)):
#         s += arr[i]
#         r = s - k
#         if r in mp:
#             c += mp[r]
#         if s in mp:
#             mp[s] += 1
#         else:
#             mp[s] = 1
#
#     print(c)
#
#
# SubArrayCount(arr, k)