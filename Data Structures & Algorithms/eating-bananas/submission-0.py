class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        ans = max(piles)
        
        while l <= r:
            k = (l + r)//2
            hours = 0
            for i in piles:
                hours += math.ceil(i / k)#hours += 1 if i < k or i//k

            if hours > h:
                l = k + 1
            else:
                ans = min(ans,k)
                r = k - 1
        return ans