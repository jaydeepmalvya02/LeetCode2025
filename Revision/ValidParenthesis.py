s="({[)"

def ValidPar(s):
    d={'(':')','[':']','{':'}'}
    st=[]
    for i in s:
        if len(st)>0 :
            print(d[st[-1]])
            if i==d[st[-1]] :
                st.pop()
            else:
                st.append(i)
        else:
            st.append(i)
    if len(st)==0:
        return True
    else:
        return False
print(ValidPar(s))