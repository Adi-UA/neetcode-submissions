class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # find total, half, and shorter array
        A, B = nums1, nums2
        total = len(A) + len(B)
        half = total // 2
        if len(B) < len(A):
            A, B = B, A
        # search for left partition
        l, r = 0, len(A) - 1
        while True:
            # define boundary indices
            i = (l+r) // 2
            j = half - i - 2

            # Detect valid partition boundaries
            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i+1] if (i+1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j+1] if (j+1) < len(B) else float("infinity")

            # valid partition
            if Aleft <= Bright and Bleft <= Aright:
                # odd
                if total % 2:
                    return min(Aright, Bright) # should be on right of left partition
                # even
                return ( max(Aleft, Bleft) + min(Aright, Bright) ) / 2
            
            ### Update values: Binary search
            # Increase A 
            # A is too short, so start binary search AFTER midpoint (update l)
            elif Bleft > Aright:
                l = i + 1

            # Increase B
            # A too long, so update to search BEFORE midpoint (update r)
            else:
                r = i - 1