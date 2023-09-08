a=[-6,1,3,-1,2,4,11]
k=5
for i in a[0:len(a)//2]:
    for j in a[len(a)//2:]:
        if i+j==k:
            print(i,j)