s = "rat"
t = "tar"
def Anagram(s,t):
    ans=False

    for i in t:
        if i not in s:
            return False
        else:
            ans=True
    return ans
print(Anagram(s,t))

