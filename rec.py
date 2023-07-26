def calculate(a,b):
    big_count=a if a>b else b
    while 1:
        if big_count%a==0 and big_count%b==0:
            num=big_count
            break
        big_count+=1
    return num



print(calculate(*map(int,input().split())))

print()
print()







def nat_chislo(x):
    con=1
    while x>con**2:
        print(con**2,end=" ")
        con+=1



nat_chislo(int(input()))

print()
print()





n = int(input())
sum = 0
for i in range(1, n + 1):
    sum += i
for i in range(n - 1):
    sum -= int(input())
print(sum)


