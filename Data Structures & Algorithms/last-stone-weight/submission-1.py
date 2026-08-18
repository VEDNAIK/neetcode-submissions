class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # python doesnt have max heap so convert the +ve value to -ve to simulate max heap
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            if x < y:
                heapq.heappush(stones, x - y)
        stones.append(0) # if list is empty then it will be 1st element else it would be 2nd and we are returning only the first element
        return abs(stones[0])
    