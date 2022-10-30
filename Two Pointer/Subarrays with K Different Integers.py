class Solution:

    # https://www.youtube.com/watch?v=akwRFY2eyXs

    def atmost(self,nums,k):
        right,left,count=0,0,0
        m={}
        for right in range(len(nums)):
            m[nums[right]]=1+m.get(nums[right],0)
            while len(m)>k:
                m[nums[left]]=m.get(nums[left])-1
                if m[nums[left]]==0:
                    del m[nums[left]]
                left+=1
            count+=right-left+1
            right+=1
        return count
            
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.atmost(nums,k)-self.atmost(nums,k-1)
