""" 189. Rotate Array - Medium"""
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        num_len=len(nums)
        backup=[None]*num_len
        k=k%num_len if k>num_len else k
        for idx,num in enumerate(nums):
            if idx+k<num_len and backup[idx+k]==None:
                    backup[idx+k]=nums[idx+k]
            if backup[idx]!=None:   
                nums[(idx+k)%num_len]=backup[idx] 
            else: 
                ## dont have to back up number to the left
                nums[(idx+k)%num_len]=num 
