# Palindrome Number

class Solution:
    def isPalindrome(self,x):
        orig=x
        c=0
        while x>9:
            x=x//10
            c=c*10+x
        return c==orig

f=Solution()
print(f.isPalindrome(545))
print()
print()
print()




# Contains Duplicate

class Solution1:
    def containsDuplicate(self,nums):
        return len(nums)!=len(set(nums))
f1=Solution1()
print(f1.containsDuplicate([1,2,3,3]))
print()
print()
print()




# Remove Linked List Elements - надо посмотреть заново 9:21-9:30


# Counting Bits

class Solution2:
    def countBits(self,n:int) -> list[int]:
        ans=[0]
        for i in range(1,n+1):
            cur=0
            while i:
                cur+=i&1
                i>>=1
            ans.append(cur)
        return ans
f2=Solution2()
print(f2.countBits(5))

print()
print()
print()



# Unique Email Addresses

class Solution3:
    def numUniqueEmails(self,emails: list[str]) ->int:

        unique=set()

        for e in emails:

            name,dom=e.split("@")

            name=name.split("+")[0]
            name=name.replace(".", "")

            unique.add(f"{name}@{dom}")
        return len(unique)

f3=Solution3()
print(f3.numUniqueEmails(["a@leetcode.com","b@leetcode.com","c@leetcode.com"]))



