# https://www.youtube.com/watch?v=7MK0GCSBoLg

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zero_count,i=0,0
        res=0
        for j in range(len(nums)):
            if nums[j]==0:
                zero_count+=1
            while zero_count>k:
                if nums[i]==0:
                    zero_count-=1
                i+=1
            res=max(res,j-i+1)
        return res