class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l = []
        p=1
        for i in range(len(nums)):
            l.append(p)
            p*=nums[i]
        p=1
        for i in range(len(nums)-1, -1, -1):
            l[i] = l[i]*p
            p=p*nums[i]
        

        


        return l


            

        