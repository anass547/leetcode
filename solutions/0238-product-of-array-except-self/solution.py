
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n=math.prod(nums)
        if nums.count(0)>1:
            return [0]*len(nums)
        elif n==0:
            n=1
            for i in range(len(nums)):
                if nums[i]!=0:
                    n=n*nums[i]
            for i in range(len(nums)):
                if nums[i]==0:
                    nums[i]=n
                else:
                    nums[i]=0
        else:
            for i in range(len(nums)):
                nums[i]=int(n/nums[i])
        return nums

