class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        k=(n+m)//2

        s=nums1+nums2
        s.sort()
        if (n+m)%2==1:
           
            return s[k]
        else:
            return (s[k-1]+s[k])/2
     