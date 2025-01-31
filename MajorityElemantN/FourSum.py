arr=[1,0,-1,0,-2,2]
target=0
def FourSum(arr,target):
    n=len(arr)
    arr.sort()
    ans=[]
    i=0
    while i<n:
        if i>0 and arr[i-1]==arr[i]:
            pass
        else:
            j=i+1
            while j<n:
                if j!=i+1 and arr[j]==arr[j-1]:
                    pass
                else:
                    k=j+1
                    l=n-1
                    while k<l:
                        s=arr[i]+arr[j]+arr[k]+arr[l]
                        if s<target:
                            k+=1
                        elif s>target:
                            l-=1
                        else:
                            ans.append([arr[i],arr[j],arr[k],arr[l]])
                            l-=1
                            k+=1
                        # while k<l and arr[k]==arr[k-1]:
                        #     k+=1
                        # while k<l and arr[l]==arr[l+1]:
                        #     l-=1
                j+=1
        i+=1
    print(ans)
    # i=0
    # st=set()
    # while i<n:
    #
    #     j=i+1
    #     while j<n:
    #         hashset = set()
    #         k=j+1
    #         while k<n:
    #             s=target-(arr[i]+arr[j]+arr[k])
    #             if s in hashset:
    #                 t=[arr[i],arr[j],arr[k],s]
    #                 t.sort()
    #                 st.add(tuple(t))
    #
    #             else:
    #                 hashset.add(arr[k])
    #             k+=1
    #         j+=1
    #     i+=1
    # print(st)

    # ans=[]
    # st=set()
    # for i in range(n):
    #     for j in range(i+1,n):
    #         for s in range(j+1,n):
    #             for t in range(s+1,n):
    #                 total=arr[i]+arr[j]+arr[s]+arr[t]
    #                 if total==k:
    #                     st.add(tuple([arr[i],arr[j],arr[s],arr[t]]))
    # SC->2*no of quads
    # TC->n^4
    # print(list(st))
FourSum(arr,target)