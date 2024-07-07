class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        if x<0:
            return False
        else :
            xs = str(x)
            if len(xs)<=4:
                return xs[0]==xs[-1]
            for i in range(0,len(xs)):
              #  print(xs[i]==xs[len(xs)-i-1])
                if xs[i]==xs[len(xs)-i-1]:
                    pass
                else:
                    return False
            return True
        