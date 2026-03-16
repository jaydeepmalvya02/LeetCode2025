n=11
def SquareRoot(n):
    ans=0
    low=1
    high=n
    while low<=high:
        mid=(low+high)//2
        if mid*mid==n:
            ans=mid
            break
        elif mid*mid>n:
            ans=mid-1
            high=mid-1
        else:
            low=mid+1

    print(high)
SquareRoot(n)