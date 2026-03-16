prices = [7,1,5,3,6,4]

def BuyAndSell(prices):
    ans=0
    d={}
    mini=prices[0]
    m=float('-inf')
    for i in range(1,len(prices)):
        p=prices[i]-mini
        mini=min(prices[i],mini)
        m=max(p,m)

    return m
print(BuyAndSell(prices))
