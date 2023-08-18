# Maximum Average Subarray

class Solution4:
    def findMaxAverage(self,nums:list[int],k:int)->float:
        cur=sum(nums[:k])
        cur_max=cur

        for i in range(k,len(nums)):
            cur-=nums[i-k]
            cur+=nums[i]
            cur_max=max(cur,cur_max)
        return cur_max

f4=Solution4()
print(f4.findMaxAverage([1,12,-5,-6,50,3],4))

print()
print()



# Move Zeroes - переставить нули в конец

class Solution5:
    def moveZeroes(self,nums:list[int]):
        j=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[i],nums[j]=nums[j],nums[i]
                j+=1
        return nums
f5=Solution5()
print(f5.moveZeroes([0,1,0,3,12]))


# Valid Perfect Square бинарный поиск

class Solution6:
    def isPerfectSquare(self,num:int):
        if num==1:
            return True

        l,r=1,num//2
        while l<=r:
            mid=(l+r)//2
            sq=mid*mid
            if sq==num:
                return True
            if sq<num:
                l=mid+1
            else:
                r=mid-1
        return False


f6=Solution6()
print(f6.isPerfectSquare(81))


# Add Digits
class Solution7:
    def addDigits(self,num:int) -> int:
        while num>=10:
            cur=num
            new_num=0
            while cur:
                cur,d=divmod(cur,10)
                new_num+=d
            num=new_num
        return num
f7=Solution7()
print(f7.addDigits(22))



f7=Solution7()
print(f7.addDigits(38))

# Student Attendance Record

class Sulution8:
    def checkRecord(self,s:str) -> bool:
        l_cnt=0
        a_cnt=0
        for c in s:
            if c=="A":
                a_cnt+=1
                if a_cnt==2:
                    return False
            if c=="L":
                l_cnt+=1
                if l_cnt>2:
                    return False
            else:
                l_cnt=0
        return True

f8=Sulution8()
print(f8.checkRecord("PPAL"))

