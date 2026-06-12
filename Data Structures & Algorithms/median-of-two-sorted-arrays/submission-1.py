class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # we need to find the left partition
        A,B = nums1, nums2
        if len(A) > len(B):
            A,B = B,A
        m,n = len(A), len(B)
        left_part = (m+n)//2
        l,r = 0, m-1
        while True:
            mid_A = (l+r)//2
            mid_B = left_part - mid_A - 2
            

            # nums 1 L,R
            # nums 2 L,R
            # L1 < R1 and L2 <. R2 we got the left partition
            L1 = A[mid_A] if mid_A >= 0 else float("-inf")
            L2 = B[mid_B] if mid_B >= 0 else float("-inf")
            R1 = A[mid_A+1] if mid_A+1 < m else float("inf")
            R2 = B[mid_B+1] if mid_B+1 < n else float("inf")

            if L1 <= R2 and L2 <= R1:
                if (m+n)%2==0:
                    return (max(L1,L2)+min(R1,R2))/2
                return min(R1,R2)

            if L1 > R2:
                r = mid_A-1
            else:
                l = mid_A+1
        return -1

        
        




        