s="UUDDDDUUUUDDDDUU"
sealevel=0
valley=0
for i in s:
    if i=='D':
        sealevel+=1
    else:
        sealevel-=1
    if sealevel==0 and i=='U':
        valley+=1

print(valley)
