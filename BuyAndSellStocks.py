arr=[7,1,5,3,6,4]
def Stocks(arr):
    n=len(arr)
    mini=arr[0]
    mxprofit=0

    for i in range(1,n):
        p=(arr[i]-mini)
        mxprofit=max(mxprofit,p)
        mini=min(arr[i],mini)


    print(mxprofit)
Stocks(arr)