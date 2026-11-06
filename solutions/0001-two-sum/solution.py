class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        
        i=0
        
        while i<len(nums):
            l=[]
            s=nums[i]
            l.append(i)
            i+=1
            for n in range(len(nums[i:])):
                if s+nums[n+i]==target :
                    l.append(n+i)
                    return l
        
