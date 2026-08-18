class MedianFinder:

    def __init__(self):
        # we can have 2 heaps, small which will be a maxheap and large which will be a minheap
        # both the heaps should be of equal size
        self.small = []
        self.large = []    

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1 * num)

        # make sure every element in small is <= every element in large
        # at 0th position in minheap, we have the smallest element. We dont have maxheap in python so we take negative of every element
        if (self.small and self.large and 
            (-1 * self.small[0]) > self.large[0]):
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        # uneven size:
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        if len(self.small) < len(self.large):
            return self.large[0]
        return (-1 * self.small[0] + self.large[0]) / 2





        
        