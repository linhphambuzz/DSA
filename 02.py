# 88. Easy - Merge Sorted Array 

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
       
        n_idx=m
        for s2 in nums2:
            nums1[n_idx]=s2
            n_idx+=1
            if n_idx == m+n:
                break 
        
        nums1.sort()
