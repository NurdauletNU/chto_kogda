def while_sum(n):
    result=0
    while n>0:
        result+=n
        n-=1
    print(result)

while_sum(5)




def recursion_count(N):
    if N==1:
        return 1
    return N*recursion_count(N-1)
rs=recursion_count(5)
print(rs)





def nod(a,b):
    res=a if a<b else b
    while 1:
        if a%res==0 and b%res==0:
            rt=res
            break
        res-=1
    return rt




print(nod(14,21))


def recursia(c:int ,d=20):
    if c==d:
        return 0
    return c+recursia(c+1)


print(recursia(9))







aim="Нурдаулет"
def poisk_names(names):
    return True if aim in names else False


res=poisk_names(input().split())
print(res)










