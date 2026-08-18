class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        leftmin = [0] * n
        rightmin = [0] * n
        leftmin[0] = height[0]
        rightmin[n-1] = height[n-1]
        for i in range(1, n):
            leftmin[i] = max(leftmin[i-1], height[i])
        for i in range(n-2, -1, -1):
            rightmin[i] = max(rightmin[i+1], height[i])
        ans = 0
        for i in range(n):
            curr = abs(min(leftmin[i], rightmin[i]) - height[i])
            ans+=curr
        return ans


        