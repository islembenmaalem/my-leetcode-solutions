class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        n = len(nums)
        for i in range(n):
            t = target - nums[i]
            if t in d:
                return [d[t],i]
            else : 
                d[nums[i]] = i
        