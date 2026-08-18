class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        nums = set(nums)
        for i in nums:
            if (i - 1) not in nums:
                temp = i
                count = 1
                while temp + 1 in nums:
                    count += 1
                    temp = temp + 1
                res = max(res, count)
        return res
