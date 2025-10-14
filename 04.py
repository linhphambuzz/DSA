""" 26. Remove Duplicates from Sorted Array """
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        holder=set()
        idx=0
        for num in nums:
            if num not in holder:
                holder.add(num)
                nums[idx]=num
                idx+=1
           
        return len(holder)
