class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        if len(nums)==1:
            return [f"{nums[0]}"]
        r=[]
        i=0
        j=1
        while j<len(nums):
            if nums[j-1]+1==nums[j]:
                j+=1
            
            else:
                r.append([nums[i],nums[j-1]])
                i=j
                j=j+1
            if j==len(nums):
                r.append([nums[i],nums[j-1]])
        s=[]
        for i in r:
            if len(set(i))==1:
                s.append(f"{i[0]}")
            else:
                s.append(f"{i[0]}->{i[1]}")

        return s
            

            


