class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A = nums1
        B = nums2
        total = len(nums1) + len(nums2)
        half = total // 2
        if len(A) > len(B):
            B, A = A, B
        l = 0
        r = len(A) - 1
        while True:
            i = (l + r) // 2 # A
            j = half - i - 2 # B (-2 because array is 0 indexed as i it actually for eg 2 but 0,1,2 i.e. 3 elements and also half is also 1 indexed so -1 more.)

            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i+1] if (i + 1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j+1] if (j + 1) < len(B) else float("infinity")

            # if partition is correct
            if Aleft <= Bright and Bleft <= Aright:
                if total%2: #odd length
                    return min(Aright, Bright)
                return (max(Aleft, Bleft) + min(Aright, Bright))/2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1
        

        
        