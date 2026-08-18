class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for i in nums:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        hashmap = dict(sorted(hashmap.items(), key=lambda item: item[1], reverse=True))
        ans = []
        for key in hashmap:
            if k == 0:
                break
            ans.append(key)
            k-=1
        return ans