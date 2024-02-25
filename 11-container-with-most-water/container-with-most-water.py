class Solution:
    def maxArea(self, height: List[int]) -> int:
        aa =0
        i = 0
        j = len(height)-1
        while i<j:
            bar_min = min(height[i] ,height[j])
            diff = j-i
            a = bar_min * diff
            if  a>aa:
                aa=a
            if height[i] < height[j]:
                i+=1
            else :
                j-=1
        return aa
          
        

        