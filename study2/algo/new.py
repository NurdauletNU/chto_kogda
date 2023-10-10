# Превращаем встроенный кортеж в словарь

tuple1=((1,"Bogdan"), (2, "Roman"))
dict1={}
for k,v in tuple1:
    dict1[k]=v
print(dict1)



# Проверка на уникальность элементов без множества
def hash_duplicate(nums):
    new: list = []
    for i in nums:
        if i not in new:
            new.append(i)
    return len(nums)==len(new)
print(hash_duplicate([1,2,3,4]))





# Бинарный поиск
def binary_search(arr, target):
    l,r=0, len(arr)-1
    while l<=r:
        mid=(l+r)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            l=mid+1
        else:
            r=mid-1
    return -1

print(binary_search(sorted([1,2,-1,24,0]),0))


s=input()
stack=[]
is_good=True
for i in s:
    if i in "([{":
        stack.append(i)
    elif i in ")]}":
        if not stack:
            is_good=False
            break
        open_bracket=stack.pop()
        if open_bracket=="(" and i==")":
            continue
if is_good and len(stack)==0:
    print("balanced")
else:
    print("not balanced")