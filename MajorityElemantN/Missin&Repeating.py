arr=[4,3,6,2,1,1]
def MissingRepeating(arr):
    n=len(arr)

    SN = (n * (n + 1)) // 2
    SN2 = (n * (n + 1) * (2 * n + 1)) // 6
    s1 = 0
    s2 = 0
    for i in range(n):
        s1 += arr[i]
        s2 += arr[i] * arr[i]
    val1 = (s1 - SN)
    val2 = (s2 - SN2)
    val2 = val2//val1
    x = (val1 + val2) // 2
    y=x-val1
    print(x,y)
MissingRepeating(arr)