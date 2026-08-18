class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1]*len(nums)
        prod = 1
        for i in range(len(nums) - 1):
            prod = prod * nums[i]
            output[i+1] = prod
        prod = 1
        for i in range(len(nums) - 1, 0, -1):
            prod = prod * nums[i]
            output[i-1] = output[i-1] * prod
        
        return output
        









# can also do using division