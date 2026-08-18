class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        res = 0
        while l<r:
            height = min(heights[l], heights[r])
            width = r - l
            area = height * width
            res = max(area, res)
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return res
        