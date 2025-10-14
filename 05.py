""" 80. Remove Duplicates from Sorted Array II. Medium """

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx=0
        key_cnt={}
        for num in nums:
            if num not in key_cnt:
                nums[idx]=num
                key_cnt.update({num:1})
                idx+=1
            elif key_cnt[num]==1:
                nums[idx]=num
                key_cnt.update({num:2})
                idx+=1
        return idx
