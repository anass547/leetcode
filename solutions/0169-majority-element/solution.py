class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        s=set(nums)
        max=0
        one=0
        for i in s:
            if max<nums.count(i):
                max=nums.count(i)
                one=i
        return one
