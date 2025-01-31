import copy

arr=[0]*5
print(id(arr))
a=arr.copy()
print(id(a),'->',a)
b=copy.deepcopy(a)
print(id(b),'->',b)
c=b
c.append(1)
b.append(2)
print(id(c),b,'->',a)
a.append(3)
print(arr)