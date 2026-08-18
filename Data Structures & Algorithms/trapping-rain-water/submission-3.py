class Solution:
    def trap(self, height: List[int]) -> int:
    
        l = 0
        r = len(height) - 1
        maxLeft = height[l]
        maxRight = height[r]
        ans = 0

        while l<r:
            if maxLeft <= maxRight:
                l += 1
                maxLeft = max(maxLeft, height[l])
                ans += maxLeft - height[l]   # No need to check for min(maxl,maxr)
                # because in the if condition we are already checking if maxLeft < maxRight and it will be smaller only
                # cause if its greater than maxright then height at current point will be == to maxleft so it would become 0
                # and if its leff then that that means current height is also not greater than maxleft otherwise it would have gotten updated.
            else:
                r -= 1
                maxRight = max(maxRight, height[r])
                ans += maxRight - height[r]
        return ans















        # n = len(height)
        
        # leftmax = [0] * n
        # rightmax = [0] * n

        # leftmax[0] = height[0]
        # rightmax[n-1] = height[n-1]

        # for i in range(1, n):
        #     leftmax[i] = max(leftmax[i-1], height[i])

        # for i in range(n-2, -1, -1):
        #     rightmax[i] = max(rightmax[i+1], height[i])

        # ans = 0
        # for i in range(n):
        #     curr = abs(min(leftmax[i], rightmax[i]) - height[i])
        #     ans+=curr
        # return ans


        