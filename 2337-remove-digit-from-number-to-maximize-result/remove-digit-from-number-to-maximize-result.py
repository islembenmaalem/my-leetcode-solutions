class Solution(object):
    def removeDigit(self, number, digit):
        """
        :type number: str
        :type digit: str
        :rtype: str
        """
        a = []
        for i in range(len(number)):
            if number[i] == digit:
                a.append(number[0:i]+number[i+1:]) 
        print(a)
        return max(a)

        
        