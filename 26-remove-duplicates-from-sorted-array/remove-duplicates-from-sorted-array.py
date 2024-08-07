class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        out = [nums[0]]
        for element in nums[1:] :
            if element in out:
                nums.remove(element)
            if element not in out :
                out.append(element)
            
            
       
        return  len(out)
           
            