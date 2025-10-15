""" 169. Majority Element - Easy """
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        track={}
        for num in nums: 
            if num not in track:
                track.update({num:1})
            else:
                track[num]+=1
        
        key_max_cnt=max(track.values())
        for key,val in track.items():
            if val==key_max_cnt:
                return key
