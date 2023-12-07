# Palindrome number  type-divmod

def is_palindrome_number(n):
    if n<0:
        return "Число отрицательное!"
    new = 0
    orig = n
    while n:
        n,d=divmod(n,10)
        new=new*10+d
    return "Палиндром" if new==orig else "Не палиндром"


# Contains Duplicate type-hash

def is_duplicate(x):
    return "Нет дубликатов" if len(x)==len(set(x)) else "Есть дубликаты"



# Counting Bits type-bitwise

def count_bits(n):
    ans=[0]
    for i in range(1,n+1):
        cur=0
        while i:
            cur+=i & 1
            i>>=1
        ans.append(cur)
    return ans




# Unique Email Adressess  type-hash

def num_unique_emails(emails: list[str]):
    unique=set()
    for e in emails:
        name, dom = e.split("@")
        name=name.split("+")[0]
        name=name.replace(".", "")
        unique.add(f"{name}@{dom}")
    return len(unique)


# Maximum Average Subarray type-sliding window
def find_max_average(nums: list[int],k: int):
    ans=-float("inf")
    cnt=0
    cur=0
    for i in range(len(nums)):
        cur+=nums[i]
        cnt+=1
        if cnt==k:
            ans=max(ans,cur/k)
        if cnt>k:
            cur-=nums[i-k]
            ans=max(ans,cur/k)
    return ans

# Move Zeroes type-two pointers

def move_zeroes(nums :list[int]):
    j=0
    for i in range(len(nums)):
        if nums[i]!=0:
            nums[i],nums[j]=nums[j],nums[i]
            j+=1
    return nums
# return sorted(nums,key=lambda x: x==0)

# Valid perfect Square type-binary search

def is_perfect_square(num :int):
    if num==1:
        return True
    l, r = 1, num // 2
    while l<=r:
        mid=(l+r)//2
        sq=mid**2
        if sq==num:
            return True
        elif sq<num:
            l=mid+1
        else:
            r=mid-1
    return False


# Add Digits type-divmod

def add_digit(num :int):
    cnt=0
    while num:
        num,d=divmod(num,10)
        cnt+=d
    return cnt

# Student Attendance Record type-string

def check_record(s :str):            # A:absent, L:late, P:present
    l_cnt=0
    a_cnt=0
    for c in s:
        if c=="A":
            a_cnt+=1
            if a_cnt==2:
                return False
        elif c=="L":
            l_cnt+=1
            if l_cnt>2:
                return False
    return True


# Binary Tree Postorder Traversal type-tree    -пропустил



# is Subsequence  type-stack

def is_subsequence(s :str, t: str):
    stack=list(s)[::-1]
    for c in t:
        if stack and stack[-1]==c:
            stack.pop()
    return len(stack)==0


# Symmetric tree  type-tree - пропустил
class Solution:

    def is_symmetric(self,root):
        def helper(r1,r2):
            if not r1 and r2:
                return True
            if not r1 or not r2:
                return False
            return r1.val==r2.val and helper(r1.left, r2.right) and helper(r1.right, r2.left)
        return helper(root,root)

#sol=Solution.is_symmetric([1,2,2,3,4,4,3])




# Plus One type-divmod

def plus_one(digit):
    carry=1
    for i in range(len(digit)-1,-1,-1):
        carry,digit[i]=divmod(digit[i]+carry,10)
    return digit if not carry else [carry]+digit



# Meeting Romms type-sortings
def can_attend_meetingd(intervals: list[list[int]]):
    intervals.sort()
    for i in range(1,len(intervals)):
        if intervals[i][0]<intervals[i-1][0]:
            return False
    return True


# 


if __name__=="__main__":
    print(is_palindrome_number(121))
    print(is_duplicate([1,4,8,0]))
    print(count_bits(5))
    #print(num_unique_emails(["test@mail.ru", "test1@mail.list", "test1email.com"]))
    print(move_zeroes([7,0,-1,0,2,1]))
    print(is_perfect_square(9))
    print(add_digit(47))
    print(check_record("PPAALL"))
    print(is_subsequence("abc", "ahbgdc"))
    #print(sol)
    print(plus_one([9]))
    print(can_attend_meetingd([[0,30],[5,10],[15,20]]))

