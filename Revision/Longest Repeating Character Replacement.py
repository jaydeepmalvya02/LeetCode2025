
def Brute(s,k):
    ans=0
    index=0
    l=list(s)
    c = Frequency(s)
    while k and index<len(s):

        if l[index]!=c:
            l[index]=c
            index+=1
            k-=1
        else:
            index+=1

    res = 0
    for i in range(len(l)):
        if l[i]==c:
            res+=1
        else:
            res=0
        ans=max(res,ans)

    return ans



def Frequency(s):
    d={}
    for i in s:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    ans=max(d.values())
    maxFchar=[c for c,f in d.items() if f==ans]
    return maxFchar[0]


def characterReplacement(s, k):
    max_count = 0  # Max count of a single character in the current window
    count = {}     # Dictionary to store frequency of chars in current window
    left = 0
    result = 0

    for right in range(len(s)):
        count[s[right]] = count.get(s[right], 0) + 1
        max_count = max(max_count, count[s[right]])

        # If the remaining characters in window > k, shrink the window
        if (right - left + 1) - max_count > k:
            count[s[left]] -= 1
            left += 1

        # Update maximum result
        result = max(result, right - left + 1)

    return result
characterReplacement("ABAB",2)
