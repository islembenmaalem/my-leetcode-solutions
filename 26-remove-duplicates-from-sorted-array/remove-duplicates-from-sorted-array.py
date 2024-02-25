class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        expectedNums =[]
        i=0
        while i<n:
            unique_element = nums[i]
            if unique_element not in expectedNums:
                expectedNums.append(unique_element)
                i+=1
                n=len(nums)
            else:
                del nums[i]
                n=len(nums)
                
            
        

                
                
        nums = expectedNums
        return len(expectedNums)
