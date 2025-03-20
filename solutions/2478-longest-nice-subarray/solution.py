class Solution(object):
    def longestNiceSubarray(self,nums):
        left = 0
        bitmask = 0
        max_len = 0

        for right in range(len(nums)):
            while (bitmask & nums[right]) != 0:
                bitmask ^= nums[left]  # Remove nums[left]
                left += 1
            bitmask |= nums[right]  # Add nums[right]
            max_len = max(max_len, right - left + 1)

        return max_len
        
